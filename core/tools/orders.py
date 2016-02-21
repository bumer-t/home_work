# -*- coding: utf-8 -*-

products_count_amount = lambda products : round(sum([i.total_amount for i in products]), 2)

