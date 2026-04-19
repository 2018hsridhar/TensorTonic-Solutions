import numpy as np

def r2_score(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.sum((y_true - y_pred) ** 2)
    denominator = np.sum((y_true - np.mean(y_true)) ** 2)

    # Handle constant target
    if denominator == 0:
        return 1.0 if numerator == 0 else 0.0

    return 1.0 - (numerator / denominator)