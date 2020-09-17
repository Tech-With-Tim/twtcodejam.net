import time

class TimedCache(dict):
    def __init__(self, *, seconds: float, **kwargs):
        self.__del_after = seconds
        super().__init__(**kwargs)

    def __verify_integrity(self):
        current_time = time.monotonic()
        to_remove = [k for (k, (v, t)) in self.items() if current_time > (t + self.__del_after)]
        for item in to_remove:
            del self[item]

    def __getitem__(self, item):
        self.__verify_integrity()
        item = super().__getitem__(item)
        item[1] = time.monotonic()
        return item[0]

    def get(self, key):
        self.__verify_integrity()
        item = super().get(key)
        if item is None:
            return None
        item[1] = time.monotonic()
        return item[0]

    def __setitem__(self, key, value):
        super().__setitem__(key, [value, time.monotonic()])

    def __contains__(self, item):
        self.__verify_integrity()
        return super().__contains__(o=item)
