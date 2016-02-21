# -*- coding: utf-8 -*-
from shop.consts import CONST_ABSTRACT


class REQ_CREATE_ORDER(CONST_ABSTRACT):
    PRODUCTS_ID = 'products_id'
    AMOUNT_SIG  = 'amount'
