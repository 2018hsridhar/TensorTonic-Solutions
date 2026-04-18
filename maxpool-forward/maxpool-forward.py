import math

def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    Feature saliency in input
    """
    height = len(X)
    width = len(X[0])
    print(f"Dimensions: {height}h x {width}w")
    h_out = math.floor((height - pool_size) / stride) + 1
    w_out = math.floor((width - pool_size) / stride) + 1
    output = [[0 for x in range(w_out)] for y in range(h_out)]
    m = len(output)
    n = len(output[0])
    for i in range(m):
        for j in range(n):
            top = i * stride
            bottom = i * stride + pool_size
            left = j * stride
            right = j * stride + pool_size
    
            subMatrix = [row[left:right] for row in X[top:bottom]]
    
            if subMatrix and subMatrix[0]:
                output[i][j] = max(max(row) for row in subMatrix)
    return output
    
