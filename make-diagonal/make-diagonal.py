import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    diagMatrix = np.zeros(shape=(n,n))
    for i in range(len(v)):
        el = v[i]
        diagMatrix[i][i] = el
    return diagMatrix
