a) Lines 41 and 42 in my code take up by far the most amount of time. Line 41 is the 'for k in 
range(len(Y))' line and line 42 is the multiplication. line 41 takes 18.8 s and line 42 21.9 s 
to run on my system. Together they account for 90.3% of the runtime. Most memory is created in 
the first line as well as in the creation of the first array.

b) I would start to optimize the speed in line 52 where the factorize function is called, since 
this line is by far taking the most time, about 87% of the time on my system. The most memory is 
created by line 52 as well. On my system about 32mb.

c) The best performance I achieved by combining multiple loops into one (matmul_2.py in 
directory) was 32.4 s. A much larger reduction in running time can be achieved when using numpy 
(tomorrows exercise).
