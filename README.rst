tw2-benchmark
=============
Comparing toscawidgets1 with tw2 for speed (generated: 2011-04-23)

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

   test1('ew')   min: 0.4135   max: 0.4324   avg: 0.4180
   test1('tw1')   min: 0.5704   max: 0.5980   avg: 0.5844
   test1('tw2')   min: 0.5342   max: 0.5496   avg: 0.5403

test2 - Handling many (duplicate) resources ::

   test2('ew')   min: 0.0675   max: 0.0718   avg: 0.0694
   test2('tw1')   min: 0.0359   max: 0.0367   avg: 0.0362
   test2('tw2')   min: 0.1363   max: 0.1402   avg: 0.1375

test3 - Setting up an app ::

   test3('ew')   min: 0.0370   max: 0.0386   avg: 0.0374
   test3('tw1')   min: 0.0027   max: 0.0030   avg: 0.0028
   test3('tw2')   min: 0.0084   max: 0.0093   avg: 0.0089

test4 - Setting up an app. Displaying once. ::

   test4('ew')   min: 0.0675   max: 0.0688   avg: 0.0679
   test4('tw1')   min: 0.0361   max: 0.0399   avg: 0.0371
   test4('tw2')   min: 0.0138   max: 0.0153   avg: 0.0142

test5 - Instantiating widgets many times (and displaying them) ::

   test5('ew')   min: 0.4510   max: 0.4599   avg: 0.4546
   test5('tw1')   min: 0.7051   max: 0.7314   avg: 0.7178
   test5('tw2')   min: 1.1640   max: 1.1893   avg: 1.1741

test6 - Specifying parameters once, then displaying many times. ::

   test6('ew')   min: 0.3841   max: 0.3981   avg: 0.3906
   test6('tw1')   min: 0.4741   max: 0.4873   avg: 0.4802
   test6('tw2')   min: 0.4747   max: 0.4961   avg: 0.4824

test7 - Specifying parameters *and* displaying many times. ::

   test7('ew')   min: 0.3834   max: 0.3881   avg: 0.3850
   test7('tw1')   min: 0.4732   max: 0.4818   avg: 0.4757
   test7('tw2')   min: 0.4743   max: 0.4835   avg: 0.4790

tests with the ``hotshot`` module
---------------------------------

test1
~~~~~

test1 with ew -  Handling many WSGI requests ::

         23698 function calls (23486 primitive calls) in 0.065 CPU seconds

   Ordered by: internal time, call count
   List reduced from 216 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      600    0.004    0.000    0.023    0.000 output.py:451(__call__)
      600    0.003    0.000    0.018    0.000 output.py:628(__call__)
      800    0.003    0.000    0.013    0.000 output.py:759(__call__)
      400    0.003    0.000    0.005    0.000 utils.py:24(push_context)
 1000/800    0.002    0.000    0.004    0.000 base.py:537(_flatten)


test1 with tw1 -  Handling many WSGI requests ::

         30536 function calls (29724 primitive calls) in 0.090 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      600    0.004    0.000    0.025    0.000 output.py:320(__call__)
      600    0.004    0.000    0.019    0.000 output.py:628(__call__)
      800    0.003    0.000    0.014    0.000 output.py:759(__call__)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1000/800    0.002    0.000    0.005    0.000 base.py:537(_flatten)


test1 with tw2 -  Handling many WSGI requests ::

         23033 function calls (22830 primitive calls) in 0.078 CPU seconds

   Ordered by: internal time, call count
   List reduced from 158 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      600    0.005    0.000    0.025    0.000 output.py:451(__call__)
     1400    0.003    0.000    0.003    0.000 posixpath.py:79(split)
      600    0.003    0.000    0.016    0.000 output.py:759(__call__)
      600    0.003    0.000    0.019    0.000 output.py:628(__call__)
      200    0.003    0.000    0.005    0.000 pkg_resources.py:1253(_setup_prefix)



