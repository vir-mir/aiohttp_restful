from abc import ABC

from aiohttp.hdrs import METH_ALL

__all__ = ['Field']


class Field(ABC):
    type_value = ''

    def __init__(self, *, verbose_name=None, default=None, required=True, methods=None):
        self.value = None
        self.methods = methods or METH_ALL
        self.verbose_name = verbose_name
        self.name = None
        self.required = required
        self.default = default

    def set_name(self, name):
        self.name = name
        return self

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        if self.value is None:
            if callable(self.default):
                return self.default()

            return self.default

        return self.value
