#!/usr/bin/env python

if __name__ == '__main__':
    import datetime
    from timeit import Timer
    import hotshot, hotshot.stats

    import widgets

    from widgets import test_wsgi_app_works
    test_wsgi_app_works()

    num_tests = 7
    passes = 10

    print "tw2-benchmark"
    print "============="
    print "Comparing toscawidgets1 with tw2 for speed"
    print
    print "(generated: %s)" % datetime.datetime.now().strftime("%F")
    print

    print "tests with the ``timeit`` module"
    print "--------------------------------"
    print

    for test in map(str, range(1, num_tests+1)):
        func = "test%s" % test
        print func + " -" + getattr(widgets, func).__doc__ + "::"
        print
        for lib in ['tw1', 'tw2']:
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
    
    print "tests with the ``hotshot`` module"
    print "---------------------------------"
    print

    for test in map(str, range(1, num_tests+1)):
        func = "test%s" % test
        print func
        print "~~~~~"
        print

        for lib in ['tw1', 'tw2']:
            print func + " with " + lib + " -",
            print getattr(widgets, func).__doc__ + "::"
            print
            fname = "%s_%s.prof" % (func, lib)
            prof = hotshot.Profile(fname)
            prof.runcall(getattr(widgets, func), lib)
            prof.close()
            stats = hotshot.stats.load(fname)
            stats.strip_dirs()
            stats.sort_stats('time', 'calls')
            stats.print_stats(5)

        print
