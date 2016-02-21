# -*- coding: utf-8 -*-
from core.tools.tasks.task_3 import Task3
from core.tools.tasks.task_4 import Task4
from core.tools.tasks import TASK_NUMBER_3, TASK_NUMBER_4


class TaskQueryFactoryMethod(object):
    def __new__(self, task_id):
        """
        :type task_id: int
        """
        if task_id == TASK_NUMBER_3:
            return Task3()
        if task_id == TASK_NUMBER_4:
            return Task4()
        raise NotImplementedError('task_id is bad')
