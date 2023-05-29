import os
import numpy as np

from .params import paths 
from PIL import Image

def load_image(path: str, *, source: str=None)-> np.ndarray:

    if source is not None:
        path = os.path.join(paths[source], path)


    image = Image.open(path)
    image = np.array(image)

    return image
