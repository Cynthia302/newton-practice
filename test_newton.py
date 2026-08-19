import pytest
import numpy as np
import math
import newton

def test_basic_function():
    assert np.isclose(newton.optimize(2.95, np.cos), math.pi)

def test_input_type():
    with newton.optimize.raises(ValueError):
        newton.optimize(1, 1)
    with newton.optimize.raises(ValueError):
        newton.optimize("string", 1)