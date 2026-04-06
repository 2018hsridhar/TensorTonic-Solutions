import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    dotProd = np.sum(np.multiply(a,b))
    normA = np.linalg.norm(a)
    normB = np.linalg.norm(b)
    if(normA * normB == 0):
        return 0
    cos_sim = dotProd / (normA * normB)
    return cos_sim
