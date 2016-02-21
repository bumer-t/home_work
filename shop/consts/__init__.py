# -*- coding: utf-8 -*-
import abc


def sort_choices(choices):
    return sorted(choices, key=lambda x: x[1])


class CONST_ABSTRACT(object):
    __metaclass__ = abc.ABCMeta

    @classmethod
    def choices(cls):
        raise NotImplementedError

    @classmethod
    def dict(cls):
        return {k: v for k, v in cls.choices()}

    @classmethod
    def choices_for_admin(cls):
        return sort_choices(((key, u'%s (%s)' % (key, title)) for key, title in cls.choices()))

    @classmethod
    def list(cls):
        return [i[0] for i in cls.choices()]

    @classmethod
    def list_lc(cls):
        return [str(i[0]).lower() for i in cls.choices()]

    @classmethod
    def exists(cls, item):
        return item in cls.list()
