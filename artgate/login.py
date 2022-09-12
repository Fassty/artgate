import json
import os
import bcrypt

from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from artgate.components.password_field import PasswordField


class LoginScreen(ThemableBehavior, MDScreen):
    def __init__(self, app_dir: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app_dir = app_dir
        Window.bind(on_key_down=self._on_key_down)

        self._user_data = None

    def on_enter(self):
        # TODO: create a secure DB connection and store data there
        with open(os.path.join(self._app_dir, '.userdata.json')) as f:
            self._user_data = json.load(f)

    def try_log_in(self):
        self.ids.error_message.text = ''
        username = self.ids.username_field.text
        password = self.ids.password_field.text.encode('utf-8')

        if username not in self._user_data['users']:
            self._warn_invalid_credentials()
            return

        hashed_password = self._user_data['users'][username]['password'].encode('utf-8')

        if bcrypt.checkpw(password, hashed_password):
            self._log_in()
            return
        else:
            self._warn_invalid_credentials()
            return

    def _log_in(self):
        self.manager.current = 'main_screen'
        self.manager.current_screen.dispatch('on_enter')

    def _warn_invalid_credentials(self):
        self.ids.password_field.text = ''
        self.ids.error_message.text = "Invalid username and/or password. Please try again."

    def _on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if self.ids.password_field.focus and keycode == 40:
            self.try_log_in()
