from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'shaped', 1)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class MainScreen(Widget):
    pass


class ArtGateApp(App):

    def build(self):
        Window.size = (800, 600)
        Window.shape_image = 'data/images/window_mask.png'
        Window.shape_mode = 'binalpha'
        return MainScreen()


if __name__ == '__main__':
    ArtGateApp().run()


