#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Inventory.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   21-10-2020
@Function       Inventory entity
'''''''''''''''''''''''''''''''''''''''''''''''''''

class Inventory():
    NAME = 'ENTITY_INVENTORY'

    def __init__(self):
        self.list_of_items = []
        self.quantities = {}
        self.dates = {}

    def get_list_of_items(self):
        '''
        getter of list_of_items
        @return: list_of_items(list)
        '''
        return self.list_of_items

    def get_quantities(self):
        '''
        getter of quantities
        @return: quantities(dict)
        '''
        return self.quantities

    def get_dates(self):
        '''
        getter of dates
        @return: dates(dict)
        '''
        return self.dates

    def set_list_of_items(self, new_list_of_items):
        '''
        setter of list_of_items
        @param new_list_of_items: list
        @return:
        '''
        self.list_of_items = new_list_of_items

    def set_quantities(self, new_quantities):
        '''
        setter of quantities
        @param new_quantities: dict
        @return:
        '''
        self.quantities = new_quantities

    def set_dates(self, new_dates):
        '''
        setter of dates
        @param new_dates: dict
        @return:
        '''
        self.dates = new_dates