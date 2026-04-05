import numpy as np

'''
No manual indexing ( vectoried ) 
no np.T
Every row becomes a column
To reshape? The req is TO use manual indexing with loops/ops !
'''
def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # 2. Get rows and columns individually
    A = np.array(A)
    # num_rows = A.shape[0]
    # num_cols = A.shape[1]
    
    # 3. Alternative: Unpack the shape tuple
    rows, cols = A.shape

    m, n = A.shape
    transposed = np.zeros(shape=(n,m))
    for i in range(m):
        for j in range(n):
            transposed[j][i] = A[i][j]
    return transposed
