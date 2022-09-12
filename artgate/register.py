import json
import os

import bcrypt
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen


class RegisterScreen(ThemableBehavior, MDScreen):
    def __init__(self, app_dir: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app_dir = app_dir

        with open(os.path.join(self._app_dir, '.userdata.json')) as f:
            self._user_data = json.load(f)

    def try_register(self):
        self.ids.error_message.text = ''
        username = self.ids.username_field.text

        if username == '':
            self.ids.error_message.text = "Username can't be empty"
            return

        if username in self._user_data['users']:
            self._warn_user_exists(username)
            return

        password = self.ids.password_field.text.encode('utf-8')
        password_2 = self.ids.password_field_2.text.encode('utf-8')

        if password.decode('utf-8') == '':
            self.ids.error_message.text = "Password can't be empty"
            return

        if password != password_2:
            self._warn_passwords_not_matching()
            return

        tos_accepted = self.ids.tos_checkbox.active

        if not tos_accepted:
            self._warn_tos_not_accepted()
            return

        # TODO: sanitize user inputs
        if username != '':
            password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
            self.register_new_user(username, password_hash)

    def register_new_user(self, username, password_hash):
        self._user_data['users'][username] = {'password': password_hash.decode('utf-8')}

        with open(os.path.join(self._app_dir, '.userdata.json'), 'w') as f:
            json.dump(self._user_data, f)

        self.manager.current = 'login_screen'

    def _warn_user_exists(self, username):
        self.ids.error_message.text = f"User \"{username}\" already exists."

    def _warn_passwords_not_matching(self):
        self.ids.error_message.text = "Passwords don't match."

    def _warn_tos_not_accepted(self):
        self.ids.error_message.text = "Accept the fucking TOS, sell us your soul."
