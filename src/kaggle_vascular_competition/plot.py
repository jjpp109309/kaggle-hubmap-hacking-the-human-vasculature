import numpy as np
import matplotlib.pyplot as plt

from .data_loaders import load_image, load_polygons

contrast_colors = ['#ff030b', '#fffb03', '#0bff03']

def plot_image(image_id: str, source: str)-> None:

    image = load_image(image_id+'.tif', source='train')
    polygons = load_polygons(image_id)

    types = np.unique([polygon['type'] for polygon in polygons])
    colors = {t: color for t, color in list(zip(types, contrast_colors))}

    fig, ax = plt.subplots()
    ax.imshow(image)

    for polygon in polygons:
        type_name = polygon['type']
        color = colors[type_name]
        ax.plot(polygon['coordinates'][:, 0], polygon['coordinates'][:, 1], color, lw=2, label=type_name)

    handles, labels = fig.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.01, 1.02))

    ax.set_title(f'id: {image_id}')

    fig
