import ctypes

from kivy.uix.button import Button

from artgate.constants import CATEGORIES
from artgate.img_utils import load_images_to_categories

IMAGES = load_images_to_categories('data/images/zdroje')
ACTIVE_CATEGORIES = {cat: False for cat in CATEGORIES}

from artgate.behaviors.hover_behavior import HoverBehavior


class StrokeButtonSmall(HoverBehavior, Button):
    stroke_width = 0.9
    stroke_radius = 17
    stroke_color = (0, 0, 0, .8)
    active = False

    def on_enter(self):
        if not self.active:
            self.canvas.before.children[0].a = 0.5
            print("I'm in")

    def on_leave(self):
        if not self.active:
            self.canvas.before.children[0].a = 0
            print("I'm out")

    def on_release(self):
        if not self.active:
            self.canvas.before.children[0].a = 0.5
            print("I'm in")

    def on_press(self):
        self.active = not self.active
        if self.active:
            self.canvas.before.children[0].a = 0.75
            category = str(self.text).lower()
            ACTIVE_CATEGORIES[category] = True
            print(ACTIVE_CATEGORIES)
            img = IMAGES[category][0]
            ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 3)
        else:
            self.canvas.before.children[0].a = 0
            ACTIVE_CATEGORIES[str(self.text).lower()] = False
            print(ACTIVE_CATEGORIES)


class StrokeButtonLarge(Button):
    stroke_width = 1.1
    stroke_radius = 20
    stroke_color = (0, 0, 0, 1)