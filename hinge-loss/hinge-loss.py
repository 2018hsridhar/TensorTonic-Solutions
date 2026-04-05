import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    vfunc = np.vectorize(custom_function)
    intermed = margin - np.multiply(y_true, y_score)
    transform_two = vfunc(intermed)
    hinge_loss = 0
    if reduction == "mean":
        hinge_loss = np.mean(transform_two)
    elif reduction == "sum":
        hinge_loss = np.sum(transform_two)
    return hinge_loss

# Use vectorized functions ( lest coercion ) 
def custom_function(error):
    loss = np.maximum(0,error)
    return loss