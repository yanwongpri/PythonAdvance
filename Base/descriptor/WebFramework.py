# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


# This is about python's descriptor example
# Source:
# www.jianshu.com/p/250f0d305c35

class WebFramework(object):
    def __init__(self, name='Flask'):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.name = value


class PythonSite(object):

    webframework = WebFramework()

    version = 0.01

    def __init__(self, site):
        self.site = site

    def get_site(self):
        return self.site

    @classmethod
    def get_version(cls):
        return cls.version

    @staticmethod
    def find_version():
        return PythonSite.version

if __name__ == '__main__':
    # example 1
    print('\n' + 'example 1'.center(50, '='))
    print PythonSite.webframework

    # example 2
    print('\n' + 'example 2'.center(50, '='))
    PythonSite.webframework = 'Tornado'
    print PythonSite.webframework

    # example 3
    print('\n' + 'example 3'.center(50, '='))
    webframework = WebFramework()
    print webframework.__get__(webframework, WebFramework)

    # example 4
    print('\n' + 'example 4'.center(50, '='))
    pysite = PythonSite('ghost')
    print vars(PythonSite).items()
    print vars(pysite)
    print PythonSite.__dict__
    # vars is use for list attribute of object
    # it's equal to __dict__

    # example 5
    print('\n' + 'example 5'.center(50, '='))
    pysite1 = PythonSite('ghost')
    pysite2 = PythonSite('admin')
    print PythonSite.version
    print pysite1.version
    print pysite2.version
    print pysite1.version is pysite2.version
    # This, object pysite1 and pysite2 get class PythonSite attribute 'version'
    pysite1.version = 'pysite1'
    # This only add a new attribute for object pysite1
    # but PythonSite attribute 'version' not modified
    print vars(pysite1)
    print vars(pysite2)
    PythonSite.version = 0.02
    # Modified PythonSite attribute, and pysite2's version also changed
    print pysite1.version
    print pysite2.version
    print pysite1.version is pysite2.version

    # example 6
    print('\n' + 'example 6'.center(50, '='))
    print pysite1.site
    print pysite1.__dict__['site']
    print pysite2.version
    try:
        print pysite2.__dict__['version']
    except KeyError:
        print 'There is not \'version\' in pysite2.__dict__'

    # example 7
    print('\n' + 'example 7'.center(50, '='))
    ps = PythonSite('ghost')
    print ps.get_version
    # it's a bound method if not exist __dict__.get_version, will find other class
    print ps.get_version()
    print PythonSite.get_version
    print PythonSite.get_version()
    print vars(ps)
    print type(ps).__dict__['get_version']
    print type(ps).__dict__['get_version'].__get__(ps, type(ps))
    print type(ps).__dict__['get_version'].__get__(ps, type(ps)) == ps.get_version