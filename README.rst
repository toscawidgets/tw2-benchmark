tw2-benchmark
=============
Comparing toscawidgets1 with tw2 for speed

test1 - Handling many WSGI requests ::

   test1('tw1')   min: 0.0672   max: 0.0709   avg: 0.0687
   test1('tw2')   min: 0.0718   max: 0.0734   avg: 0.0726

test2 - Handling de-duplication of resources ::

   test2('tw1')   min: 0.0675   max: 0.0682   avg: 0.0677
   test2('tw2')   min: 1.3811   max: 1.4183   avg: 1.3986

test3 - Setting up an app ::

   test3('tw1')   min: 0.0009   max: 0.0010   avg: 0.0009
   test3('tw2')   min: 0.0041   max: 0.0044   avg: 0.0042

test4 - Setting up an app. Displaying once. ::

   test4('tw1')   min: 0.0051   max: 0.0075   avg: 0.0055
   test4('tw2')   min: 0.0099   max: 0.0106   avg: 0.0103

test5 - Instantiating widgets many times (and displaying them) ::

   test5('tw1')   min: 0.0405   max: 0.0416   avg: 0.0409
   test5('tw2')   min: 0.0568   max: 0.0590   avg: 0.0573

test6 - Specifying parameters once, then displaying many times. ::

   test6('tw1')   min: 0.0227   max: 0.0233   avg: 0.0230
   test6('tw2')   min: 0.0180   max: 0.0191   avg: 0.0184

test7 - Specifying parameters *and* displaying many times. ::

   test7('tw1')   min: 0.0361   max: 0.0375   avg: 0.0365
   test7('tw2')   min: 0.0356   max: 0.0386   avg: 0.0363

