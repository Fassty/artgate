from abc import ABC, abstractmethod
from typing import Tuple


class AbstractEnvConnector(ABC):
    @abstractmethod
    def get_screen_size(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def change_wallpaper(self, image) -> None:
        pass
