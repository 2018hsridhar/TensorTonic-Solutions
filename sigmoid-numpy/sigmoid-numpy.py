import numpy as np

def activation_func(x):
    res = 1.0/(1.0 + np.exp(-1 * x ))
    return res

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    vfunc = np.vectorize(activation_func)
    result = vfunc(x)
    return result    
