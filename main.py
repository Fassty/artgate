from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'width', 900)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'shaped', 1)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button


class StrokeButton(Button):
    stroke_color = (0, 0, 0, 1)
    stroke_width = 1.01
    stroke_radius = 20


class MainScreen(Widget):
    def slide_it(self, *args):
        val = args[1]
        if val == 0:
            self.slider_image = 'data/images/slider_cropped.png'
        else:
            self.slider_image = 'data/images/slider_cropped_flipped.png'


class ArtGateApp(App):

    def build(self):
        Window.size = (900, 500)
        Window.shape_image = 'data/images/window_mask900x500.png'
        Window.shape_mode = 'binalpha'
        return MainScreen()


if __name__ == '__main__':
    ArtGateApp().run()


