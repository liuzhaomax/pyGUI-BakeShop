#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Navi.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       Handler_Navi
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *


class Handler_Navi(Handler):
    NAME = 'HANDLER_NAVI'

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_view_data(self, parent):
        '''
        Update view by adding data
        @return: self.view
        '''
        return self.view.init_compo(parent)

