import numpy as np
from collections import Counter
from scipy import stats

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    input = np.array(x)
    mean = np.mean(input)
    median = np.median(input)
    mode = stats.mode(input, keepdims=True).mode[0] # as a scalar
    sumStats = (mean, median, mode)
    return sumStats
