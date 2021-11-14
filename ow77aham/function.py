import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
    
def imshow(X, resize=None):
    X = np.resize(X, resize)
    plt.imshow(X)
    pass