test2
~~~~~

test2 with ew -  Handling many (duplicate) resources ::

         5779 function calls (5765 primitive calls) in 0.013 CPU seconds

   Ordered by: internal time, call count
   List reduced from 214 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.006    0.006 input.py:171(_build_foreign)
     1764    0.002    0.000    0.004    0.000 pyexpat.c:871(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
       45    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)


test2 with tw1 -  Handling many (duplicate) resources ::

         4202 function calls (4182 primitive calls) in 0.008 CPU seconds

   Ordered by: internal time, call count
   List reduced from 274 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.005    0.005 input.py:171(_build_foreign)
     1764    0.002    0.000    0.003    0.000 pyexpat.c:871(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
        2    0.000    0.000    0.000    0.000 eval.py:428(_compile)
        8    0.000    0.000    0.006    0.001 input.py:142(_generate)


test2 with tw2 -  Handling many (duplicate) resources ::

         2519 function calls (2367 primitive calls) in 0.017 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     52/2    0.006    0.000    0.014    0.007 widgets.py:92(post_define)
       52    0.003    0.000    0.005    0.000 params.py:135(__new__)
     52/2    0.001    0.000    0.014    0.007 widgets.py:31(__new__)
       52    0.001    0.000    0.001    0.000 copy.py:65(copy)
        1    0.001    0.001    0.001    0.001 directives.py:166(__call__)



test3
~~~~~

test3 with ew -  Setting up an app ::

         1853 function calls in 0.006 CPU seconds

   Ordered by: internal time, call count
   List reduced from 50 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
       45    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)
     1170    0.001    0.000    0.001    0.000 pkg_resources.py:1831(_normalize_cached)
        9    0.000    0.000    0.001    0.000 pkg_resources.py:534(resolve)
        1    0.000    0.000    0.000    0.000 render.py:175(__init__)


test3 with tw1 -  Setting up an app ::

         114 function calls in 0.001 CPU seconds

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

         5779 function calls (5765 primitive calls) in 0.014 CPU seconds

   Ordered by: internal time, call count
   List reduced from 214 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.006    0.006 input.py:171(_build_foreign)
     1764    0.002    0.000    0.004    0.000 pyexpat.c:871(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
       45    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)


test4 with tw1 -  Setting up an app. Displaying once. ::

         4202 function calls (4182 primitive calls) in 0.008 CPU seconds

   Ordered by: internal time, call count
   List reduced from 274 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.005    0.005 input.py:171(_build_foreign)
     1764    0.002    0.000    0.003    0.000 pyexpat.c:871(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
        2    0.000    0.000    0.000    0.000 eval.py:428(_compile)
        8    0.000    0.000    0.005    0.001 input.py:142(_generate)


test4 with tw2 -  Setting up an app. Displaying once. ::

         461 function calls (456 primitive calls) in 0.002 CPU seconds

   Ordered by: internal time, call count
   List reduced from 158 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/2    0.000    0.000    0.001    0.000 widgets.py:92(post_define)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)
      3/2    0.000    0.000    0.001    0.000 widgets.py:31(__new__)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:2257(insert_on)
        6    0.000    0.000    0.000    0.000 output.py:451(__call__)



test5
~~~~~

test5 with ew -  Instantiating widgets many times (and displaying them) ::

         23766 function calls (23552 primitive calls) in 0.070 CPU seconds

   Ordered by: internal time, call count
   List reduced from 216 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 1010/808    0.004    0.000    0.007    0.000 base.py:537(_flatten)
      606    0.004    0.000    0.026    0.000 output.py:451(__call__)
      606    0.004    0.000    0.020    0.000 output.py:628(__call__)
      100    0.003    0.000    0.004    0.000 widgets.py:48(get_ew_widget)
      808    0.003    0.000    0.015    0.000 output.py:759(__call__)


