import os
import ast
import random

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemableBehavior

from artgate.components.sliders.scroll_bar import ScrollBar
from artgate.components.buttons.multichoice import SingleChoiceButton, MultiChoiceButton
from artgate.components.top_bar import TopBar
from artgate.platform.utils import get_platform_connector, flatten


class MainScreen(ThemableBehavior, MDScreen):
    def __init__(self, app_dir: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_changer_event = None
        self._app_dir = app_dir
        self.platform_connector = get_platform_connector()
        self._was_setup = False

    def _change_wallpaper(self, *args, **kwargs):
        active_widgets = [widget for widget in self.ids.category_box.children if widget.active]
        if not active_widgets:
            return

        wallpaper_dirs = flatten([widget.value for widget in active_widgets])
        if not wallpaper_dirs:
            return

        wallpaper_group: str = random.choice(wallpaper_dirs)

        img_name = random.choice(os.listdir(os.path.join(self._app_dir, 'assets', 'images', 'db', wallpaper_group)))
        img_path = os.path.abspath(os.path.join(self._app_dir, 'assets', 'images', 'db', wallpaper_group, img_name))

        self.platform_connector.change_wallpaper(img_path)

    def set_active_frequency(self, instance_btn):
        for widget in self.ids.freq_box.children:
            if issubclass(widget.__class__, MDBoxLayout):
                if widget == instance_btn:
                    widget.active = True

                    if self.bg_changer_event is not None:
                        self.bg_changer_event.cancel()
                    self.bg_changer_event = Clock.schedule_interval(self._change_wallpaper, widget.value)
                else:
                    widget.active = False

    def set_active_category(self, instance_btn):
        for widget in self.ids.category_box.children:
            if issubclass(widget.__class__, MDBoxLayout) and widget == instance_btn:
                widget.active = not widget.active

    def on_enter(self):
        if not self._was_setup:
            self.list_frequencies()
            self.list_categories()
            self.create_scroll_bar()
            self._was_setup = True

    def list_frequencies(self):
        with open(os.path.join(self._app_dir, 'assets', 'configs', 'frequencies.json')) as freq_data:
            freq_data = ast.literal_eval(freq_data.read())
            for btn_name in freq_data:
                self.ids.freq_box.add_widget(
                    SingleChoiceButton(
                        text=btn_name,
                        value=freq_data[btn_name]['value_in_sec']
                    )
                )

    def list_categories(self):
        with open(os.path.join(self._app_dir, 'assets', 'configs', 'categories.json')) as freq_data:
            freq_data = ast.literal_eval(freq_data.read())
            for btn_name in freq_data:
                self.ids.category_box.add_widget(
                    MultiChoiceButton(
                        text=btn_name,
                        value=freq_data[btn_name]['images']
                    )
                )

    def create_scroll_bar(self):
        names, values = [], []
        with open(os.path.join(self._app_dir, 'assets', 'configs', 'frequencies.json')) as freq_data:
            freq_data = ast.literal_eval(freq_data.read())
            for name in freq_data:
                names.append(name)
                values.append(freq_data[name]['value_in_sec'])
        self.ids.freq_bar.values = values
        self.ids.freq_bar.names = names


class ArtGate(ThemableBehavior, MDScreen):
    def __init__(self, app_dir: str = '', *args, **kwargs):
        self.bg_changer_event = None
        self._app_dir = app_dir
        self.platform_connector = get_platform_connector()
        super().__init__(*args, **kwargs)

    def on_enter(self):
        Window.custom_titlebar = True
        Window.set_custom_titlebar(self.ids.top_bar)
