# -*- coding: utf-8 -*-
from django.db.models.aggregates import Count
from core.models import User
from core.tools.task_query import TASK_NUMBER_3
from core.tools.task_query.task_abstract import TaskAbstract


class Task3(TaskAbstract):

    MAX_COUNT = 3

    @property
    def TASK_ID(self):
        return TASK_NUMBER_3

    def _validation(self):
        return User.objects.all().exists()

    @property
    def _sql_query(self):
        return """
                SELECT a.id,
                   a.name,
                   a.data
                FROM core_user a
                LEFT  JOIN
                  (SELECT id,
                          COUNT(name)
                   FROM core_user
                   GROUP BY name
                   HAVING COUNT(name) >= %s LIMIT 1) b ON a.id = b.id LIMIT 1
                """ % self.MAX_COUNT

    def _orm_result(self):
        users = User.objects.filter().values('name').annotate(count_id=Count('name')).order_by('count_id').filter(count_id__gte=self.MAX_COUNT)
        return User.objects.filter(name=users[0]['name'])[0].output
