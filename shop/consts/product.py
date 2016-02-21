# -*- coding: utf-8 -*-
from shop.consts import CONST_ABSTRACT


class SOURCE(CONST_ABSTRACT):
    DOMESTIC    = True
    IMPORT      = False

    @classmethod
    def choices(cls):
        return (
            (cls.DOMESTIC,  u'Отечественный'),
            (cls.IMPORT,    u'Импортный'),
        )
