tw2-benchmark
=============
Comparing toscawidgets1 with tw2 for speed (generated: 2011-04-21)

``timeit`` summary
------------------

- tw2 wins at

  - test1 - Handling many WSGI requests 

  - test7 - Specifying parameters *and* displaying many times. 

  - test6 - Specifying parameters once, then displaying many times. 

  - test9 - Minimizing tw2 subclasses with params in display 

  - test8 - Minimizing tw2 subclasses with params before display


- tw1 wins at

  - test3 - Setting up an app 

  - test2 - Handling many (duplicate) resources 

  - test5 - Instantiating widgets many times (and displaying them) 

  - test4 - Setting up an app. Displaying once. 


tests with the ``timeit`` module
--------------------------------

test1 - Handling many WSGI requests ::

   test1('tw1')   min: 0.3358   max: 0.3491   avg: 0.3402
   test1('tw2')   min: 0.2534   max: 0.2575   avg: 0.2553

test2 - Handling many (duplicate) resources ::

   test2('tw1')   min: 0.3339   max: 0.3395   avg: 0.3366
   test2('tw2')   min: 1.3035   max: 1.3437   avg: 1.3155

test3 - Setting up an app ::

   test3('tw1')   min: 0.0024   max: 0.0027   avg: 0.0025
   test3('tw2')   min: 0.0082   max: 0.0085   avg: 0.0083

test4 - Setting up an app. Displaying once. ::

   test4('tw1')   min: 0.0065   max: 0.0090   avg: 0.0068
   test4('tw2')   min: 0.0140   max: 0.0154   avg: 0.0144

test5 - Instantiating widgets many times (and displaying them) ::

   test5('tw1')   min: 0.4172   max: 0.4290   avg: 0.4219
   test5('tw2')   min: 0.5872   max: 0.6223   avg: 0.6022

test6 - Specifying parameters once, then displaying many times. ::

   test6('tw1')   min: 0.2176   max: 0.2385   avg: 0.2288
   test6('tw2')   min: 0.1460   max: 0.1528   avg: 0.1497

test7 - Specifying parameters *and* displaying many times. ::

   test7('tw1')   min: 0.3773   max: 0.3942   avg: 0.3863
   test7('tw2')   min: 0.3501   max: 0.3697   avg: 0.3597

test8 - Minimizing tw2 subclasses with params before display::

   test8('tw1')   min: 0.2183   max: 0.2323   avg: 0.2261
   test8('tw2')   min: 0.1403   max: 0.1515   avg: 0.1438

test9 - Minimizing tw2 subclasses with params in display ::

   test9('tw1')   min: 0.2197   max: 0.2279   avg: 0.2245
   test9('tw2')   min: 0.1428   max: 0.1507   avg: 0.1473

tests with the ``hotshot`` module
---------------------------------

test1
~~~~~

test1 with tw1 -  Handling many WSGI requests ::

         15401 function calls (14779 primitive calls) in 0.053 CPU seconds

   Ordered by: internal time, call count
   List reduced from 241 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.007    0.000 base.py:560(prepare_dict)
 1000/600    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      100    0.001    0.000    0.049    0.000 middleware.py:45(wsgi_app)
      100    0.001    0.000    0.009    0.000 runtime.py:642(_render)
      200    0.001    0.000    0.002    0.000 util.py:352(__get__)


test1 with tw2 -  Handling many WSGI requests ::

         8513 function calls (8410 primitive calls) in 0.037 CPU seconds

   Ordered by: internal time, call count
   List reduced from 115 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  200/100    0.002    0.000    0.025    0.000 widgets.py:235(display)
      100    0.002    0.000    0.033    0.000 middleware.py:136(__call__)
      100    0.001    0.000    0.007    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
      100    0.001    0.000    0.017    0.000 template.py:77(render)
      206    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)



test2
~~~~~

test2 with tw1 -  Handling many (duplicate) resources ::

         15401 function calls (14779 primitive calls) in 0.052 CPU seconds

   Ordered by: internal time, call count
   List reduced from 241 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.007    0.000 base.py:560(prepare_dict)
      100    0.002    0.000    0.003    0.000 _tw2benchmark_templates_tw1_mak:14(render_body)
 1000/600    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      100    0.001    0.000    0.049    0.000 middleware.py:45(wsgi_app)
      100    0.001    0.000    0.009    0.000 runtime.py:642(_render)


test2 with tw2 -  Handling many (duplicate) resources ::

         54230 function calls (53980 primitive calls) in 0.196 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5000    0.031    0.000    0.120    0.000 resources.py:79(prepare)
     5100    0.030    0.000    0.030    0.000 widgets.py:181(prepare)
     5000    0.021    0.000    0.066    0.000 resources.py:63(prepare)
     5000    0.019    0.000    0.019    0.000 resources.py:184(register)
  200/100    0.013    0.000    0.170    0.002 widgets.py:235(display)



test3
~~~~~

test3 with tw1 -  Setting up an app ::

         104 function calls in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 43 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       23    0.000    0.000    0.000    0.000 base.py:44(__setattr__)
        1    0.000    0.000    0.000    0.000 base.py:249(__new__)
        1    0.000    0.000    0.000    0.000 meta.py:12(__new__)
       22    0.000    0.000    0.000    0.000 base.py:728(__setattr__)
        1    0.000    0.000    0.000    0.000 util.py:138(wrapper)


test3 with tw2 -  Setting up an app ::

         213 function calls (210 primitive calls) in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 47 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/2    0.000    0.000    0.001    0.000 widgets.py:92(post_define)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)
      3/2    0.000    0.000    0.001    0.000 widgets.py:31(__new__)
        3    0.000    0.000    0.000    0.000 copy.py:65(copy)



