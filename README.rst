tw2-benchmark
=============
Comparing toscawidgets1 with tw2 for speed (generated: 2011-04-22)

.. comment: Testing tw1 output against tw1
.. comment: Testing tw1 output against tw2
.. comment: Testing tw1 output against ew
.. comment: Testing tw2 output against tw1
.. comment: Testing tw2 output against tw2
.. comment: Testing tw2 output against ew
.. comment: Testing ew output against tw1
.. comment: Testing ew output against tw2
.. comment: Testing ew output against ew
.. comment: (running test1('ew'))
.. comment: (running test1('tw1'))
.. comment: (running test1('tw2'))
.. comment: (running test2('ew'))
.. comment: (running test2('tw1'))
.. comment: (running test2('tw2'))
.. comment: (running test3('ew'))
.. comment: (running test3('tw1'))
.. comment: (running test3('tw2'))
.. comment: (running test4('ew'))
.. comment: (running test4('tw1'))
.. comment: (running test4('tw2'))
.. comment: (running test5('ew'))
.. comment: (running test5('tw1'))
.. comment: (running test5('tw2'))
.. comment: (running test6('ew'))
.. comment: (running test6('tw1'))
.. comment: (running test6('tw2'))
.. comment: (running test7('ew'))
.. comment: (running test7('tw1'))
.. comment: (running test7('tw2'))
``timeit`` summary
------------------

- ew wins at

  - test1 - Handling many WSGI requests 

  - test5 - Instantiating widgets many times (and displaying them) 

  - test7 - Specifying parameters *and* displaying many times. 

  - test6 - Specifying parameters once, then displaying many times. 

- tw1 wins at

  - test3 - Setting up an app 

  - test2 - Handling many (duplicate) resources 

- tw2 wins at

  - test4 - Setting up an app. Displaying once. 

tests with the ``timeit`` module
--------------------------------

test1 - Handling many WSGI requests ::

   test1('ew')   min: 0.1710   max: 0.1787   avg: 0.1737
   test1('tw1')   min: 0.3249   max: 0.3388   avg: 0.3300
   test1('tw2')   min: 0.2519   max: 0.2676   avg: 0.2568

test2 - Handling many (duplicate) resources ::

   test2('ew')   min: 0.0384   max: 0.0402   avg: 0.0389
   test2('tw1')   min: 0.0262   max: 0.0268   avg: 0.0265
   test2('tw2')   min: 0.1348   max: 0.1419   avg: 0.1379

test3 - Setting up an app ::

   test3('ew')   min: 0.0368   max: 0.0394   avg: 0.0377
   test3('tw1')   min: 0.0027   max: 0.0028   avg: 0.0027
   test3('tw2')   min: 0.0084   max: 0.0087   avg: 0.0084

test4 - Setting up an app. Displaying once. ::

   test4('ew')   min: 0.0386   max: 0.0399   avg: 0.0389
   test4('tw1')   min: 0.0263   max: 0.0269   avg: 0.0264
   test4('tw2')   min: 0.0111   max: 0.0115   avg: 0.0112

test5 - Instantiating widgets many times (and displaying them) ::

   test5('ew')   min: 0.2049   max: 0.2138   avg: 0.2079
   test5('tw1')   min: 0.4552   max: 0.4633   avg: 0.4585
   test5('tw2')   min: 0.8694   max: 0.8902   avg: 0.8766

test6 - Specifying parameters once, then displaying many times. ::

   test6('ew')   min: 0.1499   max: 0.1743   avg: 0.1590
   test6('tw1')   min: 0.2299   max: 0.2415   avg: 0.2344
   test6('tw2')   min: 0.1931   max: 0.1958   avg: 0.1943

test7 - Specifying parameters *and* displaying many times. ::

   test7('ew')   min: 0.1384   max: 0.1440   avg: 0.1400
   test7('tw1')   min: 0.2303   max: 0.2360   avg: 0.2325
   test7('tw2')   min: 0.1917   max: 0.2002   avg: 0.1951

tests with the ``hotshot`` module
---------------------------------

test1
~~~~~

test1 with ew -  Handling many WSGI requests ::

         6660 function calls in 0.024 CPU seconds

   Ordered by: internal time, call count
   List reduced from 90 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      200    0.004    0.000    0.004    0.000 render.py:141(__getitem__)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
      100    0.001    0.000    0.006    0.000 string.py:174(safe_substitute)
      100    0.001    0.000    0.014    0.000 widget.py:37(display)
      200    0.001    0.000    0.003    0.000 utils.py:24(push_context)


test1 with tw1 -  Handling many WSGI requests ::

         15429 function calls (14807 primitive calls) in 0.049 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1000/600    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      200    0.001    0.000    0.002    0.000 util.py:352(__get__)
      100    0.001    0.000    0.046    0.000 middleware.py:45(wsgi_app)
      200    0.001    0.000    0.002    0.000 response.py:36(__init__)


