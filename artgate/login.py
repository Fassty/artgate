from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen


class LoginScreen(ThemableBehavior, MDScreen):
    def __init__(self, app_dir):
        super().__init__()
        self._app_dir = app_dir

    def on_enter(self):
        Window.custom_titlebar = True
        Window.set_custom_titlebar(self.ids.top_bar)
