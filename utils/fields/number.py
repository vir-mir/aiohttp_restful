from middlewares.exceptions import abort
from utils.fields.base import Field

__all__ = ['FieldInteger', 'FieldCompare', 'FieldLarger', 'FieldLess', 'FieldListInteger', 'FieldFloat']


class FieldInteger(Field):
    type_value = 'integer'

    def set_value(self, value):
        try:
            self.value = int(value)
        except ValueError as e:
            abort(400, 'Field "%s" is not Integer, %s' % (self.name, e), help_text='Field is not Integer')


class FieldFloat(Field):
    type_value = 'float'

    def set_value(self, value):
        try:
            self.value = float(value)
        except ValueError as e:
            abort(400, 'Field "%s" is not Float, %s' % (self.name, e), help_text='Field is not Float')


class FieldListInteger(Field):
    def __init__(self, *, sep=',', **kwargs):
        self.sep = sep
        super(FieldListInteger, self).__init__(**kwargs)

    def set_value(self, value):
        try:
            self.value = [int(i) for i in str(value).split(self.sep)]
        except ValueError as e:
            abort(400, 'Field "%s" is not List Integer, %s' % (self.name, e), help_text='Field is not List Integer')


class FieldLess(FieldInteger):
    def __init__(self, *, less: int, eq=False, **kwargs):
        self.less = less
        self.eq = eq
        super(FieldLess, self).__init__(**kwargs)

    def set_value(self, value):
        super(FieldLess, self).set_value(value)
        less = self.less
        eq = '='
        if not self.eq:
            eq = ''
            less -= 1

        if self.value > less:
            abort(400, 'Field "%s" %s <%s %s' % (self.name, self.value, eq, self.less), help_text='Value is not Less')


class FieldLarger(FieldInteger):
    def __init__(self, *, larger: int, eq=False, **kwargs):
        self.larger = larger
        self.eq = eq
        super(FieldLarger, self).__init__(**kwargs)

    def set_value(self, value):
        super(FieldLarger, self).set_value(value)
        larger = self.larger
        eq = '='
        if not self.eq:
            eq = ''
            larger += 1
        if self.value < larger:
            abort(400, 'Field "%s" %s >%s %s' % (self.name, self.value, eq, self.larger),
                  help_text='Value is not Larger')


class FieldCompare(FieldLess, FieldLarger):
    def __init__(self, *, larger: int, less: int, eq=False, **kwargs):
        super(FieldCompare, self).__init__(less=less, larger=larger, eq=eq, **kwargs)
        self.larger = larger
        self.less = less
        self.eq = eq

    def set_value(self, value):
        super(FieldCompare, self).set_value(value)
