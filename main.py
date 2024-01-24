import os
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivymd.uix.button import MDFloatingActionButtonSpeedDial

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
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivymd.app import MDApp
from kivy.core.window import Window

from artgate.app import ArtGate
from artgate.login import LoginScreen
from artgate.register import RegisterScreen

import pystray

from PIL import Image, ImageDraw
from threading import Thread


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

image = create_image(64, 64, 'black', 'white')


class ArtGateApp(MDApp):
    visible = True

    def build(self):
        self.load_all_kv_strings()
        Window.size = (overlay_x, overlay_y)
        Window.left = (screen_x - overlay_x) / 2
        Window.top = (screen_y - overlay_y) / 2
        Window.shape_image = f'assets/images/window_mask_color_{overlay_x}x{overlay_y}.png'
        Window.shape_mode = 'colorkey'
        Window.shape_color_key = [0, 1, 0, 1]
        Window.borderless = True

        return ArtGate(self.directory)

    def load_all_kv_strings(self):
        for d, dirs, files in os.walk(self.directory):
            for f in files:
                if os.path.splitext(f)[1] == ".kv":
                    path = os.path.join(d, f)
                    with open(path, encoding="utf-8") as kv_file:
                        Builder.load_string(kv_file.read())

    def on_start(self):
        self.root.dispatch("on_enter")

    def on_stop(self):
        self.root_window.hide()
        return

    def _show(self):
        if not self.visible:
            self.root_window.show()
            self.visible = True

    def _hide(self):
        if self.visible:
            self.root_window.hide()
            self.visible = False


if __name__ == '__main__':
    artgate_app = ArtGateApp()

    # In order for the icon to be displayed, you must provide an icon
    icon = pystray.Icon(
        'test name',
        icon=image,
        menu=pystray.Menu(pystray.MenuItem(text='Clickable', action=artgate_app._show, default=True, visible=False))
    )
    systray_thread = Thread(target=icon.run)
    systray_thread.start()

    artgate_app.run()


