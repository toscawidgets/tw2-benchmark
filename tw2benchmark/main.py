#!/usr/bin/env python

if __name__ == '__main__':

    from widgets import test_wsgi_app_works
    test_wsgi_app_works()

    passes = 10
    for test in map(str, range(1, 7)):
        print "-" * 72
        for lib in ['tw1', 'tw2']:
            from timeit import Timer
            func = "test%s_%s" % (test, lib)
            timer = Timer(
                stmt=func + "()",
                setup="from widgets import %s" % func,
            )
            t = timer.repeat(passes, 10)
            _min, _max, _avg = min(t), max(t), sum(t)/len(t)
            print "Test %s on %s (%s())" % (test, lib, func)
            print "  min: %.4f usec/pass" % (passes * _min/passes),
            print "  max: %.4f usec/pass" % (passes * _max/passes),
            print "  avg: %.4f usec/pass" % (passes * _avg/passes)
