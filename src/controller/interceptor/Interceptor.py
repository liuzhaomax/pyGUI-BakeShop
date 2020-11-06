#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       interceptor.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      01-09-2020
@LastModified   24-09-2020
@Function       Authorization interceptor
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Aspect import *

class Interceptor(Aspect):
    NAME = 'INTERCEPTOR'

    def __init__(self):
        super().__init__()
        self.permission = ''

    @classmethod
    def get_instance(cls):
        '''
        Return the instance of the class
        @return: cls._instance
        '''
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def get_permission(self):
        '''
        Return the permission
        @return: self.permission
        '''
        return self.permission

    def set_permission(self, permission):
        '''
        Set the permission
        @param permission: str
        @return:
        '''
        self.permission = permission
        self.on_permission_update()

    def on_permission_update(self):
        '''
        Listening the permission changing and broadcast to all observers
        @return:
        '''
        for element in self.observers:
            element.set_permission(self.permission)


