import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    if(x.shape != y.shape):
        raise ValueError
    vfunc = np.vectorize(my_func)
    multiplied = vfunc(x,y)
    dot_prod = np.sum(multiplied)
    return dot_prod

def my_func(x,y):
    res = x*y
    return res