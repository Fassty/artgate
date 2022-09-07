import itertools
import sys
from typing import Iterable

from artgate.platform import *
from artgate.constants import PlatformType

PLATFORM_CONNECTOR_MAPPING = {
    PlatformType.LINUX: LinuxEnvConnector,
    PlatformType.WINDOWS: WindowsEnvConnector
}


def determine_platform() -> str:
    if sys.platform == 'linux2':
        return PlatformType.LINUX
    if sys.platform == 'win32':
        return PlatformType.WINDOWS
    else:
        raise NotImplementedError('Unsupported platform')


def get_platform_connector() -> AbstractEnvConnector:
    platform: str = determine_platform()
    return PLATFORM_CONNECTOR_MAPPING[platform]()


def flatten(lst):
    return list(itertools.chain(*lst))
