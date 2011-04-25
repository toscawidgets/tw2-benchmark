tw2-benchmark
=============
Comparing toscawidgets1, tw2, and EasyWidgets for speed (generated: 2011-04-25)

Speed results for tw2 are contingent on two patches not yet
merged upstream:

 - https://bitbucket.org/ralphbean/tw2core/changeset/e8670e8e7315
 - https://bitbucket.org/ralphbean/tw2core/changeset/62f22632b61b

.. comment: (running test1('tw1'))
.. comment: (running test1('tw2'))
.. comment: (running test1('ew'))
.. comment: (running test2('tw1'))
.. comment: (running test2('tw2'))
.. comment: (running test2('ew'))
.. comment: (running test3('tw1'))
.. comment: (running test3('tw2'))
.. comment: (running test3('ew'))
.. comment: (running test4('tw1'))
.. comment: (running test4('tw2'))
.. comment: (running test4('ew'))
.. comment: (running test5('tw1'))
.. comment: (running test5('tw2'))
.. comment: (running test5('ew'))
.. comment: (running test6('tw1'))
.. comment: (running test6('tw2'))
.. comment: (running test6('ew'))
.. comment: (running test7('tw1'))
.. comment: (running test7('tw2'))
.. comment: (running test7('ew'))
.. comment: producing graphs

.. figure:: tw2-benchmark/raw/master/summary.png
   :scale: 300 %

   Normalized score results.  (tw1: blue, tw2: yellow, ew: brown)
``timeit`` summary
------------------

- tw1 wins at

  - test3 - Setting up an app 

  - test2 - Handling many (duplicate) resources 

- tw2 wins at

  - test1 - Handling many WSGI requests 

  - test4 - Setting up an app. Displaying once. 

  - test7 - Specifying parameters *and* displaying many times. 

  - test6 - Specifying parameters once, then displaying many times. 

- ew wins at

  - test5 - Instantiating widgets many times (and displaying them) 

tests with the ``timeit`` module
--------------------------------

test1 - Handling many WSGI requests ::

   test1('tw1')   min: 0.8081   max: 0.8353   avg: 0.8197
   test1('tw2')   min: 0.4642   max: 0.4748   avg: 0.4704
   test1('ew')   min: 0.5230   max: 0.5473   avg: 0.5302

test2 - Handling many (duplicate) resources ::

   test2('tw1')   min: 0.0750   max: 0.0770   avg: 0.0760
   test2('tw2')   min: 0.1924   max: 0.2014   avg: 0.1962
   test2('ew')   min: 0.1204   max: 0.1257   avg: 0.1223

test3 - Setting up an app ::

   test3('tw1')   min: 0.0114   max: 0.0118   avg: 0.0115
   test3('tw2')   min: 0.0209   max: 0.0246   avg: 0.0216
   test3('ew')   min: 0.1153   max: 0.1172   avg: 0.1161

test4 - Setting up an app. Displaying once. ::

   test4('tw1')   min: 0.0758   max: 0.0781   avg: 0.0771
   test4('tw2')   min: 0.0262   max: 0.0275   avg: 0.0265
   test4('ew')   min: 0.1207   max: 0.1515   avg: 0.1271

test5 - Instantiating widgets many times (and displaying them) ::

   test5('tw1')   min: 1.1217   max: 1.1992   avg: 1.1535
   test5('tw2')   min: 1.2557   max: 1.2825   avg: 1.2628
   test5('ew')   min: 0.6066   max: 0.6289   avg: 0.6202

test6 - Specifying parameters once, then displaying many times. ::

   test6('tw1')   min: 0.5970   max: 0.6077   avg: 0.6034
   test6('tw2')   min: 0.3374   max: 0.3495   avg: 0.3439
   test6('ew')   min: 0.4513   max: 0.4837   avg: 0.4655

test7 - Specifying parameters *and* displaying many times. ::

   test7('tw1')   min: 0.5904   max: 0.5974   avg: 0.5934
   test7('tw2')   min: 0.3349   max: 0.3384   avg: 0.3369
   test7('ew')   min: 0.4522   max: 0.4573   avg: 0.4542

