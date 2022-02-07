import os
from collections import defaultdict
from typing import Dict
from artgate.constants import CATEGORIES


from PIL import Image


def load_images_to_categories(src_path) -> Dict:
    img_dict = defaultdict(list)
    for img_name in os.listdir(src_path):
        # TODO: smarter organisation of image names and categories
        category = img_name.split('.')[0][:-1]
        if category not in CATEGORIES:
            print('SUM TING WONG')
        img = Image.open(os.path.join(src_path, img_name))
        img_dict[category].append(os.path.abspath(os.path.join(src_path, img_name)))
    return img_dict
