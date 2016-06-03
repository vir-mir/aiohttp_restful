import json

from middlewares.exceptions import abort
from utils.fields.base import Field

__all__ = ['FieldString', 'FieldJson', 'FieldEnum']


class FieldString(Field):
    type_value = 'string'

    def set_value(self, value):
        self.value = str(value)


class FieldJson(Field):
    def set_value(self, value):
        try:
            self.value = json.loads(value)
        except json.JSONDecodeError as e:
            abort(400, 'Invalid json field "%s", %s' % (self.name, e))


class FieldEnum(FieldString):
    def __init__(self, *, enum=None, **kwargs):
        self.enum = enum or []
        super(FieldEnum, self).__init__(**kwargs)

    def set_value(self, value):
        super(FieldEnum, self).set_value(value)
        if self.value not in self.enum:
            abort(400, 'Field "%s" %s not [%s]' % (self.name, self.value, ', '.join(self.enum)))
