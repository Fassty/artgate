import random
import time
from threading import Thread, Lock
from artgate.globals import category_registry
from artgate.constants import CATEGORIES
from artgate.img_utils import load_images_to_categories
from artgate.platform import AbstractEnvConnector


class WallPaperChanger(Thread):
    def __init__(self, connector, src_path):
        super().__init__()
        self.name = 'wallpaper_changer_thread'
        self.images = load_images_to_categories(src_path)
        self.connector: AbstractEnvConnector = connector
        self._lock = Lock()

    # TODO: how to change the sleep period?
    def run(self):
        while True:
            active_categories = category_registry.get_active_keys()
            if len(active_categories) == 0:
                continue
            category = random.choice(active_categories)
            if category not in CATEGORIES:
                continue
            image = random.choice(self.images[category])
            self.connector.change_wallpaper(image)
            time.sleep(2)
