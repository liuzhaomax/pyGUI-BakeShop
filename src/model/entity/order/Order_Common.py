#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Common.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Order_Common entity
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.entity.order.Order import *


class Order_Common(Order):
    NAME = 'ENTITY_ORDER_COMMON'

    def __init__(self):
        super().__init__()
        self.type = 'Common'

    def get_type (self):
        '''
        Return order type
        @return: self.type
        '''
        return self.type

    def set_type(self, new_type):
        '''
        Set order type
        @param new_type: str
        @return:
        '''
        self.type = new_type