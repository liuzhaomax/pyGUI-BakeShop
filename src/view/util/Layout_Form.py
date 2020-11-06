#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Layout_Form.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      01-09-2020
@LastModified   01-09-2020
@Function       layout of list page
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *

class Layout_Form(Component):
    NAME = 'LAYOUT_OF_LIST_PAGE'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.main = QFrame(parent)
        self.main.setVisible(False)
        self.main.resize(parent.geometry().width() - 40, parent.geometry().height() - 60)
        self.main.move(20, 20)
        self.main.setStyleSheet(self.ctx.style_mian_body)
        # layout
        self.main_north = QFrame(self.main)
        self.main_north.setMinimumWidth(800)
        self.main_north.resize(self.main.geometry().width(), self.main.geometry().height() * 1 / 9)
        self.main_north.move(0, 0)
        self.main_north.setStyleSheet(self.ctx.style_frame)
        self.main_middle = QFrame(self.main)
        self.main_middle.setMinimumWidth(800)
        self.main_middle.resize(self.main.geometry().width(), self.main.geometry().height() * 7 / 9)
        self.main_middle.move(0, 100)
        self.main_middle.setStyleSheet(self.ctx.style_frame)
        self.main_south = QFrame(self.main)
        self.main_south.setMinimumWidth(800)
        self.main_south.resize(self.main.geometry().width(), self.main.geometry().height() * 1 / 9)
        self.main_south.move(0, 800)
        self.main_south.setStyleSheet(self.ctx.style_frame)

        self.main_north_west = QFrame(self.main_north)
        self.main_north_west.setMinimumWidth(400)
        self.main_north_west.resize(self.main_north.geometry().width() / 2, self.main_north.geometry().height())
        self.main_north_west.move(0, 0)
        self.main_north_west.setStyleSheet(self.ctx.style_frame)
        self.main_north_east = QFrame(self.main_north)
        self.main_north_east.setMinimumWidth(400)
        self.main_north_east.resize(self.main_north.geometry().width() / 2, self.main_north.geometry().height())
        self.main_north_east.move(self.main_north.geometry().width() / 2, 0)
        self.main_north_east.setStyleSheet(self.ctx.style_frame)

        self.main_middle_west = QFrame(self.main_middle)
        self.main_middle_west.setMinimumWidth(400)
        self.main_middle_west.resize(self.main_middle.geometry().width() / 2, self.main_middle.geometry().height())
        self.main_middle_west.move(0, 0)
        self.main_middle_west.setStyleSheet(self.ctx.style_frame)
        self.main_middle_east = QFrame(self.main_middle)
        self.main_middle_east.setMinimumWidth(400)
        self.main_middle_east.resize(self.main_middle.geometry().width() / 2, self.main_middle.geometry().height())
        self.main_middle_east.move(self.main_middle.geometry().width() / 2, 0)
        self.main_middle_east.setStyleSheet(self.ctx.style_frame)
        return self