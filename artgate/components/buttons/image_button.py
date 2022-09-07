from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class ImageButton(FocusBehavior, MDBoxLayout):
    source = StringProperty()
    btn_function = ObjectProperty()

    def on_enter(self):
        Window.set_system_cursor("hand")

    def on_leave(self):
        Window.set_system_cursor("arrow")
