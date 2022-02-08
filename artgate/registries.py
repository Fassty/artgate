from threading import Lock


class ThreadSafeCategoryRegistry:
    def __init__(self):
        self.dct = {}
        self._lock = Lock()

    def __setitem__(self, key, value):
        with self._lock:
            self.dct[key] = value

    def __getitem__(self, item):
        with self._lock:
            val = self.dct[item]
        return val

    def get_active_keys(self):
        with self._lock:
            active_keys = [k for k, active in self.dct.items() if active]
        return active_keys
