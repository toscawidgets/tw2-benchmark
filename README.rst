tw2-benchmark
=============
Comparing toscawidgets1 with tw2 for speed

(generated: 2011-04-21)

tests with the ``timeit`` module
--------------------------------

test1 - Handling many WSGI requests ::

   test1('tw1')   min: 0.4894   max: 0.5387   avg: 0.5103
   test1('tw2')   min: 0.6928   max: 0.7148   avg: 0.6986

test2 - Handling de-duplication of resources ::

   test2('tw1')   min: 0.4845   max: 0.5603   avg: 0.4973
   test2('tw2')   min: 19.2053   max: 26.4516   avg: 21.6204

test3 - Setting up an app ::

   test3('tw1')   min: 0.0009   max: 0.0010   avg: 0.0009
   test3('tw2')   min: 0.0041   max: 0.0045   avg: 0.0042

test4 - Setting up an app. Displaying once. ::

   test4('tw1')   min: 0.0050   max: 0.0076   avg: 0.0054
   test4('tw2')   min: 0.0099   max: 0.0105   avg: 0.0100

test5 - Instantiating widgets many times (and displaying them) ::

   test5('tw1')   min: 0.4202   max: 0.4285   avg: 0.4245
   test5('tw2')   min: 0.5901   max: 0.5948   avg: 0.5922

test6 - Specifying parameters once, then displaying many times. ::

   test6('tw1')   min: 0.2149   max: 0.2197   avg: 0.2172
   test6('tw2')   min: 0.1400   max: 0.1443   avg: 0.1418

test7 - Specifying parameters *and* displaying many times. ::

   test7('tw1')   min: 0.3648   max: 0.3702   avg: 0.3668
   test7('tw2')   min: 0.3413   max: 0.3500   avg: 0.3445

tests with the ``hotshot`` module
---------------------------------

test1
~~~~~

test1 with tw1 -  Handling many WSGI requests ::

         22232 function calls (21610 primitive calls) in 0.073 CPU seconds

   Ordered by: internal time, call count
   List reduced from 241 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.015    0.000 base.py:249(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.002    0.000    0.006    0.000 util.py:138(wrapper)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)


test1 with tw2 -  Handling many WSGI requests ::

         14256 function calls (13856 primitive calls) in 0.088 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  201/101    0.023    0.000    0.042    0.000 widgets.py:92(post_define)
      201    0.011    0.000    0.016    0.000 params.py:135(__new__)
  201/101    0.005    0.000    0.050    0.000 widgets.py:31(__new__)
      602    0.003    0.000    0.003    0.000 functools.py:17(update_wrapper)
     2812    0.002    0.000    0.002    0.000 params.py:171(<genexpr>)



test2
~~~~~

test2 with tw1 -  Handling de-duplication of resources ::

         22232 function calls (21610 primitive calls) in 0.073 CPU seconds

   Ordered by: internal time, call count
   List reduced from 241 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.016    0.000 base.py:249(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.002    0.000    0.006    0.000 util.py:138(wrapper)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)


test2 with tw2 -  Handling de-duplication of resources ::

         220056 function calls (204956 primitive calls) in 1.628 CPU seconds

   Ordered by: internal time, call count
   List reduced from 117 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 5101/101    0.609    0.000    1.419    0.014 widgets.py:92(post_define)
     5101    0.317    0.000    0.492    0.000 params.py:135(__new__)
 5101/101    0.123    0.000    1.427    0.014 widgets.py:31(__new__)
     5002    0.070    0.000    0.124    0.000 copy.py:65(copy)
    10402    0.069    0.000    0.069    0.000 functools.py:17(update_wrapper)



test3
~~~~~

test3 with tw1 -  Setting up an app ::

         35 function calls in 0.000 CPU seconds

   Ordered by: internal time, call count
   List reduced from 25 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 meta.py:12(__new__)
        1    0.000    0.000    0.000    0.000 middleware.py:100(make_middleware)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:468(iter_entry_points)
        1    0.000    0.000    0.000    0.000 widgets.py:64(make_tw1_wsgi_app)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1952(load)


