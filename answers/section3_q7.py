"""
On average, the parameters are estimated well by the model: The green dot is
close to the height of the blue bars. However, there is a lot of variance in the
estimates, despite all data being generated using the same parameter values.

Suggested exercise: Test how good the model is at recovering the parameters. For
this, write a loop around the code to simulate multiple values of alpha and plot
these against the true value. If the model is good at recovering the true
parameters, the points on this scatterplot should be on the unity line.

The EV and ML estimates don't seem to differ much in terms of their performance.
Suggested exercise: Play around with reducing the bin size. Does the performance
of the ML estimates change a lot? What about the EV estimates? Can you think of
why?
""";
