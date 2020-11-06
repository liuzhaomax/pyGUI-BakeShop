#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Item_Bean.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Item_Bean entity
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.entity.item.Item import *

class Item_Bean(Item):
    NAME = 'ENTITY_ITEM_BEAN'

    def __init__(self):
        super().__init__()
        self.type = 'Bean'

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