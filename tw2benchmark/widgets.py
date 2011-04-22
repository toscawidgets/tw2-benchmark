#!/usr/bin/env python

from paste.registry import RegistryManager, Registry
import tw2.core
import tw.api
import ew
import ew.core

tw2csslink = tw2.core.CSSLink(filename='test.css')
tw1csslink = tw.api.CSSLink(filename='test.css')
ewcsslink = ew.CSSLink('test.css')

itertest_passes = 100

fake_env = {
    'PATH_INFO' : '/',
    'REQUEST_METHOD' : 'GET',
    'wsgi.url_scheme' : 'http', # easy_widgets depends on this.
}

def get_tw2_widget():
    class tw2Widget(tw2.core.Widget):
        template = "mako:tw2benchmark.templates.tw2"
        boz = tw2.core.Param('test', default='foo')

        def prepare(self):
            self.boz  = self.boz + "-bar"
            super(tw2Widget, self).prepare()
    return tw2Widget

def get_tw1_widget():
    class tw1Widget(tw.api.Widget):
        template = "mako:tw2benchmark.templates.tw1"
        params = ['boz']
        boz = 'foo'

        def update_params(self, d):
            d['boz'] = d['boz'] + "-bar"
            super(tw1Widget, self).update_params(d)
    return tw1Widget

def get_ew_widget():
    # TODO -- mako template? mako vs ew.Snippet isn't fair.  Use genshi.

    class ewWidget(ew.Widget):
        # NOTE -- this is not quite equivalent.  No 'prepare' or
        # 'update_params'.
        template = ew.Snippet(
            "<html><body id=\"${id}\">${boz}-bar</body></html>"
        )


    return ewWidget


def make_wsgi_app(widget, *args, **kwargs):
    if 'tw2id' in kwargs:
        widget = widget(*args, id=kwargs['tw2id'])
        del kwargs['tw2id']
    else:
        widget = widget(*args)

    def simple_app(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type','text/plain')]
        start_response(status, response_headers)
        return [widget.display(**kwargs)]
    return simple_app

def fake_request(app, environ):
    body = []
    status_headers = [None, None]
    def start_response(status, headers):
        status_headers[:] = [status, headers]
        return body.append
    app_iter = app(environ, start_response)
    try:
        for item in app_iter:
            body.append(item)
    finally:
        if hasattr(app_iter, 'close'):
            app_iter.close()
    return status_headers[0], status_headers[1], ''.join(body)

def make_tw1_wsgi_app(resource_multiplier=1):
    tw1Widget = get_tw1_widget()
    tw1Widget.resources = [tw1csslink] * resource_multiplier
    tw1_app = make_wsgi_app(tw1Widget, 'some_id', boz='far')
    tw1_app = tw.api.make_middleware(app=tw1_app)

    # Yuck -- tw1 requires this.
    tw1_app = RegistryManager(tw1_app)
    return tw1_app

def make_tw2_wsgi_app(resource_multiplier=1):
    tw2Widget = get_tw2_widget()
    tw2Widget.resources = [tw2csslink] * resource_multiplier
    tw2_app = make_wsgi_app(tw2Widget, tw2id='some_id', boz='far')
    tw2_app = tw2.core.make_middleware(app=tw2_app)

    # Just doing this to be fair to tw1
    tw2_app = RegistryManager(tw2_app)
    return tw2_app

def make_ew_wsgi_app(resource_multiplier=1):
    ewWidget = get_ew_widget()

    ewWidget.resources = [ewcsslink] * resource_multiplier

    ew_app = make_wsgi_app(ewWidget, id='some_id', boz='far')
    ew_app = ew.WidgetMiddleware(ew_app)

    # Just doing this to be fair to tw1
    ew_app = RegistryManager(ew_app)
    return ew_app

def get_widget(lib):
    lookup = {
        'tw1' : get_tw1_widget,
        'tw2' : get_tw2_widget,
        'ew' : get_ew_widget,
    }
    return lookup[lib]()

def make_specific_wsgi_app(lib, mul):
    lookup = {
        'tw1' : make_tw1_wsgi_app,
        'tw2' : make_tw2_wsgi_app,
        'ew' : make_ew_wsgi_app,
    }
    return lookup[lib](mul)

def test_wsgi_app_works():
    tw1_app = make_tw1_wsgi_app(1)
    tw2_app = make_tw2_wsgi_app(1)
    ew_app = make_ew_wsgi_app(1)
    status, headers, body1 = fake_request(tw1_app, fake_env)
    status, headers, body2 = fake_request(tw2_app, fake_env)
    status, headers, body3 = fake_request(ew_app, fake_env)
    body1 = body1.strip()
    body2 = body2.strip()
    body3 = body3.strip()
    assert(body1 == body2)
    assert(body2 == body3)

def fake_ew_middleware():
    """ TODO -- This does not work.

    I'm going to have to rewrite tests five through 9 to all use the wsgi stack
    since EasyWidgets depends on it so hard.

    """

    registry = Registry()
    registry.register(
        ew.widget_context,
        ew.core.WidgetContext(
            scheme='http',
            resource_manager=ew.ResourceManager()
        )
    )

def test9(lib):
    """ Minimizing tw2 subclasses with params in display """
    widget = get_widget(lib)
    if lib == 'tw1':
        widget = widget()
    for i in range(itertest_passes):
        foo = widget.display(boz='faz')

def test8(lib):
    """ Minimizing tw2 subclasses with params before display"""
    widget = get_widget(lib)
    if lib == 'tw1':
        widget = widget()
        for i in range(itertest_passes):
            foo = widget.display(boz='faz')
    elif lib == 'tw2':
        widget = widget(boz='faz')
        for i in range(itertest_passes):
            foo = widget.display()
    else:
        raise ValueError, 'lib is unrecognized'

def test7(lib):
    """ Specifying parameters *and* displaying many times. """
    widget = get_widget(lib)
    for i in range(itertest_passes):
        foo = widget().display(boz='faz')

def test6(lib):
    """ Specifying parameters once, then displaying many times. """
    widget = get_widget(lib)(boz='faz')
    for i in range(itertest_passes):
        widget.display(boz='faz')
        
def test5(lib):
    """ Instantiating widgets many times (and displaying them) """
    if lib == 'ew':
        fake_ew_middleware()
    for i in range(itertest_passes):
        foo = get_widget(lib)().display(boz='faz')

def test4(lib):
    """ Setting up an app. Displaying once. """
    app = make_specific_wsgi_app(lib, 1)
    fake_request(app, fake_env)

def test3(lib):
    """ Setting up an app """
    app = make_specific_wsgi_app(lib, 1)

def test2(lib):
    """ Handling many (duplicate) resources """
    app = make_specific_wsgi_app(lib, 50)
    for i in range(itertest_passes):
        status, headers, body = fake_request(app, fake_env)

def test1(lib):
    """ Handling many WSGI requests """
    app = make_specific_wsgi_app(lib, 1)
    for i in range(itertest_passes):
        status, headers, body = fake_request(app, fake_env)
