# -*- coding: utf-8 -*-

products_count_amount   = lambda products : round(sum([i.total_amount for i in products]), 2)
products_count_tax      = lambda products : round(sum([i.total_tax for i in products]), 2)

