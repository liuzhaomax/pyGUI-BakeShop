#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       System.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      23-09-2020
@LastModified   23-09-2020
@Function       System entity - single instance mode
'''''''''''''''''''''''''''''''''''''''''''''''''''

class System():
    NAME = 'ENTITY_SYSTEM'

    def __init__(self):
        self.list_of_stores = []

    @classmethod
    def get_instance(cls):
        '''
        Return the instance of the class
        @return: cls._instance
        '''
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    @classmethod
    def set_instance(cls, instance):
        '''
        Set the instance of the class
        @param instance:
        @return:
        '''
        cls._instance = instance

    def get_list_of_stores(self):
        '''
        Return the list of stores
        @return: self.list_of_stores
        '''
        return self.list_of_stores

    def set_list_of_stores(self, new_list_of_stores):
        '''
        Set the list of stores
        @param new_list_of_stores: str
        @return:
        '''
        self.list_of_stores = new_list_of_stores