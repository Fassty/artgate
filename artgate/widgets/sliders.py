import os

from kivy.uix.slider import Slider


class OverlaySlider(Slider):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.id = 'slider1'
        self.min = 0
        self.max = 1
        self.step = 1
        self.sensitivity = 'all'
        self.cursor_image = 'data/images/slider_cropped.png'

    def on_value(self, *args):
        val = args[1]
        if val == 0:
            self.cursor_image = 'data/images/slider_cropped.png'
        else:
            self.cursor_image = 'data/images/slider_cropped_flipped.png'