test1 with tw2 -  Handling many WSGI requests ::

         8634 function calls (8531 primitive calls) in 0.035 CPU seconds

   Ordered by: internal time, call count
   List reduced from 119 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.017    0.000 template.py:77(render)
  200/100    0.002    0.000    0.024    0.000 widgets.py:235(display)
      100    0.002    0.000    0.032    0.000 middleware.py:136(__call__)
      100    0.001    0.000    0.006    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
      200    0.001    0.000    0.001    0.000 widgets.py:181(prepare)



test2
~~~~~

test2 with ew -  Handling many (duplicate) resources ::

         1908 function calls in 0.006 CPU seconds

   Ordered by: internal time, call count
   List reduced from 90 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
       45    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)
     1170    0.001    0.000    0.001    0.000 pkg_resources.py:1831(_normalize_cached)
        9    0.000    0.000    0.001    0.000 pkg_resources.py:534(resolve)
        1    0.000    0.000    0.000    0.000 render.py:175(__init__)


test2 with tw1 -  Handling many (duplicate) resources ::

         1074 function calls (1046 primitive calls) in 0.004 CPU seconds

   Ordered by: internal time, call count
   List reduced from 247 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 template.py:471(_compile_text)
       44    0.000    0.000    0.000    0.000 lexer.py:64(match_reg)
      141    0.000    0.000    0.000    0.000 re.py:229(_compile)
       29    0.000    0.000    0.001    0.000 pygen.py:55(writeline)
       30    0.000    0.000    0.000    0.000 posixpath.py:308(normpath)


test2 with tw2 -  Handling many (duplicate) resources ::

         2375 function calls (2224 primitive calls) in 0.016 CPU seconds

   Ordered by: internal time, call count
   List reduced from 119 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     52/2    0.006    0.000    0.013    0.007 widgets.py:92(post_define)
       52    0.003    0.000    0.005    0.000 params.py:135(__new__)
     52/2    0.001    0.000    0.014    0.007 widgets.py:31(__new__)
       52    0.001    0.000    0.001    0.000 copy.py:65(copy)
      824    0.001    0.000    0.001    0.000 params.py:171(<genexpr>)



test3
~~~~~

test3 with ew -  Setting up an app ::

         1853 function calls in 0.005 CPU seconds

   Ordered by: internal time, call count
   List reduced from 50 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.001    0.000    0.001    0.000 render.py:257(__init__)
       45    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)
     1170    0.001    0.000    0.001    0.000 pkg_resources.py:1831(_normalize_cached)
        9    0.000    0.000    0.001    0.000 pkg_resources.py:534(resolve)
        1    0.000    0.000    0.000    0.000 render.py:175(__init__)


test3 with tw1 -  Setting up an app ::

         114 function calls in 0.000 CPU seconds

   Ordered by: internal time, call count
   List reduced from 49 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       23    0.000    0.000    0.000    0.000 base.py:44(__setattr__)
        1    0.000    0.000    0.000    0.000 base.py:249(__new__)
        1    0.000    0.000    0.000    0.000 meta.py:12(__new__)
       22    0.000    0.000    0.000    0.000 base.py:728(__setattr__)
        1    0.000    0.000    0.000    0.000 util.py:138(wrapper)


test3 with tw2 -  Setting up an app ::

         233 function calls (230 primitive calls) in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 49 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/2    0.000    0.000    0.001    0.000 widgets.py:92(post_define)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)
      3/2    0.000    0.000    0.001    0.000 widgets.py:31(__new__)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)
        3    0.000    0.000    0.000    0.000 copy.py:65(copy)



test4
~~~~~

test4 with ew -  Setting up an app. Displaying once. ::

         1908 function calls in 0.006 CPU seconds

   Ordered by: internal time, call count
   List reduced from 90 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.001    0.000    0.001    0.000 render.py:257(__init__)
       45    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)
     1170    0.001    0.000    0.001    0.000 pkg_resources.py:1831(_normalize_cached)
        9    0.000    0.000    0.001    0.000 pkg_resources.py:534(resolve)
        1    0.000    0.000    0.000    0.000 render.py:175(__init__)


test4 with tw1 -  Setting up an app. Displaying once. ::

         1074 function calls (1046 primitive calls) in 0.004 CPU seconds

   Ordered by: internal time, call count
   List reduced from 247 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 template.py:471(_compile_text)
       44    0.000    0.000    0.000    0.000 lexer.py:64(match_reg)
      141    0.000    0.000    0.000    0.000 re.py:229(_compile)
       30    0.000    0.000    0.000    0.000 posixpath.py:308(normpath)
       29    0.000    0.000    0.001    0.000 pygen.py:55(writeline)


