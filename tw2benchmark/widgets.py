#!/usr/bin/env python

from paste.registry import RegistryManager, Registry
import tw2.core
import tw.api
import ew
import ew.core

tw2csslink = tw2.core.CSSLink(filename='test.css')
tw1csslink = tw.api.CSSLink(filename='test.css')
ewcsslink = ew.CSSLink('test.css')
css_lookup = {
    'tw1' : tw1csslink,
    'tw2' : tw2csslink,
    'ew' : ewcsslink,
}

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


def make_wsgi_app(lib, prefunc, postfunc, middlewares, *args, **kwargs):
    widget = prefunc(lib, *args, **kwargs)

    def simple_app(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type','text/plain')]
        start_response(status, response_headers)
        return [postfunc(widget, **kwargs)]

    for ware in middlewares:
        simple_app = ware(simple_app)

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

def get_widget(lib):
    lookup = {
        'tw1' : get_tw1_widget,
        'tw2' : get_tw2_widget,
        'ew' : get_ew_widget,
    }
    return lookup[lib]()

def test_wsgi_app_works():
    # TODO
    return
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

def get_middlewares(lib):
    lookup = {
        'tw1' : [tw.api.make_middleware, RegistryManager],
        'tw2' : [tw2.core.make_middleware, RegistryManager],
        'ew'  : [ew.WidgetMiddleware, RegistryManager],
    }
    return lookup[lib]


def build_widget_smartly(lib, n_resources=1, *args, **kwargs):
    widget = get_widget(lib)
    widget.resources = [css_lookup[lib]]*n_resources
    if lib == 'ew':
        widget = widget()
    elif lib == 'tw1':
        widget = widget(kwargs['id'])
    elif lib == 'tw2':
        pass
    return widget

def test7(lib):
    """ Specifying parameters *and* displaying many times. """
    def prefunc(lib, *args, **kw):
        widget = build_widget_smartly(lib, **kw)
        return widget

    def postfunc(widget, **kwargs):
        for i in range(itertest_passes):
            widget.display(**kwargs)

        return widget.display(**kwargs)

    app = make_wsgi_app(lib, prefunc, postfunc, get_middlewares(lib),
                        id='some_id', boz='far')

    status, headers, body = fake_request(app, fake_env)

def test6(lib):
    """ Specifying parameters once, then displaying many times. """

    def prefunc(lib, *args, **kw):
        widget = build_widget_smartly(lib, **kw)
        if lib == 'tw2':
            widget = widget(**kw)
        return widget

    def postfunc(widget, **kwargs):
        for i in range(itertest_passes):
            if lib == 'tw1':
                widget.display(**kwargs)
            else:
                widget.display()

        if lib == 'tw1':
            return widget.display(**kwargs)
        else:
            return widget.display()

    app = make_wsgi_app(lib, prefunc, postfunc, get_middlewares(lib),
                        id='some_id', boz='far')

    status, headers, body = fake_request(app, fake_env)
        
def test5(lib):
    """ Instantiating widgets many times (and displaying them) """

    def prefunc(lib, *args, **kw):
        return None

    def postfunc(widget, **kwargs):
        for i in range(itertest_passes):
            widget = build_widget_smartly(lib, **kwargs)
            widget.display(**kwargs)

        return widget.display(**kwargs)

    app = make_wsgi_app(lib, prefunc, postfunc, get_middlewares(lib),
                        id='some_id', boz='far')

    status, headers, body = fake_request(app, fake_env)

def test4(lib):
    """ Setting up an app. Displaying once. """
    def prefunc(lib, *args, **kw):
        return build_widget_smartly(lib, *args, **kw)

    def postfunc(widget, **kwargs):
        return widget.display(**kwargs)

    app = make_wsgi_app(lib, prefunc, postfunc, get_middlewares(lib),
                        id='some_id', boz='far')

    status, headers, body = fake_request(app, fake_env)

def test3(lib):
    """ Setting up an app """
    def prefunc(lib, *args, **kw):
        return build_widget_smartly(lib, *args, **kw)

    def postfunc(widget, **kwargs):
        return widget.display(**kwargs)

    app = make_wsgi_app(lib, prefunc, postfunc, get_middlewares(lib),
                        id='some_id', boz='far')

def test2(lib):
    """ Handling many (duplicate) resources """
    def prefunc(lib, *args, **kw):
        return build_widget_smartly(lib, *args, n_resources=50, **kw)

    def postfunc(widget, **kwargs):
        return widget.display(**kwargs)

    app = make_wsgi_app(lib, prefunc, postfunc, get_middlewares(lib),
                        id='some_id', boz='far')

    status, headers, body = fake_request(app, fake_env)

def test1(lib):
    """ Handling many WSGI requests """
    def prefunc(lib, *args, **kw):
        return build_widget_smartly(lib, *args, **kw)

    def postfunc(widget, **kwargs):
        return widget.display(**kwargs)

    app = make_wsgi_app(lib, prefunc, postfunc, get_middlewares(lib),
                        id='some_id', boz='far')

    for i in range(itertest_passes):
        status, headers, body = fake_request(app, fake_env)
