#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Staff_General.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Staff_General entity
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.entity.staff.Staff import *

class Staff_General(Staff):
    NAME = 'ENTITY_STAFF_GENERAL'

    def __init__(self):
        super().__init__()
        self.type = 'General'

    def get_type (self):
        '''
        Return staff type
        @return: self.type
        '''
        return self.type

    def set_type(self, new_type):
        '''
        Set staff type
        @param new_type: str
        @return:
        '''
        self.type = new_type