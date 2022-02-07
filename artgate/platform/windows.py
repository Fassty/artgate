import ctypes
from typing import Tuple
from artgate.platform import *


class WindowsEnvConnector(AbstractEnvConnector):
    def get_screen_size(self) -> Tuple[int, int]:
        user32 = ctypes.windll.user32
        screen_x = user32.GetSystemMetrics(0)
        screen_y = user32.GetSystemMetrics(1)
        return screen_x, screen_y

    def change_wallpaper(self, image_path: str) -> None:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
