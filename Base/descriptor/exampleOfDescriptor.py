# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

# This is an example of application in descriptor


class _Missing(object):
    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'

_missing = _Missing()


class cached_property(object):
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = name or func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class Foo_Base(object):
    def foo(self):
        print 'first calculate'
        result = 'this is result'
        return result


class Foo(object):
    @cached_property
    def foo(self):
        print 'first calculate'
        result = 'this is result'
        return result


print('Foo'.center(50, '='))
f = Foo()
print f.__dict__
print f.foo
print f.__dict__
print f.foo
print f.__dict__

print('\n'+'Foo_Base'.center(50, '='))
fb = Foo_Base()
print fb.__dict__
print fb.foo
print fb.__dict__
print fb.foo
print fb.__dict__
