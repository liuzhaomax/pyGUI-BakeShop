#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Item_Coffee.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Item_Coffee entity
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.entity.item.Item import *

class Item_Coffee(Item):
    NAME = 'ENTITY_ITEM_COFFEE'

    def __init__(self):
        super().__init__()
        self.type = 'Coffee'

    def get_type (self):
        '''
        Return item type
        @return: self.type
        '''
        return self.type

    def set_type(self, new_type):
        '''
        Set item type
        @param new_type: str
        @return:
        '''
        self.type = new_type