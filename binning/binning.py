import numpy as np

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    Range -> equal width intervals
    
    """
    values = np.asarray(values)
    eps=1e-8
    w = (np.max(values) - np.min(values)) / num_bins
    # Avoid zero-width by adding a tiny epsilon
    w = w if w > 0 else eps
    minX = np.min(values)
    vfunc = np.vectorize(binForm)
    bins = vfunc(values,w, minX, num_bins)
    return list(bins)

def binForm(value, w, minX, num_bins):
    binValue = np.minimum(np.floor((value - minX)/w), num_bins - 1)
    return binValue
    
