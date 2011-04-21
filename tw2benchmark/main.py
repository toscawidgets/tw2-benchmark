#!/usr/bin/env python

if __name__ == '__main__':

    import widgets
    from widgets import test_wsgi_app_works
    test_wsgi_app_works()

    passes = 10
    for test in map(str, range(1, 8)):
        print
        print "-" * 72
        for lib in ['tw1', 'tw2']:
            from timeit import Timer
            func = "test%s" % test
            statement = "%s('%s')" % (func, lib)
            timer = Timer(
                stmt=statement,
                setup="from widgets import %s" % func,
            )
            t = timer.repeat(passes, 10)
            _min, _max, _avg = min(t), max(t), sum(t)/len(t)
            print "(%s)" % statement,
            print "", getattr(widgets, func).__doc__
            print "  min: %.4f usec/pass" % (passes * _min/passes),
            print "  max: %.4f usec/pass" % (passes * _max/passes),
            print "  avg: %.4f usec/pass" % (passes * _avg/passes)
