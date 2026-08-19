import pandas as pd
import numpy as np
import math

def optimize(x, f):
    """
    x: starting value x0
    f: f(.) to optimize
    """
    e = 0.1
    
    d1 = deriv(x, f)
    d2 = deriv(d1, f)
    x1 = x - d1/d2

    if abs(x1 - x) <= e:
        return x1
    else:
        optimize(x1, f)


def deriv(x, f):
    """
    f(x+e) - f(x) / e -> f'(x)
    """
    e = 0.1

    d = (f(x+e) - f(x))/e
    
    return d


def quadratic(x):
    return x**2
    