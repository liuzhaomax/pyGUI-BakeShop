#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Order entity
'''''''''''''''''''''''''''''''''''''''''''''''''''

class Order():
    NAME = 'ENTITY_ORDER'

    def __init__(self):
        self.order_id = ''
        self.store_id = ''
        self.staff_id = ''
        self.list_of_items = []
        self.quantities = {}
        self.total_cost = ''
        self.date = ''
        self.time = ''
        self.cust_name = ''
        self.status = ''

    def get_order_id (self):
        '''
        Return order id
        @return: self.order_id
        '''
        return self.order_id

    def get_store_id(self):
        '''
        Return store id
        @return: self.store_id
        '''
        return self.store_id

    def get_staff_id(self):
        '''
        Return staff id
        @return: self.staff_id
        '''
        return self.staff_id

    def get_list_of_items(self):
        '''
        Return list of items
        @return: self.list_of_items
        '''
        return self.list_of_items

    def get_quantities(self):
        '''
        Return dict of quantities
        @return: self.quantities
        '''
        return self.quantities

    def get_total_cost(self):
        '''
        Return Total cost
        @return: self.total_cost
        '''
        return self.total_cost

    def get_date(self):
        '''
        Return date creating
        @return: self.date
        '''
        return self.date

    def get_time(self):
        '''
        Return time creating
        @return: self.time
        '''
        return self.time

    def get_cust_name(self):
        '''
        Return customer name
        @return: self.cust_name
        '''
        return self.cust_name

    def get_status(self):
        '''
        Return order status
        @return: self.status
        '''
        return self.status

    def set_order_id(self, new_order_id):
        '''
        Set order id
        @param new_order_id: str
        @return:
        '''
        self.order_id = new_order_id

    def set_store_id(self, new_store_id):
        '''
        Set store id
        @param new_store_id: str
        @return:
        '''
        self.store_id = new_store_id

    def set_staff_id(self, new_staff_id):
        '''
        Set staff id
        @param new_staff_id: str
        @return:
        '''
        self.staff_id = new_staff_id

    def set_list_of_items(self, new_list_of_items):
        '''
        Set list of items
        @param new_list_of_items: list
        @return:
        '''
        self.list_of_items = new_list_of_items

    def set_quantities(self, new_quantities):
        '''
        Set quantities
        @param new_quantities: dict
        @return:
        '''
        self.quantities = new_quantities

    def set_total_cost(self, new_total_cost):
        '''
        Set total cost
        @param new_total_cost: str
        @return:
        '''
        self.total_cost = new_total_cost

    def set_date(self, new_date):
        '''
        Set date creating
        @param new_date: str
        @return:
        '''
        self.date = new_date

    def set_time(self, new_time):
        '''
        Set time creating
        @param new_time: str
        @return:
        '''
        self.time = new_time

    def set_cust_name(self, new_cust_name):
        '''
        Set customer name
        @param new_cust_nme: str
        @return:
        '''
        self.cust_name = new_cust_name

    def set_status(self, new_status):
        '''
        Set order status
        @param new_status: str
        @return:
        '''
        self.status = new_status