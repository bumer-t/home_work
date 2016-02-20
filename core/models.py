# -*- coding: utf-8 -*-
import datetime as dt
from django.db import models


class DateCreatedChanged(models.Model):
    created = models.DateTimeField(u'Дата создания', auto_now_add=True, null=True, default=dt.datetime.now())
    changed = models.DateTimeField(u'Дата модификации', auto_now=True, null=True)

    class Meta:
        abstract = True


class User(models.Model):
    name = models.CharField(u'Name', max_length=30)
    data = models.CharField(u'Data', max_length=30)

    @property
    def output(self):
        return [self.id, self.name, self.data]

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['id']
        app_label           = 'core'
        verbose_name_plural = u'User (task_3)'


class User2(models.Model):
    name = models.CharField(u'Name', max_length=30, unique=True)
    data = models.CharField(u'Data', max_length=30)

    @property
    def output(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['id']
        app_label           = 'core'
        verbose_name_plural = u'User (task_4)'


class Data(models.Model):
    user = models.ManyToManyField(User2, related_name="%(app_label)s_%(class)s_Users2")
    data = models.CharField(u'Data', max_length=30, blank=True, null=True, default=None)

    class Meta:
        ordering    = ['id']
        app_label   = 'core'
