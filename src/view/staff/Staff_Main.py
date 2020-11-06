#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Staff_Main.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      30-08-2020
@LastModified   30-08-2020
@Function       Staff main page
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Layout_Table import *

class Staff_Main(Component):
    NAME = 'STAFF_MAIN_PAGE'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        # layout
        layout_table = Layout_Table()
        self.layout = layout_table.init_compo(parent.main)
        return self