test5 with tw1 -  Instantiating widgets many times (and displaying them) ::

         33419 function calls (32799 primitive calls) in 0.105 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.011    0.000 base.py:44(__setattr__)
      100    0.005    0.000    0.018    0.000 base.py:249(__new__)
      606    0.004    0.000    0.025    0.000 output.py:320(__call__)
      606    0.004    0.000    0.019    0.000 output.py:628(__call__)
     2200    0.003    0.000    0.003    0.000 base.py:728(__setattr__)


test5 with tw2 -  Instantiating widgets many times (and displaying them) ::

         29469 function calls (28967 primitive calls) in 0.149 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  300/200    0.032    0.000    0.052    0.000 widgets.py:92(post_define)
      300    0.016    0.000    0.025    0.000 params.py:135(__new__)
  300/200    0.007    0.000    0.074    0.000 widgets.py:31(__new__)
      606    0.005    0.000    0.027    0.000 output.py:451(__call__)
      300    0.004    0.000    0.007    0.000 copy.py:65(copy)



test6
~~~~~

test6 with ew -  Specifying parameters once, then displaying many times. ::

         22479 function calls (22265 primitive calls) in 0.061 CPU seconds

   Ordered by: internal time, call count
   List reduced from 216 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.023    0.000 output.py:451(__call__)
      606    0.004    0.000    0.018    0.000 output.py:628(__call__)
      808    0.003    0.000    0.013    0.000 output.py:759(__call__)
      404    0.003    0.000    0.005    0.000 utils.py:24(push_context)
 1010/808    0.002    0.000    0.004    0.000 base.py:537(_flatten)


test6 with tw1 -  Specifying parameters once, then displaying many times. ::

         25202 function calls (24582 primitive calls) in 0.077 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.005    0.000    0.026    0.000 output.py:320(__call__)
      606    0.004    0.000    0.020    0.000 output.py:628(__call__)
      808    0.003    0.000    0.014    0.000 output.py:759(__call__)
 1010/808    0.002    0.000    0.005    0.000 base.py:537(_flatten)
      101    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)


test6 with tw2 -  Specifying parameters once, then displaying many times. ::

         20425 function calls (20217 primitive calls) in 0.069 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:451(__call__)
     1414    0.003    0.000    0.003    0.000 posixpath.py:79(split)
      606    0.003    0.000    0.016    0.000 output.py:759(__call__)
      202    0.003    0.000    0.006    0.000 pkg_resources.py:1253(_setup_prefix)
      606    0.003    0.000    0.019    0.000 output.py:628(__call__)



test7
~~~~~

test7 with ew -  Specifying parameters *and* displaying many times. ::

         22479 function calls (22265 primitive calls) in 0.062 CPU seconds

   Ordered by: internal time, call count
   List reduced from 216 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:451(__call__)
      606    0.004    0.000    0.018    0.000 output.py:628(__call__)
      808    0.003    0.000    0.013    0.000 output.py:759(__call__)
      404    0.003    0.000    0.005    0.000 utils.py:24(push_context)
 1010/808    0.002    0.000    0.005    0.000 base.py:537(_flatten)


test7 with tw1 -  Specifying parameters *and* displaying many times. ::

         25202 function calls (24582 primitive calls) in 0.073 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:320(__call__)
      606    0.004    0.000    0.018    0.000 output.py:628(__call__)
      808    0.003    0.000    0.013    0.000 output.py:759(__call__)
 1010/808    0.002    0.000    0.005    0.000 base.py:537(_flatten)
      101    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)


test7 with tw2 -  Specifying parameters *and* displaying many times. ::

         20361 function calls (20156 primitive calls) in 0.073 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.026    0.000 output.py:451(__call__)
     1414    0.003    0.000    0.003    0.000 posixpath.py:79(split)
      606    0.003    0.000    0.017    0.000 output.py:759(__call__)
      202    0.003    0.000    0.006    0.000 pkg_resources.py:1253(_setup_prefix)
      606    0.003    0.000    0.021    0.000 output.py:628(__call__)