tests with the ``hotshot`` module
---------------------------------

test1
~~~~~

test1 with tw1 -  Handling many WSGI requests ::

         16734 function calls (16112 primitive calls) in 0.123 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.006    0.000    0.017    0.000 base.py:560(prepare_dict)
 1000/600    0.004    0.000    0.009    0.000 registry.py:136(__getattr__)
      100    0.004    0.000    0.004    0.000 runtime.py:14(__init__)
      200    0.003    0.000    0.005    0.000 util.py:352(__get__)
      200    0.003    0.000    0.004    0.000 response.py:38(__init__)


test1 with tw2 -  Handling many WSGI requests ::

         8703 function calls (8600 primitive calls) in 0.072 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  200/100    0.004    0.000    0.044    0.000 widgets.py:236(display)
      100    0.004    0.000    0.026    0.000 template.py:77(render)
      200    0.004    0.000    0.004    0.000 widgets.py:87(__init__)
      100    0.003    0.000    0.063    0.001 middleware.py:148(__call__)
      100    0.003    0.000    0.003    0.000 runtime.py:14(__init__)


test1 with ew -  Handling many WSGI requests ::

         7935 function calls in 0.072 CPU seconds

   Ordered by: internal time, call count
   List reduced from 109 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      200    0.008    0.000    0.009    0.000 render.py:141(__getitem__)
      100    0.007    0.000    0.009    0.000 render.py:156(load)
        5    0.006    0.001    0.006    0.001 render.py:257(__init__)
      100    0.004    0.000    0.014    0.000 string.py:174(safe_substitute)
      100    0.003    0.000    0.044    0.000 widget.py:37(display)



test2
~~~~~

test2 with tw1 -  Handling many (duplicate) resources ::

         1686 function calls (1658 primitive calls) in 0.012 CPU seconds

   Ordered by: internal time, call count
   List reduced from 246 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        9    0.001    0.000    0.003    0.000 pkg_resources.py:468(iter_entry_points)
      289    0.001    0.000    0.001    0.000 pkg_resources.py:493(__iter__)
       44    0.001    0.000    0.001    0.000 posixpath.py:308(normpath)
        1    0.001    0.001    0.005    0.005 template.py:350(_compile_text)
      287    0.001    0.000    0.001    0.000 pkg_resources.py:2223(get_entry_map)


test2 with tw2 -  Handling many (duplicate) resources ::

         2545 function calls (2394 primitive calls) in 0.026 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       52    0.007    0.000    0.011    0.000 params.py:135(__new__)
     52/2    0.003    0.000    0.018    0.009 widgets.py:92(post_define)
     52/2    0.003    0.000    0.019    0.009 widgets.py:31(__new__)
       52    0.002    0.000    0.003    0.000 copy.py:65(copy)
       52    0.001    0.000    0.001    0.000 copy.py:300(_reconstruct)


test2 with ew -  Handling many (duplicate) resources ::

         2688 function calls in 0.018 CPU seconds

   Ordered by: internal time, call count
   List reduced from 109 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.006    0.001    0.006    0.001 render.py:257(__init__)
       36    0.003    0.000    0.005    0.000 pkg_resources.py:2257(insert_on)
     1440    0.001    0.000    0.001    0.000 pkg_resources.py:1831(_normalize_cached)
       11    0.001    0.000    0.003    0.000 pkg_resources.py:468(iter_entry_points)
        9    0.001    0.000    0.001    0.000 pkg_resources.py:534(resolve)



test3
~~~~~

test3 with tw1 -  Setting up an app ::

         348 function calls in 0.002 CPU seconds

   Ordered by: internal time, call count
   List reduced from 49 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.001    0.000    0.001    0.001 pkg_resources.py:468(iter_entry_points)
      122    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)
      123    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)
       23    0.000    0.000    0.000    0.000 base.py:44(__setattr__)
        1    0.000    0.000    0.000    0.000 base.py:249(__new__)


