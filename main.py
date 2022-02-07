import os
import sys
from kivy.config import Config
from kivy.resources import resource_add_path, resource_find
from artgate.img_utils import load_images_to_categories
from artgate.constants import CATEGORIES
from artgate.platform.utils import get_platform_connector

connector = get_platform_connector()

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'width', 900)
Config.set('graphics', 'height', 500)
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

IMAGES = load_images_to_categories('data/images/zdroje')
ACTIVE_CATEGORIES = {cat: False for cat in CATEGORIES}


class MainScreen(Widget):
    def slide_it(self, *args):
        val = args[1]
        if val == 0:
            self.slider_image = 'data/images/slider_cropped.png'
        else:
            self.slider_image = 'data/images/slider_cropped_flipped.png'


class ArtGateApp(App):

    def build(self):
        screenx, screeny = connector.get_screen_size()
        Window.size = (900, 500)
        Window.shape_image = 'data/images/window_mask900x500.png'
        Window.shape_mode = 'binalpha'
        Window.left = (screenx - 900) / 2
        Window.top = (screeny - 500) / 2
        return MainScreen()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    ArtGateApp().run()