test4
~~~~~

test4 with tw1 -  Setting up an app. Displaying once. ::

         270 function calls (266 primitive calls) in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 99 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       46    0.000    0.000    0.000    0.000 base.py:44(__setattr__)
        2    0.000    0.000    0.000    0.000 base.py:249(__new__)
        2    0.000    0.000    0.000    0.000 meta.py:12(__new__)
       44    0.000    0.000    0.000    0.000 base.py:728(__setattr__)
        2    0.000    0.000    0.000    0.000 util.py:138(wrapper)


test4 with tw2 -  Setting up an app. Displaying once. ::

         315 function calls (311 primitive calls) in 0.002 CPU seconds

   Ordered by: internal time, call count
   List reduced from 85 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      5/4    0.001    0.000    0.001    0.000 widgets.py:92(post_define)
        5    0.000    0.000    0.000    0.000 params.py:135(__new__)
      5/4    0.000    0.000    0.001    0.000 widgets.py:31(__new__)
       12    0.000    0.000    0.000    0.000 functools.py:17(update_wrapper)
        5    0.000    0.000    0.000    0.000 copy.py:65(copy)



test5
~~~~~

test5 with tw1 -  Instantiating widgets many times (and displaying them) ::

         16601 function calls (16201 primitive calls) in 0.060 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.011    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.016    0.000 base.py:249(__new__)
      100    0.003    0.000    0.004    0.000 meta.py:12(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.003    0.000    0.007    0.000 util.py:138(wrapper)


test5 with tw2 -  Instantiating widgets many times (and displaying them) ::

         10201 function calls (10101 primitive calls) in 0.075 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      200    0.022    0.000    0.028    0.000 widgets.py:92(post_define)
      200    0.010    0.000    0.016    0.000 params.py:135(__new__)
      200    0.005    0.000    0.049    0.000 widgets.py:31(__new__)
      600    0.003    0.000    0.003    0.000 functools.py:17(update_wrapper)
      200    0.002    0.000    0.004    0.000 copy.py:65(copy)



test6
~~~~~

test6 with tw1 -  Specifying parameters once, then displaying many times. ::

         9079 function calls (8679 primitive calls) in 0.032 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1000/600    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      200    0.001    0.000    0.002    0.000 util.py:352(__get__)
      100    0.001    0.000    0.008    0.000 runtime.py:642(_render)
     1000    0.001    0.000    0.001    0.000 registry.py:177(_current_obj)


test6 with tw2 -  Specifying parameters once, then displaying many times. ::

         4462 function calls (4362 primitive calls) in 0.020 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.015    0.000 template.py:77(render)
      100    0.001    0.000    0.007    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
  200/100    0.001    0.000    0.019    0.000 widgets.py:235(display)
      100    0.001    0.000    0.002    0.000 mako_util.py:14(attrs)
      204    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)



test7
~~~~~

test7 with tw1 -  Specifying parameters *and* displaying many times. ::

         15909 function calls (15509 primitive calls) in 0.069 CPU seconds

   Ordered by: internal time, call count
   List reduced from 82 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.014    0.000    0.016    0.000 widgets.py:35(update_params)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.016    0.000 base.py:249(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.003    0.000    0.021    0.000 base.py:560(prepare_dict)


test7 with tw2 -  Specifying parameters *and* displaying many times. ::

         6934 function calls (6834 primitive calls) in 0.043 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.011    0.000    0.014    0.000 widgets.py:92(post_define)
      101    0.005    0.000    0.006    0.000 params.py:135(__new__)
      101    0.002    0.000    0.023    0.000 widgets.py:31(__new__)
      402    0.002    0.000    0.002    0.000 functools.py:17(update_wrapper)
      100    0.001    0.000    0.006    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)



test8
~~~~~

test8 with tw1 -  Minimizing tw2 subclasses with params before display::

         9077 function calls (8677 primitive calls) in 0.033 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.007    0.000 base.py:560(prepare_dict)
 1000/600    0.002    0.000    0.005    0.000 registry.py:136(__getattr__)
      100    0.001    0.000    0.008    0.000 runtime.py:642(_render)
      200    0.001    0.000    0.003    0.000 util.py:352(__get__)
      100    0.001    0.000    0.002    0.000 base.py:474(retrieve_resources)


test8 with tw2 -  Minimizing tw2 subclasses with params before display::

         4462 function calls (4362 primitive calls) in 0.020 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.006    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
      100    0.002    0.000    0.015    0.000 template.py:77(render)
  200/100    0.001    0.000    0.018    0.000 widgets.py:235(display)
      204    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)
      100    0.001    0.000    0.001    0.000 mako_util.py:14(attrs)



test9
~~~~~

test9 with tw1 -  Minimizing tw2 subclasses with params in display ::

         9077 function calls (8677 primitive calls) in 0.033 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.007    0.000 base.py:560(prepare_dict)
 1000/600    0.002    0.000    0.004    0.000 registry.py:136(__getattr__)
      100    0.001    0.000    0.008    0.000 runtime.py:642(_render)
      200    0.001    0.000    0.002    0.000 util.py:352(__get__)
      100    0.001    0.000    0.018    0.000 view.py:26(_renderer)


test9 with tw2 -  Minimizing tw2 subclasses with params in display ::

         4434 function calls (4334 primitive calls) in 0.020 CPU seconds

   Ordered by: internal time, call count
   List reduced from 56 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.015    0.000 template.py:77(render)
      100    0.001    0.000    0.007    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
  200/100    0.001    0.000    0.019    0.000 widgets.py:235(display)
      202    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)
      100    0.001    0.000    0.012    0.000 runtime.py:642(_render)



