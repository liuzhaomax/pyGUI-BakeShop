#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Staff_Main.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       Handler_Staff_Main
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *


class Handler_Staff_Main(Handler):
    NAME = 'HANDLER_STAFF_MAIN_PAGE'

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_view_data(self):
        '''
        Update view by adding data
        '''
        pass

