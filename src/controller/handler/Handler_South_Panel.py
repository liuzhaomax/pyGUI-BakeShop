#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_South_Panel.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       Handler_South_Panel
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *


class Handler_South_Panel(Handler):
    NAME = 'HANDLER_SOUTH_PANEL'

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_view_data(self, parent):
        '''
        Update view by adding data
        @return: self.view
        '''
        return self.view.init_compo(parent)

