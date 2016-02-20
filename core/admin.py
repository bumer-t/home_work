# -*- coding: utf-8 -*-
from django.contrib import admin
from core.models import User


class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'name', 'data')


admin.site.register(User, UserAdmin)
