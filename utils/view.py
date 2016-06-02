from abc import ABCMeta
from json import JSONDecodeError

from aiohttp import web

from middlewares.exceptions import abort
from utils.fields.base import Field

__all__ = ['View']


class ViewMeta(ABCMeta):
    def __new__(mcls, name, bases, namespace):
        cls = super(ViewMeta, mcls).__new__(mcls, name, bases, namespace)
        if hasattr(cls, 'Meta'):
            meta = dict(filter(lambda x: issubclass(x[1].__class__, Field), getattr(cls, 'Meta').__dict__.items()))
            cls.objects = cls.objects(meta)
        return cls


class Objects:
    def __init__(self, meta):
        self.__meta = meta

    def __getattr__(self, key):
        return self.__meta[key].get_value()

    def set_data(self, key, val):
        if key in self.__meta:
            self.__meta[key].set_name(key).set_value(val)

    def __requireds(self, data):
        key, field = data
        if field.required:
            val = field.get_value()
            return not (val is not None or val is not field.default)
        return False

    def _requireds(self):
        errors = dict(filter(self.__requireds, self.__meta.items()))
        if errors:
            abort(400, {
                'message': 'required fields',
                'fields': list(errors.keys()),
            })


class View(web.View, metaclass=ViewMeta):
    objects = Objects

    def __await__(self):
        [self.objects.set_data(key, val) for key, val in self.request.match_info.items()]
        [self.objects.set_data(key, val) for key, val in self.request.GET.items()]
        [self.objects.set_data(key, val) for key, val in (yield from self.request.post()).items()]

        try:
            [self.objects.set_data(key, val) for key, val in (yield from self.request.json()).items()]
        except JSONDecodeError:
            pass

        self.objects._requireds()

        return (yield from self.__iter__())
