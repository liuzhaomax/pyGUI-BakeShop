#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Button_General.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      01-09-2020
@LastModified   01-09-2020
@Function       general button
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *

class Button_General(Component):
    NAME = 'BUTTON_GENERAL'

    def __init__(self, btn_name):
        super().__init__()
        self.btn_name = btn_name

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self.btn_gene
        '''
        self.btn_gene = QPushButton(self.btn_name, parent)
        self.btn_gene.setStyleSheet(self.ctx.style_btn_general)
        self.btn_gene.setCursor(QtCore.Qt.PointingHandCursor)
        return self.btn_gene
