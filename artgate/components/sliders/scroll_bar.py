from kivy.properties import ListProperty
from kivy.uix.scrollview import ScrollView


class ScrollBar(ScrollView):
    names = ListProperty(defaultvalue=['default'])
    values = ListProperty(defaultvalue=[0])
