#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Paging.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      30-08-2020
@LastModified   31-08-2020
@Function       Paging
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *

class Paging(Component):
    NAME = 'Paging'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.btn_next = QPushButton('Next', parent)
        self.btn_next.resize(100, self.ctx.style_btn_general_height)
        self.btn_next.move(parent.geometry().width() - self.ctx.style_btn_general_space * 2 - 100, self.ctx.style_btn_general_space)
        self.btn_next.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_next.setStyleSheet(self.ctx.style_btn_general)
        self.btn_prev = QPushButton('Previous', parent)
        self.btn_prev.resize(100, self.ctx.style_btn_general_height)
        self.btn_prev.move(parent.geometry().width() - self.ctx.style_btn_general_space * 2 - 100 - self.ctx.style_btn_general_space - 100, self.ctx.style_btn_general_space)
        self.btn_prev.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_prev.setStyleSheet(self.ctx.style_btn_general)
        return self
