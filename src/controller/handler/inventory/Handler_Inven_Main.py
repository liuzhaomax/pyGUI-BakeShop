#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Inven_Main.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   10-09-2020
@Function       Handler_Inven_Main
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *


class Handler_Inven_Main(Handler):
    NAME = 'HANDLER_INVEN_MAIN_PAGE'

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_view_data(self):
        '''
        Update view by adding data
        @return: self.view
        '''
        self.view.register_data(self.model)
        # self.view.init_data_table_order()
        return self.view

