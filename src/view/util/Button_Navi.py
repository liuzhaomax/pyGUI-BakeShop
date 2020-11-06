#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Button_Navi.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      01-09-2020
@LastModified   01-09-2020
@Function       Button in Navi
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *

class Button_Navi(Component):
    NAME = 'BUTTON_NAVI'

    def __init__(self, btn_name):
        super().__init__()
        self.btn_name = btn_name

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self.btn_navi
        '''
        self.btn_navi = QPushButton(self.btn_name, parent)
        self.btn_navi.setStyleSheet(self.ctx.style_btn_navi)
        self.btn_navi.setCursor(QtCore.Qt.PointingHandCursor)
        return self.btn_navi
