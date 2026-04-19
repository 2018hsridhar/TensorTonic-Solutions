import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
      
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    y_hat = np.mean(y_true)
    numerator = np.sum(np.square(y_true - y_pred))
    denominator = np.sum(np.square(y_true - y_hat))
    # Handle constant target
    if denominator == 0:
        return 1.0 if numerator == 0 else 0.0
    r_squared_score = 1.0 - (numerator/denominator)
    return r_squared_score
