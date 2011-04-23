tw2-benchmark
=============
Comparing toscawidgets1, tw2, and EasyWidgets for speed (generated: 2011-04-23)

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
   :scale: 400 %

   Normalized score results in order tw1, tw2, ew
``timeit`` summary
------------------

- tw1 wins at

  - test3 - Setting up an app 

  - test2 - Handling many (duplicate) resources 

- tw2 wins at

  - test4 - Setting up an app. Displaying once. 

- ew wins at

  - test1 - Handling many WSGI requests 

  - test5 - Instantiating widgets many times (and displaying them) 

  - test7 - Specifying parameters *and* displaying many times. 

  - test6 - Specifying parameters once, then displaying many times. 

tests with the ``timeit`` module
--------------------------------

test1 - Handling many WSGI requests ::

   test1('tw1')   min: 0.5724   max: 0.5846   avg: 0.5787
   test1('tw2')   min: 0.5390   max: 0.5569   avg: 0.5438
   test1('ew')   min: 0.4221   max: 0.4319   avg: 0.4255

test2 - Handling many (duplicate) resources ::

   test2('tw1')   min: 0.0407   max: 0.0447   avg: 0.0422
   test2('tw2')   min: 0.1400   max: 0.1462   avg: 0.1416
   test2('ew')   min: 0.0780   max: 0.0808   avg: 0.0792

test3 - Setting up an app ::

   test3('tw1')   min: 0.0049   max: 0.0051   avg: 0.0049
   test3('tw2')   min: 0.0117   max: 0.0125   avg: 0.0122
   test3('ew')   min: 0.0466   max: 0.0486   avg: 0.0473

test4 - Setting up an app. Displaying once. ::

   test4('tw1')   min: 0.0407   max: 0.0427   avg: 0.0414
   test4('tw2')   min: 0.0171   max: 0.0181   avg: 0.0174
   test4('ew')   min: 0.0773   max: 0.0834   avg: 0.0788

test5 - Instantiating widgets many times (and displaying them) ::

   test5('tw1')   min: 0.7086   max: 0.7167   avg: 0.7128
   test5('tw2')   min: 1.1638   max: 1.1760   avg: 1.1681
   test5('ew')   min: 0.4614   max: 0.4691   avg: 0.4648

test6 - Specifying parameters once, then displaying many times. ::

   test6('tw1')   min: 0.4768   max: 0.4885   avg: 0.4826
   test6('tw2')   min: 0.4810   max: 0.4878   avg: 0.4841
   test6('ew')   min: 0.3935   max: 0.4014   avg: 0.3963

test7 - Specifying parameters *and* displaying many times. ::

   test7('tw1')   min: 0.4780   max: 0.4824   avg: 0.4796
   test7('tw2')   min: 0.4752   max: 0.4961   avg: 0.4821
   test7('ew')   min: 0.3954   max: 0.4086   avg: 0.3999

tests with the ``hotshot`` module
---------------------------------

test1
~~~~~

test1 with tw1 -  Handling many WSGI requests ::

         31076 function calls (30264 primitive calls) in 0.091 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      600    0.005    0.000    0.025    0.000 output.py:320(__call__)
      600    0.004    0.000    0.018    0.000 output.py:628(__call__)
      800    0.003    0.000    0.013    0.000 output.py:759(__call__)
      100    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1000/800    0.002    0.000    0.005    0.000 base.py:537(_flatten)


test1 with tw2 -  Handling many WSGI requests ::

         23502 function calls (23299 primitive calls) in 0.077 CPU seconds

   Ordered by: internal time, call count
   List reduced from 158 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      600    0.004    0.000    0.023    0.000 output.py:451(__call__)
     1400    0.003    0.000    0.003    0.000 posixpath.py:79(split)
      600    0.003    0.000    0.015    0.000 output.py:759(__call__)
      200    0.003    0.000    0.005    0.000 pkg_resources.py:1253(_setup_prefix)
      600    0.003    0.000    0.018    0.000 output.py:628(__call__)


test1 with ew -  Handling many WSGI requests ::

         24423 function calls (24211 primitive calls) in 0.069 CPU seconds

   Ordered by: internal time, call count
   List reduced from 222 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      600    0.004    0.000    0.019    0.000 output.py:628(__call__)
      600    0.004    0.000    0.024    0.000 output.py:451(__call__)
      800    0.003    0.000    0.013    0.000 output.py:759(__call__)
      400    0.003    0.000    0.005    0.000 utils.py:24(push_context)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)