test3 with tw2 -  Setting up an app ::

         155 function calls in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 45 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 widgets.py:92(post_define)
       15    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)
        1    0.000    0.000    0.000    0.000 params.py:135(__new__)
        6    0.000    0.000    0.000    0.000 pkg_resources.py:468(iter_entry_points)



test4
~~~~~

test4 with tw1 -  Setting up an app. Displaying once. ::

         201 function calls (197 primitive calls) in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 99 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       23    0.000    0.000    0.000    0.000 base.py:44(__setattr__)
        2    0.000    0.000    0.000    0.000 meta.py:12(__new__)
        1    0.000    0.000    0.000    0.000 base.py:249(__new__)
       22    0.000    0.000    0.000    0.000 base.py:728(__setattr__)
        1    0.000    0.000    0.000    0.000 base.py:560(prepare_dict)


test4 with tw2 -  Setting up an app. Displaying once. ::

         257 function calls (256 primitive calls) in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 85 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.000    0.000    0.000    0.000 widgets.py:92(post_define)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)
        3    0.000    0.000    0.001    0.000 widgets.py:31(__new__)
        4    0.000    0.000    0.000    0.000 copy.py:65(copy)



test5
~~~~~

test5 with tw1 -  Instantiating widgets many times (and displaying them) ::

         16601 function calls (16201 primitive calls) in 0.059 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.016    0.000 base.py:249(__new__)
      100    0.003    0.000    0.004    0.000 meta.py:12(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.003    0.000    0.007    0.000 util.py:138(wrapper)


test5 with tw2 -  Instantiating widgets many times (and displaying them) ::

         10201 function calls (10101 primitive calls) in 0.095 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.022    0.000    0.038    0.000 template.py:77(render)
      200    0.022    0.000    0.027    0.000 widgets.py:92(post_define)
      200    0.010    0.000    0.016    0.000 params.py:135(__new__)
      200    0.005    0.000    0.048    0.000 widgets.py:31(__new__)
      100    0.003    0.000    0.009    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)



test6
~~~~~

test6 with tw1 -  Specifying parameters once, then displaying many times. ::

         9079 function calls (8679 primitive calls) in 0.031 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1000/600    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      100    0.001    0.000    0.008    0.000 runtime.py:642(_render)
      200    0.001    0.000    0.002    0.000 util.py:352(__get__)
     1000    0.001    0.000    0.001    0.000 registry.py:177(_current_obj)


test6 with tw2 -  Specifying parameters once, then displaying many times. ::

         4462 function calls (4362 primitive calls) in 0.020 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.014    0.000 template.py:77(render)
      100    0.001    0.000    0.006    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
  200/100    0.001    0.000    0.018    0.000 widgets.py:235(display)
      204    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)
      100    0.001    0.000    0.001    0.000 mako_util.py:14(attrs)



test7
~~~~~

test7 with tw1 -  Specifying parameters *and* displaying many times. ::

         15908 function calls (15508 primitive calls) in 0.056 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.011    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.016    0.000 base.py:249(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.002    0.000    0.007    0.000 util.py:138(wrapper)
      100    0.002    0.000    0.007    0.000 base.py:560(prepare_dict)


test7 with tw2 -  Specifying parameters *and* displaying many times. ::

         6934 function calls (6834 primitive calls) in 0.043 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.011    0.000    0.014    0.000 widgets.py:92(post_define)
      101    0.005    0.000    0.006    0.000 params.py:135(__new__)
      101    0.002    0.000    0.022    0.000 widgets.py:31(__new__)
      402    0.002    0.000    0.002    0.000 functools.py:17(update_wrapper)
      100    0.002    0.000    0.016    0.000 template.py:77(render)



