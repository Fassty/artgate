from kivy.graphics.svg import Svg
from kivy.properties import StringProperty
from kivy.uix.widget import Widget


class SvgWidget(Widget):
    source = StringProperty()

    def on_source(self, instance, value):
        with self.canvas:
            Svg(value)


