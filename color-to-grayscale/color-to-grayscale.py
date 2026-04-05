import numpy as np

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    weight sum based on human viision
    luminance formula
    """
    # m, n, channels = image.shape
    # Use apply_along_axis: axis 2 is the 3D component (RGB)
    # image is a 3d list of shape ( return a 2d list of floats )
    grayColor = np.apply_along_axis(luminance_formula, 2, np.array(image)) 
    return grayColor.tolist()

def luminance_formula(colorPixel):
    rW = 0.299
    gW = 0.587
    bW = 0.114
    R, G, B = colorPixel
    Y = (rW * R) + (gW * G) + (bW * B)
    return Y