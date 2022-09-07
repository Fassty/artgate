import os
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import ColorProperty

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

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from artgate.app import ArtGate
from artgate.login import LoginScreen


class ArtGateApp(MDApp):
    def build(self):
        self.load_all_kv_strings()
        Window.size = (overlay_x, overlay_y)
        Window.left = (screen_x - overlay_x) / 2
        Window.top = (screen_y - overlay_y) / 2
        Window.shape_image = f'assets/images/window_mask_color_{overlay_x}x{overlay_y}.png'
        Window.shape_mode = 'colorkey'
        Window.shape_color_key = [0, 1, 0, 1]
        Window.borderless = True

        screen_manager = ScreenManager()

        screen_manager.add_widget(ArtGate(self.directory, name='main_screen'))

        return screen_manager

    def load_all_kv_strings(self):
        for d, dirs, files in os.walk(self.directory):
            for f in files:
                if os.path.splitext(f)[1] == ".kv":
                    path = os.path.join(d, f)
                    with open(path, encoding="utf-8") as kv_file:
                        Builder.load_string(kv_file.read())

    def on_start(self):
        self.root.dispatch("on_enter")


if __name__ == '__main__':
    ArtGateApp().run()
