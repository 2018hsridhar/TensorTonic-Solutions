import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    Not as outlier sensitive
    L1 ( large err ) L2 ( near 0 ) 
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    prediction_error = y_true - y_pred
    vfunc = np.vectorize(piecewise_loss)
    scalar_mean_loss = np.mean(vfunc(prediction_error, delta))
    return scalar_mean_loss

def piecewise_loss(e,delta):
    loss = 0.0
    if(np.abs(e) <= delta):
        loss = 0.5 * np.square(e)
    else:
        loss = delta * (np.abs(e) - 0.5 * delta)
    return loss
