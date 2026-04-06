def log_transform(values):
    """
    Apply the log1p transformation to each value.
    Handle right-skewed data :: long right tails
    Compressify range -> symmetric distribution!
    log1p
    """
    values = np.asarray(values)
    y = np.log(1 + values)
    return y
    
    