test2
~~~~~

test2 with tw1 -  Handling many (duplicate) resources ::

         4742 function calls (4722 primitive calls) in 0.009 CPU seconds

   Ordered by: internal time, call count
   List reduced from 274 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.005    0.005 input.py:171(_build_foreign)
     1764    0.002    0.000    0.003    0.000 pyexpat.c:853(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
        9    0.001    0.000    0.001    0.000 pkg_resources.py:468(iter_entry_points)
      287    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)


test2 with tw2 -  Handling many (duplicate) resources ::

         2889 function calls (2737 primitive calls) in 0.018 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     52/2    0.006    0.000    0.014    0.007 widgets.py:92(post_define)
       52    0.003    0.000    0.005    0.000 params.py:135(__new__)
     52/2    0.001    0.000    0.014    0.007 widgets.py:31(__new__)
       52    0.001    0.000    0.001    0.000 copy.py:65(copy)
      106    0.001    0.000    0.001    0.000 functools.py:17(update_wrapper)


test2 with ew -  Handling many (duplicate) resources ::

         6504 function calls (6490 primitive calls) in 0.014 CPU seconds

   Ordered by: internal time, call count
   List reduced from 220 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
        1    0.002    0.002    0.005    0.005 input.py:171(_build_foreign)
     1764    0.002    0.000    0.003    0.000 pyexpat.c:853(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
       36    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)



test3
~~~~~

test3 with tw1 -  Setting up an app ::

         348 function calls in 0.001 CPU seconds

   Ordered by: internal time, call count
   List reduced from 49 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:468(iter_entry_points)
      123    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)
      122    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)
       23    0.000    0.000    0.000    0.000 base.py:44(__setattr__)
        1    0.000    0.000    0.000    0.000 base.py:249(__new__)


test3 with tw2 -  Setting up an app ::

         602 function calls (599 primitive calls) in 0.002 CPU seconds

   Ordered by: internal time, call count
   List reduced from 49 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/2    0.000    0.000    0.001    0.000 widgets.py:92(post_define)
        7    0.000    0.000    0.001    0.000 pkg_resources.py:468(iter_entry_points)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)
      165    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)
      166    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)


test3 with ew -  Setting up an app ::

         2578 function calls in 0.007 CPU seconds

   Ordered by: internal time, call count
   List reduced from 56 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
       36    0.001    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)
       11    0.001    0.000    0.001    0.000 pkg_resources.py:468(iter_entry_points)
     1404    0.001    0.000    0.001    0.000 pkg_resources.py:1831(_normalize_cached)
      330    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)



test4
~~~~~

test4 with tw1 -  Setting up an app. Displaying once. ::

         4742 function calls (4722 primitive calls) in 0.009 CPU seconds

   Ordered by: internal time, call count
   List reduced from 274 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.005    0.005 input.py:171(_build_foreign)
     1764    0.002    0.000    0.003    0.000 pyexpat.c:853(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
        9    0.001    0.000    0.001    0.000 pkg_resources.py:468(iter_entry_points)
      287    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)


test4 with tw2 -  Setting up an app. Displaying once. ::

         831 function calls (826 primitive calls) in 0.003 CPU seconds

   Ordered by: internal time, call count
   List reduced from 158 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/2    0.000    0.000    0.001    0.000 widgets.py:92(post_define)
        7    0.000    0.000    0.001    0.000 pkg_resources.py:468(iter_entry_points)
      165    0.000    0.000    0.000    0.000 pkg_resources.py:2223(get_entry_map)
      166    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)
        3    0.000    0.000    0.000    0.000 params.py:135(__new__)


test4 with ew -  Setting up an app. Displaying once. ::

         6504 function calls (6490 primitive calls) in 0.015 CPU seconds

   Ordered by: internal time, call count
   List reduced from 220 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)
        1    0.002    0.002    0.005    0.005 input.py:171(_build_foreign)
     1764    0.002    0.000    0.003    0.000 pyexpat.c:853(Default)
     1764    0.002    0.000    0.002    0.000 input.py:237(_handle_other)
       36    0.002    0.000    0.002    0.000 pkg_resources.py:2257(insert_on)



test5
~~~~~

test5 with tw1 -  Instantiating widgets many times (and displaying them) ::

         33959 function calls (33339 primitive calls) in 0.105 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2300    0.007    0.000    0.010    0.000 base.py:44(__setattr__)
      100    0.005    0.000    0.018    0.000 base.py:249(__new__)
      606    0.004    0.000    0.025    0.000 output.py:320(__call__)
      606    0.003    0.000    0.019    0.000 output.py:628(__call__)
      100    0.003    0.000    0.004    0.000 meta.py:12(__new__)


