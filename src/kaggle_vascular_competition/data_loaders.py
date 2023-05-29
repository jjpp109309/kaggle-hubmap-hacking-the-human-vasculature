import os
import json;

import numpy as np

from .params import paths 
from PIL import Image

def load_image(path: str, *, source: str=None)-> np.ndarray:

    if source is not None:
        path = os.path.join(paths[source], path)

    image = Image.open(path)
    image = np.array(image, dtype='int')

    return image

def load_polygons(image_id: str)-> dict:

    with open(paths['polygons'], 'r') as jsonl_file:
        for line in jsonl_file:
            if image_id in line:
                break
        else:
            return []

    data: dict = json.loads(line)
    
    polygons: dict = data['annotations']
    for polygon in polygons:
        polygon['coordinates'] = np.array(polygon['coordinates'], dtype='int').squeeze()

    return polygons
