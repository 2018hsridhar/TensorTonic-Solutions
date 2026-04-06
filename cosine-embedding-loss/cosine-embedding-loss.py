import numpy as np
# performnace for vector ops

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    Metric learning and siamese networks
    Cosine space : label-based similarity
    """
    dotProd = np.dot(x1,x2)
    normOne = np.linalg.norm(x1)
    normTwo = np.linalg.norm(x2)
    cosScore = dotProd / (normOne * normTwo )
    embedding_loss = 0
    if(label == 1):
        embedding_loss = 1 - cosScore
    elif(label == -1):
        embedding_loss = max(0, cosScore - margin)
    return embedding_loss
