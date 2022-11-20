"""
For the ML estimates, there are a couple of parameter estimates that hit the
upper bounds. This means the highest likelihood is in the first bin. However,
when using EV, you use a weighted average across bins, and thus one effect of
using the EV is that the parameter estimates are kept away from the bounds.

As a result, the EV estimates are (usually) better behaved and more normally. 
However, if parameters hit bounds may also serve as a warning signal, that tells
you your bounds are too tight. This holds particularly if there is no
theoretically defined limit (see above). Therefore, it is a good idea to inspect
the likelihood surface plots or the ML estimates.
""";
