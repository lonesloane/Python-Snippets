__author__ = 'stephane'

"""
X = random variable
E(X) = lambda (expected value)

n : number of attempts
p = probability of success
k: number of 'success'

E(X) = n * p = lambda
p = lambda/n
P(X=K) = probability of K successes in n trials
P(X=k) = P(k) * binomial_coeff(N/k)
P(k) = p**K * (1-p)**(n-k)
binomial_coeff(N/K) = N! / (k! * (N-k)!)
P(X=k) = p**K * (1-p)**(n-K) * n! / (k! * (n-k)!)
P(X=k) = (lambda/n)**k * (1 - lambda/n)**(n-k) * n! / (k! * (n-k)!)

Poisson law:
P(X=k) = lim(n->inf)[(lambda/n)**k * (1 - lambda/n)**(n-k) * n! / (k! * (n-k)!)]
P(X=k) = lambda**k * e**(-lambda) / k!
"""
