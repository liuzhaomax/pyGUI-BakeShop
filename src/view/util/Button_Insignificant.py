#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Button_Insignificant.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      02-09-2020
@LastModified   02-09-2020
@Function       general button
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *

class Button_Insignificant(Component):
    NAME = 'BUTTON_INSIGNIFICANT'

    def __init__(self, btn_name):
        super().__init__()
        self.btn_name = btn_name

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self.btn
        '''
        self.btn = QPushButton(self.btn_name, parent)
        self.btn.setStyleSheet(self.ctx.style_btn_insignificant)
        self.btn.setCursor(QtCore.Qt.PointingHandCursor)
        return self.btn