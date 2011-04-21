#!/usr/bin/env python

if __name__ == '__main__':

    import widgets
    from widgets import test_wsgi_app_works
    test_wsgi_app_works()

    print "tw2-benchmark"
    print "============="
    print "Comparing toscawidgets1 with tw2 for speed"
    print

    passes = 10
    for test in map(str, range(1, 8)):
        func = "test%s" % test
        print func + " -" + getattr(widgets, func).__doc__ + "::"
        print
        for lib in ['tw1', 'tw2']:
            from timeit import Timer
            statement = "%s('%s')" % (func, lib)
            timer = Timer(
                stmt=statement,
                setup="from widgets import %s" % func,
            )
            t = timer.repeat(passes, 10)
            _min, _max, _avg = min(t), max(t), sum(t)/len(t)
            print "  ", statement,
            print "  min: %.4f" % (passes * _min/passes),
            print "  max: %.4f" % (passes * _max/passes),
            print "  avg: %.4f" % (passes * _avg/passes)

        print
