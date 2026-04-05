import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    # Bug in unpacking shape
    if(x.shape != y.shape):
        raise ValueError
    dot_prod = np.sum(np.multiply(x,y))
    return dot_prod
