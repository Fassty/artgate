from typing import Tuple
import subprocess
from artgate.platform.base import AbstractEnvConnector


class LinuxEnvConnector(AbstractEnvConnector):
    def get_screen_size(self) -> Tuple[int, int]:
        output = subprocess.Popen(
            'xrandr | grep "\*" | cut -d" " -f4',
            shell=True,
            stdout=subprocess.PIPE).communicate()[0]
        screen_x = int(output.replace('\n', '').split('x')[0])
        screen_y = int(output.replace('\n', '').split('x')[1])
        return screen_x, screen_y

    def change_wallpaper(self, image) -> None:
        pass