test3 with tw2 -  Setting up an app ::

         602 function calls (599 primitive calls) in 0.004 CPU seconds

   Ordered by: internal time, call count
   List reduced from 49 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        7    0.001    0.000    0.001    0.000 pkg_resources.py:468(iter_entry_points)
        3    0.000    0.000    0.001    0.000 params.py:135(__new__)
      165    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)
      166    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)
        3    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)


test3 with ew -  Setting up an app ::

         2614 function calls in 0.017 CPU seconds

   Ordered by: internal time, call count
   List reduced from 56 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.006    0.001    0.006    0.001 render.py:257(__init__)
       36    0.003    0.000    0.005    0.000 pkg_resources.py:2257(insert_on)
     1440    0.002    0.000    0.002    0.000 pkg_resources.py:1831(_normalize_cached)
       11    0.001    0.000    0.003    0.000 pkg_resources.py:468(iter_entry_points)
        9    0.001    0.000    0.001    0.000 pkg_resources.py:534(resolve)



test4
~~~~~

test4 with tw1 -  Setting up an app. Displaying once. ::

         1686 function calls (1658 primitive calls) in 0.012 CPU seconds

   Ordered by: internal time, call count
   List reduced from 246 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        9    0.001    0.000    0.003    0.000 pkg_resources.py:468(iter_entry_points)
      289    0.001    0.000    0.001    0.000 pkg_resources.py:493(__iter__)
        1    0.001    0.001    0.005    0.005 template.py:350(_compile_text)
       44    0.001    0.000    0.001    0.000 posixpath.py:308(normpath)
      287    0.001    0.000    0.001    0.000 pkg_resources.py:2223(get_entry_map)


test4 with tw2 -  Setting up an app. Displaying once. ::

         683 function calls (679 primitive calls) in 0.005 CPU seconds

   Ordered by: internal time, call count
   List reduced from 115 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        7    0.001    0.000    0.002    0.000 pkg_resources.py:468(iter_entry_points)
      165    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)
      166    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)
        3    0.000    0.000    0.001    0.000 params.py:135(__new__)
        3    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)


test4 with ew -  Setting up an app. Displaying once. ::

         2688 function calls in 0.018 CPU seconds

   Ordered by: internal time, call count
   List reduced from 109 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.006    0.001    0.006    0.001 render.py:257(__init__)
       36    0.003    0.000    0.005    0.000 pkg_resources.py:2257(insert_on)
     1440    0.002    0.000    0.002    0.000 pkg_resources.py:1831(_normalize_cached)
       11    0.001    0.000    0.003    0.000 pkg_resources.py:468(iter_entry_points)
      330    0.001    0.000    0.001    0.000 pkg_resources.py:2223(get_entry_map)



test5
~~~~~

test5 with tw1 -  Instantiating widgets many times (and displaying them) ::

         19503 function calls (19075 primitive calls) in 0.164 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.018    0.000    0.027    0.000 base.py:44(__setattr__)
      100    0.011    0.000    0.046    0.000 base.py:249(__new__)
     2200    0.009    0.000    0.009    0.000 base.py:728(__setattr__)
      100    0.007    0.000    0.009    0.000 meta.py:12(__new__)
      100    0.006    0.000    0.015    0.000 util.py:138(wrapper)


test5 with tw2 -  Instantiating widgets many times (and displaying them) ::

         13703 function calls (13302 primitive calls) in 0.163 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      300    0.035    0.000    0.057    0.000 params.py:135(__new__)
  300/200    0.016    0.000    0.051    0.000 widgets.py:92(post_define)
  300/200    0.016    0.000    0.100    0.000 widgets.py:31(__new__)
      101    0.010    0.000    0.010    0.000 runtime.py:14(__init__)
      300    0.009    0.000    0.017    0.000 copy.py:65(copy)


