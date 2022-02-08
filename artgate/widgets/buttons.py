from kivy.uix.button import Button

from artgate.globals import category_registry

from artgate.behaviors.hover_behavior import HoverBehavior
from kivy.app import App


class StrokeButtonSmall(HoverBehavior, Button):
    stroke_width = 0.9
    stroke_radius = 17
    stroke_color = (0, 0, 0, .8)
    selected = False

    def _set_alpha(self, val):
        self.canvas.before.children[0].a = val

    def _highlight(self):
        self._set_alpha(0.5)

    def _unhighlight(self):
        self._set_alpha(0)

    def on_enter(self):
        if not self.selected:
            self._highlight()

    def on_leave(self):
        if not self.selected:
            self._unhighlight()


class StrokeButtonLarge(Button):
    stroke_width = 1.1
    stroke_radius = 20
    stroke_color = (0, 0, 0, 1)


class CategoryMultiSelectButton(StrokeButtonSmall):
    _category = None

    def _toggle(self):
        self.selected = not self.selected
        if self.selected:
            self._set_alpha(0.75)
        else:
            self._set_alpha(0)

    def on_release(self):
        if not self.selected:
            self._highlight()

    def on_press(self):
        self._toggle()
        category_registry[self.category] = self.selected

    @property
    def category(self):
        if self._category is None:
            self._category = str(self.text).lower()
        return self._category


class MinimizeButton(StrokeButtonSmall):
    text = '__'

    def on_press(self):
        App.get_running_app().root_window.minimize()


class ExitButton(StrokeButtonSmall):
    text = 'X'

    def on_press(self):
        App.get_running_app().stop()
