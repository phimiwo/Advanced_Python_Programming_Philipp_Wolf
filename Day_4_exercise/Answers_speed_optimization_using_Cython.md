### b) 
Without Scipy the code runs for 7.3 s while it only runs for 0.2 s with Scipy.

## c)
According to line_profiler the line that is slowing things down in the python part is the line 
in the third for loop:

r += (X[j, d] - X[i, d]) ** 2

This part of the code accounts for 53.2% of the running time. The loop itself takes up 20.7% of 
the running time. Another part that is taking up time is the following line:

Y[i] += beta[j] * exp(-(r * theta)**2)

This line takes up around 14.9% of the running time.
