__author__ = 'stephane'

from central_tendency import *
import math

def variance_population(pop):
    """
    computes the variance of the population
    using the arithmetic mean from central_tendency
    :param pop:
    :return: variance
    """
    mu = mean(pop)
    var = 0.0
    for elem in pop:
        var += (elem-mu)**2
    return var/len(pop)

def variance_alternate(pop):
    mu = mean(pop)
    var = 0.0
    for elem in pop:
        var += elem**2
    return var/len(pop) - mu**2

def variance_alien(pop):
    sumsquared = 0.0
    sum = 0
    n = len(pop)
    for elem in pop:
        sumsquared += elem**2
        sum += elem
    return sumsquared/n - (sum/n)**2

def standard_deviation(variance):
    return math.sqrt(variance)

def variance_sample(pop):
    """
    computes the 'unbiased' variance of a sample (i.e. divided by n-1)
    using the arithmetic mean from central_tendency
    :param pop:
    :return: variance
    """
    popmean = mean(pop)
    var = 0.0
    for elem in pop:
        var += (elem-popmean)**2
    return var/(len(pop)-1)