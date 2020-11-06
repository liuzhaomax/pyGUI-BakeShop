#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Item.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   21-10-2020
@Function       Item entity
'''''''''''''''''''''''''''''''''''''''''''''''''''

class Item():
    NAME = 'ENTITY_ITEM'

    def __init__(self):
        self.item_id = ''
        self.item_name = ''
        self.price = ''

    def get_item_id (self):
        '''
        getter of item_id
        @return: item_id (str)
        '''
        return self.item_id

    def get_item_name(self):
        '''
        getter of item_name
        @return: item_name (str)
        '''
        return self.item_name

    def get_price(self):
        '''
        getter of price
        @return: price (str)
        '''
        return self.price

    def set_item_id(self, new_item_id):
        '''
        setter of item_id
        @param new_item_id:
        @return: item_id (str)
        '''
        self.item_id = new_item_id

    def set_item_name(self, new_item_name):
        '''
        setter of item_name
        @param new_item_name: str
        @return:
        '''
        self.item_name = new_item_name

    def set_price(self, new_price):
        '''
        setter of price
        @param new_price: str
        @return:
        '''
        self.price = new_price