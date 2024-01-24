from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.boxlayout import MDBoxLayout


class PasswordField(MDBoxLayout):
    hint_text = StringProperty()

    @property
    def text(self):
        return self.ids.text_field.text

    @text.setter
    def text(self, value):
        self.ids.text_field.text = value

    @property
    def focus(self):
        return self.ids.text_field.focus

    @focus.setter
    def focus(self, value):
        self.ids.text_field.focus = value
