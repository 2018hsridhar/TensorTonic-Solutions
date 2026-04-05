import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # SMH list has no attribtue shape
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    N = y_pred.shape[0]
    delta = y_pred - y_true
    mse = (1/N) * np.sum(np.square(delta))
    return mse
