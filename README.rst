tw2-benchmark
=============
Comparing toscawidgets1 with tw2 for speed (generated: 2011-04-21)

``timeit`` summary
------------------

- tw2 wins at

  - test7 - Specifying parameters *and* displaying many times. 

  - test6 - Specifying parameters once, then displaying many times. 


- tw1 wins at

  - test1 - Handling many WSGI requests 

  - test3 - Setting up an app 

  - test2 - Handling de-duplication of resources 

  - test5 - Instantiating widgets many times (and displaying them) 

  - test4 - Setting up an app. Displaying once. 


tests with the ``timeit`` module
--------------------------------

test1 - Handling many WSGI requests ::

   test7('tw2')   min: 0.5036   max: 0.5226   avg: 0.5099
   test7('tw2')   min: 0.7098   max: 0.7204   avg: 0.7152

test2 - Handling de-duplication of resources ::

   test7('tw2')   min: 0.4857   max: 0.5118   avg: 0.4984
   test7('tw2')   min: 19.0675   max: 26.2260   avg: 21.4485

test3 - Setting up an app ::

   test7('tw2')   min: 0.0009   max: 0.0011   avg: 0.0010
   test7('tw2')   min: 0.0041   max: 0.0042   avg: 0.0041

test4 - Setting up an app. Displaying once. ::

   test7('tw2')   min: 0.0050   max: 0.0075   avg: 0.0054
   test7('tw2')   min: 0.0098   max: 0.0105   avg: 0.0100

test5 - Instantiating widgets many times (and displaying them) ::

   test7('tw2')   min: 0.4220   max: 0.4354   avg: 0.4254
   test7('tw2')   min: 0.5866   max: 0.5979   avg: 0.5905

test6 - Specifying parameters once, then displaying many times. ::

   test7('tw2')   min: 0.2145   max: 0.2170   avg: 0.2156
   test7('tw2')   min: 0.1418   max: 0.1432   avg: 0.1425

test7 - Specifying parameters *and* displaying many times. ::

   test7('tw2')   min: 0.3647   max: 0.3687   avg: 0.3666
   test7('tw2')   min: 0.3408   max: 0.3470   avg: 0.3432

tests with the ``hotshot`` module
---------------------------------

test1
~~~~~

test1 with tw1 -  Handling many WSGI requests ::

         22232 function calls (21610 primitive calls) in 0.072 CPU seconds

   Ordered by: internal time, call count
   List reduced from 241 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.015    0.000 base.py:249(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.002    0.000    0.006    0.000 util.py:138(wrapper)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)


test1 with tw2 -  Handling many WSGI requests ::

         14256 function calls (13856 primitive calls) in 0.087 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  201/101    0.023    0.000    0.041    0.000 widgets.py:92(post_define)
      201    0.011    0.000    0.015    0.000 params.py:135(__new__)
  201/101    0.005    0.000    0.049    0.000 widgets.py:31(__new__)
      602    0.003    0.000    0.003    0.000 functools.py:17(update_wrapper)
  200/100    0.002    0.000    0.026    0.000 widgets.py:235(display)



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

         220056 function calls (204956 primitive calls) in 1.607 CPU seconds

   Ordered by: internal time, call count
   List reduced from 117 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 5101/101    0.599    0.000    1.401    0.014 widgets.py:92(post_define)
     5101    0.314    0.000    0.488    0.000 params.py:135(__new__)
 5101/101    0.121    0.000    1.409    0.014 widgets.py:31(__new__)
     5002    0.069    0.000    0.122    0.000 copy.py:65(copy)
    10402    0.068    0.000    0.068    0.000 functools.py:17(update_wrapper)



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
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1952(load)
        2    0.000    0.000    0.000    0.000 meta.py:52(frozenset_from_all_bases)


test3 with tw2 -  Setting up an app ::

         155 function calls in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 45 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 widgets.py:92(post_define)
        6    0.000    0.000    0.000    0.000 pkg_resources.py:468(iter_entry_points)
        1    0.000    0.000    0.000    0.000 params.py:135(__new__)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)
        1    0.000    0.000    0.000    0.000 widgets.py:31(__new__)



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
        1    0.000    0.000    0.000    0.000 base.py:560(prepare_dict)
        1    0.000    0.000    0.000    0.000 util.py:138(wrapper)


test4 with tw2 -  Setting up an app. Displaying once. ::

         257 function calls (256 primitive calls) in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 85 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.000    0.000    0.000    0.000 widgets.py:92(post_define)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)
        3    0.000    0.000    0.001    0.000 widgets.py:31(__new__)
        4    0.000    0.000    0.000    0.000 copy.py:65(copy)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)



test5
~~~~~

test5 with tw1 -  Instantiating widgets many times (and displaying them) ::

         16601 function calls (16201 primitive calls) in 0.060 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.016    0.000 base.py:249(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.003    0.000    0.004    0.000 meta.py:12(__new__)
      100    0.003    0.000    0.007    0.000 util.py:138(wrapper)


test5 with tw2 -  Instantiating widgets many times (and displaying them) ::

         10201 function calls (10101 primitive calls) in 0.094 CPU seconds

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
      200    0.001    0.000    0.002    0.000 util.py:352(__get__)
      100    0.001    0.000    0.008    0.000 runtime.py:642(_render)
      100    0.001    0.000    0.018    0.000 view.py:26(_renderer)


test6 with tw2 -  Specifying parameters once, then displaying many times. ::

         4462 function calls (4362 primitive calls) in 0.021 CPU seconds

   Ordered by: internal time, call count
   List reduced from 58 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.002    0.000    0.015    0.000 template.py:77(render)
      100    0.001    0.000    0.007    0.000 _home_rjbpop_devel_tw2_benchmark_tw2benchmark_templates_tw2_mak:25(render_body)
  200/100    0.001    0.000    0.019    0.000 widgets.py:235(display)
      204    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)
      100    0.001    0.000    0.001    0.000 mako_util.py:14(attrs)



test7
~~~~~

test7 with tw1 -  Specifying parameters *and* displaying many times. ::

         15908 function calls (15508 primitive calls) in 0.054 CPU seconds

   Ordered by: internal time, call count
   List reduced from 81 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.004    0.000    0.016    0.000 base.py:249(__new__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)
      100    0.002    0.000    0.006    0.000 util.py:138(wrapper)
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



