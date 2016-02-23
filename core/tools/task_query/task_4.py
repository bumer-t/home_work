# -*- coding: utf-8 -*-
from core.models import Data, User2
from core.tools.task_query import TASK_NUMBER_4
from core.tools.task_query.task_abstract import TaskAbstract


class Task4(TaskAbstract):

    @property
    def TASK_ID(self):
        return TASK_NUMBER_4

    def _validation(self):
        return User2.objects.all().exists() and Data.objects.all().exists()

    @property
    def _sql_query(self):
        return """
                SELECT name
                FROM core_user2 U
                LEFT JOIN
                  (SELECT DU.user2_id
                   FROM core_data_user DU
                   JOIN
                     (SELECT id
                      FROM core_data a
                      WHERE a.data != '') D ON DU.data_id =D.id) Q2 ON U.id=Q2.user2_id
                WHERE Q2.user2_id IS NULL
                """

    def _orm_result(self):
        user_bad = Data.objects.prefetch_related('user').exclude(data='').values('user')
        users = User2.objects.exclude(id__in=[i['user'] for i in user_bad]).values('name')
        return [i['name'] for i in users]
