"""
The likelihood values for different values of α and β do not vary independently.
Rather, there seems to be a positive correlation between them. Such a
correlation signals that your parameters are to some degree non-identifiable,
and that parameter values trade off against each other.

If this correlation is very strong, then you should take your parameter
estimates with a pinch of salt! Luckily for us the correlation is not very
strong here.

Looking for structure in your likelihood 'landscapes' of simulated and refitted
data is a good way to check whether you have a nicely behaved model with
sufficiently independent/identifiable parameters.
""";
