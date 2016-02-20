# -*- coding: utf-8 -*-
from django.contrib import admin
from core.models import User, User2, Data


class UserAdmin(admin.ModelAdmin):
    list_per_page   = 20
    list_display    = ('id', 'name', 'data')


class User2Task4Admin(admin.ModelAdmin):
    list_per_page   = 20
    list_display    = ('id', 'name', 'data')


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_custom', 'data')

    def user_custom(self, object):
        return object.user.values_list('name', flat=True)[0]


admin.site.register(User, UserAdmin)
admin.site.register(User2, User2Task4Admin)
admin.site.register(Data, DataAdmin)
