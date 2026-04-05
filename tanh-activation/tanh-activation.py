import numpy as np

# Hyperbolic tangent : hyperbolics squash values into ranges
# symmetry at 0 / elsewhere :-)
def tanh(x):
    """
    Implement Tanh activation function.
    """
    # # Create the vectorized version
    vfunc = np.vectorize(custom_func)
    result = vfunc(np.asarray(x))
    return result
    

def custom_func(x):
    num = np.exp(x) - np.exp(-x)
    den = np.exp(x) + np.exp(-x)
    res = num / den
    return res