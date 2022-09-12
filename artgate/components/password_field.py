from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout


class PasswordField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
