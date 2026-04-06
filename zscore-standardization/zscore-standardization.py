import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # per column mean /stdDev computation
    # mean = 0 : variance is unit ( 1 ) 
    X = np.asarray(X)
    res = (X - np.mean(X, axis, keepdims=True)) / (eps + np.std(X,axis, keepdims=True))
    return res