test5 with tw2 -  Instantiating widgets many times (and displaying them) ::

         29839 function calls (29337 primitive calls) in 0.148 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  300/200    0.032    0.000    0.051    0.000 widgets.py:92(post_define)
      300    0.015    0.000    0.025    0.000 params.py:135(__new__)
  300/200    0.007    0.000    0.073    0.000 widgets.py:31(__new__)
      606    0.004    0.000    0.018    0.000 output.py:759(__call__)
      300    0.004    0.000    0.007    0.000 copy.py:65(copy)


test5 with ew -  Instantiating widgets many times (and displaying them) ::

         24491 function calls (24277 primitive calls) in 0.071 CPU seconds

   Ordered by: internal time, call count
   List reduced from 222 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:451(__call__)
      606    0.004    0.000    0.019    0.000 output.py:628(__call__)
      100    0.003    0.000    0.004    0.000 widgets.py:48(get_ew_widget)
      808    0.003    0.000    0.013    0.000 output.py:759(__call__)
      404    0.003    0.000    0.005    0.000 utils.py:24(push_context)



test6
~~~~~

test6 with tw1 -  Specifying parameters once, then displaying many times. ::

         25742 function calls (25122 primitive calls) in 0.076 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.025    0.000 output.py:320(__call__)
      606    0.004    0.000    0.019    0.000 output.py:628(__call__)
      808    0.003    0.000    0.014    0.000 output.py:759(__call__)
 1010/808    0.002    0.000    0.005    0.000 base.py:537(_flatten)
      101    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)


test6 with tw2 -  Specifying parameters once, then displaying many times. ::

         20795 function calls (20587 primitive calls) in 0.069 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:451(__call__)
     1414    0.003    0.000    0.003    0.000 posixpath.py:79(split)
      606    0.003    0.000    0.016    0.000 output.py:759(__call__)
      202    0.003    0.000    0.006    0.000 pkg_resources.py:1253(_setup_prefix)
      606    0.003    0.000    0.019    0.000 output.py:628(__call__)


test6 with ew -  Specifying parameters once, then displaying many times. ::

         23204 function calls (22990 primitive calls) in 0.062 CPU seconds

   Ordered by: internal time, call count
   List reduced from 222 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.023    0.000 output.py:451(__call__)
      606    0.003    0.000    0.017    0.000 output.py:628(__call__)
      808    0.003    0.000    0.013    0.000 output.py:759(__call__)
      404    0.003    0.000    0.005    0.000 utils.py:24(push_context)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)



test7
~~~~~

test7 with tw1 -  Specifying parameters *and* displaying many times. ::

         25742 function calls (25122 primitive calls) in 0.074 CPU seconds

   Ordered by: internal time, call count
   List reduced from 276 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:320(__call__)
      808    0.004    0.000    0.013    0.000 output.py:759(__call__)
      606    0.004    0.000    0.018    0.000 output.py:628(__call__)
      101    0.002    0.000    0.006    0.000 base.py:560(prepare_dict)
 1010/808    0.002    0.000    0.005    0.000 base.py:537(_flatten)


test7 with tw2 -  Specifying parameters *and* displaying many times. ::

         20731 function calls (20526 primitive calls) in 0.070 CPU seconds

   Ordered by: internal time, call count
   List reduced from 159 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:451(__call__)
     1414    0.003    0.000    0.003    0.000 posixpath.py:79(split)
      606    0.003    0.000    0.016    0.000 output.py:759(__call__)
      202    0.003    0.000    0.006    0.000 pkg_resources.py:1253(_setup_prefix)
      606    0.003    0.000    0.019    0.000 output.py:628(__call__)


test7 with ew -  Specifying parameters *and* displaying many times. ::

         23204 function calls (22990 primitive calls) in 0.065 CPU seconds

   Ordered by: internal time, call count
   List reduced from 222 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      606    0.004    0.000    0.024    0.000 output.py:451(__call__)
      606    0.004    0.000    0.019    0.000 output.py:628(__call__)
      808    0.003    0.000    0.014    0.000 output.py:759(__call__)
      404    0.003    0.000    0.005    0.000 utils.py:24(push_context)
        5    0.002    0.000    0.002    0.000 render.py:257(__init__)



