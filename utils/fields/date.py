import datetime

from middlewares.exceptions import abort
from utils.fields import FieldInteger
from utils.fields.base import Field

__all__ = ['FieldDateTime', 'FieldDate', 'FieldTimeStamp']


class FieldDateTime(Field):
    type_value = 'string'

    def __init__(self, format_='%Y-%m-%d %H:%M:%I', **kwargs):
        self.format = format_
        super(FieldDateTime, self).__init__(**kwargs)

    def set_value(self, value):
        self.value = str(value)
        try:
            self.value = datetime.datetime.strptime(self.value, self.format)
        except ValueError as e:
            abort(400, 'Field "%s" is not format date time, %s' % (self.name, e))


class FieldDate(FieldDateTime):
    def __init__(self, format_='%Y-%m-%d', **kwargs):
        super(FieldDateTime, self).__init__(**kwargs)
        self.format = format_

    def set_value(self, value):
        super(FieldDate, self).set_value(value)
        self.value = self.value.date()


class FieldTimeStamp(FieldInteger):
    def set_value(self, value):
        super(FieldTimeStamp, self).set_value(value)
        self.value = datetime.datetime.fromtimestamp(self.value)
