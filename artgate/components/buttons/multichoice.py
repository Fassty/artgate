from kivy.properties import StringProperty, BooleanProperty, NumericProperty, DictProperty, ObjectProperty
from kivy.core.window import Window

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import FocusBehavior


class SingleChoiceButton(FocusBehavior, MDBoxLayout):
    text = StringProperty()
    value = ObjectProperty()
    active = BooleanProperty(False)

    def on_enter(self):
        Window.set_system_cursor("hand")

    def on_leave(self):
        Window.set_system_cursor("arrow")


class MultiChoiceButton(FocusBehavior, MDBoxLayout):
    text = StringProperty()
    value = ObjectProperty()
    active = BooleanProperty(False)

    def on_enter(self):
        Window.set_system_cursor("hand")

    def on_leave(self):
        Window.set_system_cursor("arrow")
