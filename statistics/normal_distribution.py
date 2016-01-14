__author__ = 'stephane'

"""
Normal distribution, a.k.a. Gaussian distribution or bell curve
==> a good approximation for the binomial distribution if enough samples

P(X) = [1 / (std_dev * sqrt(2*pi))] * e**[ -1/2*((X-popmean)/std_dev)**2 ]

(X - popmean) / std_dev = Zscore ==> how many standard deviations away are we from the population mean

P(X) = 1 / [sqrt(2pi) * std_dev * e**Zscore ]


Empirical Rule (a.k.a. 68-95-99.7 rule):

mean - std_dev <  P(x) < mean - std_dev = 68%
mean - 2*std_dev <  P(x) < mean - 2*std_dev = 95%
mean - 3*std_dev <  P(x) < mean - 3*std_dev = 99.7%

"""