#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Order_Item_Component.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      28-09-2020
@LastModified   28-09-2020
@Function       Handler_Order_Item_Component
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *
from src.model.entity.System import *


class Handler_Order_Item_Component(Handler):
    NAME = 'HANDLER_ORDER_ITEM_COMPONENT'

    def __init__(self, view, model):
        super().__init__(view, model)

    def set_model(self):
        '''
        Set model data
        @return:
        '''
        self.model = System.get_instance()

    def search_item_name_matched(self, mode, item_name_queried):
        '''
        Search item if the name is matched
        @param mode: str
        @param item_name_queried: str
        @return: items_name_queried_array
        '''
        items_name_queried_array = []
        if str(self.ctx.store_id).__len__() > 2:  # Thread problem fixed: owner store id is 1|2|3|4... Default is 1.
            store_id = str(self.ctx.store_id).split('|')[0]
        else:
            store_id = str(self.ctx.store_id)
        for i in range(self.model.get_list_of_stores().__len__()):
            if self.model.get_list_of_stores()[i].get_store_id() == store_id:
                for j in range(self.model.get_list_of_stores()[i].get_inventory().get_list_of_items().__len__()):
                    if item_name_queried.lower() in self.model.get_list_of_stores()[i].get_inventory().get_list_of_items()[j].get_item_name().lower():
                        if mode == 'bean' and mode == self.model.get_list_of_stores()[i].get_inventory().get_list_of_items()[j].get_type().lower():
                            items_name_queried_array.append(self.model.get_list_of_stores()[i].get_inventory().get_list_of_items()[j].get_item_name())
                        if mode != 'bean' and self.model.get_list_of_stores()[i].get_inventory().get_list_of_items()[j].get_type().lower() != 'bean':
                            items_name_queried_array.append(self.model.get_list_of_stores()[i].get_inventory().get_list_of_items()[j].get_item_name())
                break
        return items_name_queried_array

    def calculate_cost(self, quantity_str, price_str):
        '''
        Calculate the cost for one item
        @param quantity_str: str
        @param price_str: str
        @return: price * quantity
        '''
        if quantity_str:
            quantity = float(quantity_str)
        else:
            quantity = 0.0
        if price_str:
            price = float(price_str)
        else:
            price = 0.0
        return price * quantity


