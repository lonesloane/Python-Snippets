__author__ = 'stephane'

import numpy as np
import matplotlib.pyplot as xplot


def nderiv(y, x):
    """Difference finie, derivee de la fonction f"""
    n = len(y)
    d = np.zeros(n, 'd')    # virgule flottante a double precision
    # differences de part et d'autre
    # centrees sur les points precedents
    for i in range(1, n-1):
        d[i] = (y[i+1]-y[i-1]) / (x[i+1]-x[i-1])
    # difference sur un seul cote pour les extremites
    d[0] = (y[1] - y[0]) / (x[1] - x[0])
    d[n-1] = (y[n-1] - y[n-2]) / (x[n-1] - x[n-2])
    return d


x = np.linspace(0, 2*np.pi, 100)
dsin = nderiv(np.sin(x), x)
xplot.plot(x, dsin, label='numerical')
xplot.plot(x, np.cos(x), label='analytical')
xplot.title("Comparison of analytical and numerical derivative of sin(x)")
xplot.legend()
xplot.show()
