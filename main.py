import os
import sys
from kivy.config import Config
from kivy.resources import resource_add_path, resource_find
from artgate.img_utils import load_images_to_categories
from artgate.constants import CATEGORIES
from artgate.platform.utils import get_platform_connector

connector = get_platform_connector()
screen_x, screen_y = connector.get_screen_size()
# TODO: overlay size based on screen dims
overlay_x, overlay_y = 900, 500

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'width', overlay_x)
Config.set('graphics', 'height', overlay_y)
Config.set('graphics', 'shaped', 1)
Config.set('graphics', 'position', 'custom')

# Has to be imported and registered after configuring graphics
# noinspection PyUnresolvedReferences
from artgate.behaviors.hover_behavior import HoverBehavior
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
# Has to be imported after HoverBehavior
# noinspection PyUnresolvedReferences
from artgate.widgets.buttons import StrokeButtonSmall, StrokeButtonLarge
# noinspection PyUnresolvedReferences
from artgate.widgets.sliders import OverlaySlider

IMAGES = load_images_to_categories('data/images/zdroje')
ACTIVE_CATEGORIES = {cat: False for cat in CATEGORIES}


class MainScreen(Widget):
    pass


class ArtGateApp(App):

    def build(self):
        Window.size = (overlay_x, overlay_y)
        Window.left = (screen_x - overlay_x) / 2
        Window.top = (screen_y - overlay_y) / 2
        Window.shape_image = f'data/images/window_mask{overlay_x}x{overlay_y}.png'
        Window.shape_mode = 'binalpha'
        Window.borderless = True
        return MainScreen()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    ArtGateApp().run()


