# -*- coding: utf-8 -*-
from django.db import connection
from abc import ABCMeta, abstractmethod, abstractproperty


class TaskAbstract(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def TASK_ID(self):
        """
        :rtype: int
        """
        raise NotImplementedError('TASK_ID is NotImplementedError')

    @abstractproperty
    def _sql_query(self):
        """
        :rtype: str
        """
        raise NotImplementedError('_sql_query is NotImplementedError')

    @abstractmethod
    def _orm_result(self):
        """
        :rtype: list
        """
        raise NotImplementedError('_orm_result is NotImplementedError')

    @abstractmethod
    def _validation(self):
        """
        :rtype: bool
        """
        raise NotImplementedError('_validation is NotImplementedError')

    def __cursor_result(self):
        cursor = connection.cursor()
        cursor.execute(self._sql_query)
        return cursor.fetchall()

    def get_result(self):
        if not self._validation():
            return {'message' : 'ERROR: DB is EMPTY'}

        return {
            'cursor_result' : self.__cursor_result(),
            'orm_result'    : self._orm_result(),
        }
