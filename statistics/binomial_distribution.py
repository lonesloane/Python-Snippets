__author__ = 'stephane'

import math
"""
Binomial distribution: when there are only 2 possible outcomes for each event

outcome 1: Out1
outcome 2: Out2

P() = probability of an outcome.

if P(Out1) = x then P(Out2) = 1 - x ==> total probability is always 1 (i.e. 100%)

N : total number of attempts

K: number of times the attempt results in Out1

The probability to have K times Out1 out of N attempts is:
P(K) = P(Out1)**K * P(Out2)**(N-K)

How many different ways can we have K times Out1 in N attempts
=> Binomial coefficient (nb of combinations) of K among N:
binomial_coeff = N! / (K! * (N-K)!)

If X is the total number of outputs Out1 with probability P(Out1)
out of N attempts, the probability of having X=K is:
P(X=K) = P(K) * binomial_coeff

Expected value of X if the sum of possible values times the frequency of
occurence of that value (i.e. its probability)
==> Expected value is also the population's arithmetic mean. This is very useful when the
population is 'infinite'

E(X) = Sum( K * P(X=K) ) for K = 0 to N

==> Equivalent to E(X) = N * P(Out1)
"""

POut1 = 0.3
POut2 = 1.0 - POut1


def binomial_coeff(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))


def probability(n, k):
    return POut1**k * POut2**(n-k)


def total_probability(n, k):
    return probability(n, k) * binomial_coeff(n, k)


def expected_value(n):
    return sum([k * total_probability(n, k) for k in range(n+1)])


def main():
    n = 100
    kvalues = [i for i in range(n+1)]
    for k in kvalues:
        print(k,
              "\t", probability(n, k),
              "\t", binomial_coeff(n, k),
              "\t", total_probability(n, k))
    print("expected value for n=%d is %r" % (n, expected_value(n)))


if __name__ == '__main__':
    main()
