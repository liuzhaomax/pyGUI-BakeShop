#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Submitting_South.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Order submitting page south panel
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Button_General import *
from src.view.util.Button_Insignificant import *


class Order_Submitting_South(Component):
    NAME = 'ORDER_SUBMITTING_PAGE_SOUTH_PANEL'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        # btn_confirm
        btn_confirm = Button_General('Confirm')
        self.btn_confirm = btn_confirm.init_compo(parent.layout.main_south)
        self.btn_confirm.resize(100, self.ctx.style_btn_general_height)
        self.btn_confirm.move(parent.layout.main_south.geometry().width()/2 - 115, self.ctx.style_btn_general_space)
        # btn_cancel
        btn_cancel = Button_Insignificant('Cancel')
        self.btn_cancel = btn_cancel.init_compo(parent.layout.main_south)
        self.btn_cancel.resize(100, self.ctx.style_btn_general_height)
        self.btn_cancel.move(parent.layout.main_south.geometry().width()/2 + 15, self.ctx.style_btn_general_space)
        return self