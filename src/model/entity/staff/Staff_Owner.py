#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Staff_Owner.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Staff_Owner entity
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.entity.staff.Staff import *

class Staff_Owner(Staff):
    NAME = 'ENTITY_STAFF_OWNER'

    def __init__(self):
        super().__init__()
        self.type = 'Owner'

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