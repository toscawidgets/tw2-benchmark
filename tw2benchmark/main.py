#!/usr/bin/env python

def do_plot(results, libs, tests):
    try:
        import tw2benchmark.CairoPlot as cp
    except ImportError as e:
        print ".. comment: !!", str(e)
        print ".. comment: !! CairoPlot is not installed.  Skipping plots."
        return []

    data, labels = [], []
    for test in tests:
        func = "test%s" % test
        values = results[func]
        labels.append(func)
        data.append( [values[lib]['min'] for lib in libs])

    maxes = [max(entry) for entry in data]

    # Normalize between zero and one
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = data[i][j] / float(maxes[i])

    width, height = 512, 128
    fname = 'tw2-benchmark/raw/master/summary.png'
    cp.bar_plot(
        'summary.png',
        data,
        width,
        height,
        background = None,
        border = 0,
        grid = False,
        h_labels = labels,
        v_labels = None,
        h_bounds = None,
        v_bounds = None,
        rounded_corners = True,
        colors = [
            [0/256.0, 101/256.0, 133/256.0],
            [180/256.0, 162/256.0, 0/256.0],
            [71/256.0, 43/256.0, 26/256.0],
        ],
    )

    return [
        [fname,
         "Normalized score results.  " +
         "(tw1: blue, tw2: yellow, ew: brown)"]
    ]


if __name__ == '__main__':
    import datetime
    from timeit import Timer
    import hotshot, hotshot.stats

    import widgets

    widget_libs = ['tw1', 'tw2', 'ew']
    num_tests = 7
    test_range = map(str, range(1, num_tests+1))
    passes = 10

    print "tw2-benchmark"
    print "============="
    print "Comparing toscawidgets1, tw2, and EasyWidgets for speed",
    print "(generated: %s)" % datetime.datetime.now().strftime("%F")
    print

    from widgets import test_wsgi_app_works
    test_wsgi_app_works()

    results = {}
    for test in test_range:
        func = "test%s" % test
        results[func] = {}
        for lib in widget_libs:
            statement = "%s('%s')" % (func, lib)
            print ".. comment: (running %s)" % statement
            timer = Timer(
                stmt=statement,
                setup="from widgets import %s" % func,
            )
            t = timer.repeat(passes, 10)
            _min, _max, _avg = min(t), max(t), sum(t)/len(t)
            results[func][lib] = { 'min': _min, 'max': _max, 'avg' : _avg }

    print ".. comment: producing graphs"
    charts = do_plot(results, widget_libs, test_range)

    for fname, title in charts:
        print
        print ".. figure::", fname
        print "   :scale: 300 %"
        print
        print "   %s" % title


    print "``timeit`` summary"
    print "------------------"
    print

    for lib in widget_libs:
        print '-', lib, "wins at"
        print
        for func in results.keys():
            if all([results[func][lib]['min'] < results[func][other]['min']
                    for other in widget_libs if lib != other]):
                print '  -', func + " -" + getattr(widgets, func).__doc__
                print


    print "tests with the ``timeit`` module"
    print "--------------------------------"
    print

    for test in test_range:
        func = "test%s" % test
        print func + " -" + getattr(widgets, func).__doc__ + "::"
        print
        for lib in widget_libs:
            statement = "%s('%s')" % (func, lib)
            print "  ", statement,
            print "  min: %.4f" % (passes * results[func][lib]['min']/passes),
            print "  max: %.4f" % (passes * results[func][lib]['max']/passes),
            print "  avg: %.4f" % (passes * results[func][lib]['avg']/passes)

        print

    print "tests with the ``hotshot`` module"
    print "---------------------------------"
    print

    for test in test_range:
        func = "test%s" % test
        print func
        print "~~~~~"
        print

        for lib in widget_libs:
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
