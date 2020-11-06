#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   09-09-2020
@Function       Handler base class  
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Controller import *
from src.core.Quick_Sort import *
import datetime


class Handler(Controller):
    NAME = 'HANDLER'

    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

    def update_view(self, parent):
        '''
        Update view
        @return: self.view
        '''
        self.view = self.view.init_compo(parent)
        return self.view

    def update_view_data(self, *args):
        '''
        Update view by adding data
        '''
        pass

    def update_model_data(self, *args):
        '''
        Update model data
        '''
        pass

    def search_orders_by_store_id(self, store_id):
        '''
        Search order by using store id
        @param store_id: str
        @return: orders
        '''
        orders = []
        for i in range(self.model.list_of_stores.__len__()):
            for element in store_id.split('|'):
                if element == self.model.list_of_stores[i].get_store_id():
                    orders += self.model.list_of_stores[i].list_of_orders
                    break
        quick_sort(orders, 'order_id', 0, orders.__len__() - 1)
        return orders

    def search_item_by_item_name(self, item_name):
        '''
        Search item by using item name
        @param item_name: str
        @return: item
        '''
        if str(self.ctx.store_id).__len__() > 2:  # Thread problem fixed: owner store id is 1|2|3|4... Default is 1.
            store_id = str(self.ctx.store_id).split('|')[0]
        else:
            store_id = str(self.ctx.store_id)
        item = None
        for i in range(self.model.get_list_of_stores().__len__()):
            if self.model.get_list_of_stores()[i].get_store_id() == store_id:
                for j in range(self.model.get_list_of_stores()[i].get_inventory().get_list_of_items().__len__()):
                    if self.model.get_list_of_stores()[i].get_inventory().get_list_of_items()[j].get_item_name() == item_name:
                        item = self.model.get_list_of_stores()[i].get_inventory().get_list_of_items()[j]
                        break
                break
        return item

    def search_item_quantity_by_item_id(self, item_id):
        '''
        Search quantity by using item id
        @param item_id: str
        @return: quantity
        '''
        if str(self.ctx.store_id).__len__() > 2:  # Thread problem fixed: owner store id is 1|2|3|4... Default is 1.
            store_id = str(self.ctx.store_id).split('|')[0]
        else:
            store_id = str(self.ctx.store_id)
        quantity = ''
        for i in range(self.model.get_list_of_stores().__len__()):
            if self.model.get_list_of_stores()[i].get_store_id() == store_id:
                quantities = self.model.get_list_of_stores()[i].get_inventory().get_quantities()
                for k in quantities:
                    if k == item_id:
                        quantity = quantities[k]
                        break
                break
        return quantity
