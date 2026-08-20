import pandas as pd
import numpy as np
from scipy.differentiate import hessian

def optimize_multivariate(x, f):
    """
    x: starting values vector
    f: f(.) to optimize
    """
    e = 0.1

    d1 = np.gradient(f, x)
    hes = hessian(f, x)
    d2 = np.linalg.inv(hes)
    x1 = x - d2 @ d1

    if abs(x1 - x) <= e:
        return x1
    else:
        return optimize_multivariate(x1, f)

def optimize(x, f):
    """
    x: starting value x0
    f: f(.) to optimize
    """
    if not isinstance(x, float):
        raise ValueError("The starting value must be a number.")

    if not callable(f):
        raise ValueError("Input must be a function.")
    
    e = 0.1

    d1 = deriv(x, f)
    d2 = deriv2(x, f)
    x1 = x - d1 / d2

    if abs(x1 - x) <= e:
        return x1
    else:
        return optimize(x1, f)


def deriv(x, f):
    """
    x: starting value x0
    f: f(.) to optimize

    f(x+e) - f(x) / e -> f'(x)
    """
    e = 0.05

    d = (f(x + e) - f(x)) / e

    return d


def deriv2(x, f):
    """
    x: starting value x0
    f: f(.) to optimize

    f'(x+e) - f'(x) / e -> f''(x)
    """
    e = 0.05

    d = (deriv(x + e, f) - deriv(x, f)) / e

    return d


def quadratic(x):
    """
    x: value

    returns x^2 output
    """
    return x**2
