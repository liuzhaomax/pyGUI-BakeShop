#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Bean.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Order_Bean entity
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.entity.order.Order import *

class Order_Bean(Order):
    NAME = 'ENTITY_ORDER_BEAN'

    def __init__(self):
        super().__init__()
        self.type = 'Bean'
        self.cust_phone = ''

    def get_type(self):
        '''
        Return order type
        @return: self.type
        '''
        return self.type

    def get_cust_phone(self):
        '''
        Return customer phone number
        @return: self.cust_phone
        '''
        return self.cust_phone

    def set_type(self, new_type):
        '''
        Set order type
        @param new_type: str
        @return:
        '''
        self.type = new_type

    def set_cust_phone(self, new_cust_phone):
        '''
        Set customer phone number
        @param new_cust_phone: str
        @return:
        '''
        self.cust_phone = new_cust_phone