import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # square matrix guaranteed
    numRows = len(A)
    trace = 0
    for i in range(numRows):
        el = A[i][i] 
        trace += el
    return trace