test5 with ew -  Instantiating widgets many times (and displaying them) ::

         7875 function calls in 0.078 CPU seconds

   Ordered by: internal time, call count
   List reduced from 109 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      202    0.008    0.000    0.009    0.000 render.py:141(__getitem__)
      101    0.008    0.000    0.009    0.000 render.py:156(load)
      100    0.007    0.000    0.008    0.000 widgets.py:48(get_ew_widget)
        5    0.006    0.001    0.006    0.001 render.py:257(__init__)
      101    0.004    0.000    0.014    0.000 string.py:174(safe_substitute)



test6
~~~~~

test6 with tw1 -  Specifying parameters once, then displaying many times. ::

         11286 function calls (10858 primitive calls) in 0.089 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.005    0.000    0.013    0.000 base.py:560(prepare_dict)
      101    0.005    0.000    0.006    0.000 _tw2benchmark_templates_tw1_mak:14(render_body)
 1010/606    0.004    0.000    0.009    0.000 registry.py:136(__getattr__)
      101    0.004    0.000    0.004    0.000 runtime.py:14(__init__)
      101    0.003    0.000    0.026    0.000 runtime.py:387(_render)


test6 with tw2 -  Specifying parameters once, then displaying many times. ::

         5839 function calls (5732 primitive calls) in 0.050 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  202/101    0.004    0.000    0.043    0.000 widgets.py:236(display)
      101    0.004    0.000    0.027    0.000 template.py:77(render)
      101    0.003    0.000    0.005    0.000 runtime.py:14(__init__)
      202    0.003    0.000    0.003    0.000 widgets.py:182(prepare)
      202    0.002    0.000    0.002    0.000 functools.py:17(update_wrapper)


test6 with ew -  Specifying parameters once, then displaying many times. ::

         6588 function calls in 0.061 CPU seconds

   Ordered by: internal time, call count
   List reduced from 109 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      202    0.008    0.000    0.009    0.000 render.py:141(__getitem__)
      101    0.007    0.000    0.009    0.000 render.py:156(load)
        5    0.006    0.001    0.006    0.001 render.py:257(__init__)
      101    0.004    0.000    0.014    0.000 string.py:174(safe_substitute)
      101    0.003    0.000    0.043    0.000 widget.py:37(display)



test7
~~~~~

test7 with tw1 -  Specifying parameters *and* displaying many times. ::

         11286 function calls (10858 primitive calls) in 0.089 CPU seconds

   Ordered by: internal time, call count
   List reduced from 248 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.006    0.000    0.007    0.000 _tw2benchmark_templates_tw1_mak:14(render_body)
      101    0.005    0.000    0.013    0.000 base.py:560(prepare_dict)
 1010/606    0.004    0.000    0.009    0.000 registry.py:136(__getattr__)
      101    0.004    0.000    0.004    0.000 runtime.py:14(__init__)
      202    0.003    0.000    0.005    0.000 util.py:352(__get__)


test7 with tw2 -  Specifying parameters *and* displaying many times. ::

         5783 function calls (5679 primitive calls) in 0.050 CPU seconds

   Ordered by: internal time, call count
   List reduced from 116 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.004    0.000    0.026    0.000 template.py:77(render)
  202/101    0.004    0.000    0.043    0.000 widgets.py:236(display)
      202    0.004    0.000    0.004    0.000 functools.py:17(update_wrapper)
      101    0.003    0.000    0.003    0.000 runtime.py:14(__init__)
      202    0.003    0.000    0.003    0.000 widgets.py:182(prepare)


test7 with ew -  Specifying parameters *and* displaying many times. ::

         6588 function calls in 0.061 CPU seconds

   Ordered by: internal time, call count
   List reduced from 109 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      202    0.008    0.000    0.009    0.000 render.py:141(__getitem__)
      101    0.007    0.000    0.009    0.000 render.py:156(load)
        5    0.005    0.001    0.005    0.001 render.py:257(__init__)
      101    0.004    0.000    0.014    0.000 string.py:174(safe_substitute)
       36    0.004    0.000    0.005    0.000 pkg_resources.py:2257(insert_on)



