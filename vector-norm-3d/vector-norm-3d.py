import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    v = np.asarray(v)
    if v.ndim == 1:
        return np.linalg.norm(v)
    # axis : per rwo operation
    # keepdims=True: maintain the batch dimension (result shape will be (3, 1))
    euclid_dist = np.linalg.norm(v, axis = 1, keepdims=False) 
    return euclid_dist
