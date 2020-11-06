#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Order_Main.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   09-09-2020
@Function       Handler_Order_Main
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *


class Handler_Order_Main(Handler):
    NAME = 'HANDLER_ORDER_MAIN_PAGE'

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_view_data(self):
        '''
        Update view by adding data
        @return: self.view
        '''
        data = self.search_orders_by_store_id(self.ctx.store_id)
        self.view.register_data(data)
        self.view.init_data_table_order()
        return self.view