test4 with tw2 -  Setting up an app. Displaying once. ::

         317 function calls (313 primitive calls) in 0.002 CPU seconds

   Ordered by: internal time, call count
   List reduced from 118 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/2    0.000    0.000    0.001    0.000 widgets.py:92(post_define)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)
      3/2    0.000    0.000    0.001    0.000 widgets.py:31(__new__)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)
        3    0.000    0.000    0.000    0.000 copy.py:65(copy)



test5
~~~~~

test5 with ew -  Instantiating widgets many times (and displaying them) ::

         6991 function calls in 0.027 CPU seconds

   Ordered by: internal time, call count
   List reduced from 90 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      202    0.004    0.000    0.004    0.000 render.py:141(__getitem__)
      100    0.003    0.000    0.003    0.000 widgets.py:48(get_ew_widget)
      101    0.002    0.000    0.015    0.000 widget.py:37(display)
      101    0.001    0.000    0.006    0.000 string.py:174(safe_substitute)
        5    0.001    0.000    0.001    0.000 render.py:257(__init__)


test5 with tw1 -  Instantiating widgets many times (and displaying them) ::

         18191 function calls (17763 primitive calls) in 0.065 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.005    0.000    0.018    0.000 base.py:249(__new__)
      100    0.003    0.000    0.004    0.000 meta.py:12(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.002    0.000    0.006    0.000 util.py:138(wrapper)


test5 with tw2 -  Instantiating widgets many times (and displaying them) ::

         14925 function calls (14524 primitive calls) in 0.105 CPU seconds

   Ordered by: internal time, call count
   List reduced from 119 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  300/200    0.032    0.000    0.051    0.000 widgets.py:92(post_define)
      300    0.015    0.000    0.025    0.000 params.py:135(__new__)
  300/200    0.007    0.000    0.072    0.000 widgets.py:31(__new__)
      300    0.004    0.000    0.007    0.000 copy.py:65(copy)
      802    0.004    0.000    0.004    0.000 functools.py:17(update_wrapper)



test6
~~~~~

test6 with ew -  Specifying parameters once, then displaying many times. ::

         5308 function calls in 0.021 CPU seconds

   Ordered by: internal time, call count
   List reduced from 90 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      202    0.004    0.000    0.005    0.000 render.py:141(__getitem__)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
      101    0.001    0.000    0.007    0.000 string.py:174(safe_substitute)
      202    0.001    0.000    0.003    0.000 utils.py:24(push_context)
      101    0.001    0.000    0.015    0.000 widget.py:37(display)


test6 with tw1 -  Specifying parameters once, then displaying many times. ::

         9974 function calls (9546 primitive calls) in 0.035 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1010/606    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      202    0.001    0.000    0.002    0.000 util.py:352(__get__)
      101    0.001    0.000    0.008    0.000 runtime.py:642(_render)
      100    0.001    0.000    0.001    0.000 lookup.py:294(_check)


test6 with tw2 -  Specifying parameters once, then displaying many times. ::

         5882 function calls (5775 primitive calls) in 0.027 CPU seconds

   Ordered by: internal time, call count
   List reduced from 120 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.002    0.000    0.002    0.000 runtime.py:630(_populate_self_namespace)
  202/101    0.002    0.000    0.024    0.000 widgets.py:235(display)
      101    0.001    0.000    0.007    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
      101    0.001    0.000    0.017    0.000 template.py:77(render)
      212    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)



test7
~~~~~

test7 with ew -  Specifying parameters *and* displaying many times. ::

         5308 function calls in 0.019 CPU seconds

   Ordered by: internal time, call count
   List reduced from 90 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      202    0.003    0.000    0.003    0.000 render.py:141(__getitem__)
        5    0.001    0.000    0.001    0.000 render.py:257(__init__)
      101    0.001    0.000    0.006    0.000 string.py:174(safe_substitute)
      101    0.001    0.000    0.013    0.000 widget.py:37(display)
      202    0.001    0.000    0.003    0.000 utils.py:24(push_context)


test7 with tw1 -  Specifying parameters *and* displaying many times. ::

         9974 function calls (9546 primitive calls) in 0.034 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1010/606    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      202    0.001    0.000    0.002    0.000 util.py:352(__get__)
      101    0.001    0.000    0.008    0.000 runtime.py:642(_render)
      101    0.001    0.000    0.022    0.000 view.py:26(_renderer)


test7 with tw2 -  Specifying parameters *and* displaying many times. ::

         5817 function calls (5713 primitive calls) in 0.027 CPU seconds

   Ordered by: internal time, call count
   List reduced from 119 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  202/101    0.002    0.000    0.024    0.000 widgets.py:235(display)
      101    0.001    0.000    0.007    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
      101    0.001    0.000    0.017    0.000 template.py:77(render)
      202    0.001    0.000    0.001    0.000 widgets.py:181(prepare)
      208    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)



