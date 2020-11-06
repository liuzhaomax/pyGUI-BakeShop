#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Message.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      18-09-2020
@LastModified   18-10-2020
@Function       Message
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Button_General import *
import time


class Message(Component):
    NAME = 'MESSAGE'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.frame = QFrame(parent)
        self.frame.resize(520, 150)
        self.frame.move(0, parent.geometry().height() - 150)
        self.frame.setStyleSheet(self.ctx.style_dialog_panel)

        self.panel_north_west = QFrame(self.frame)
        self.panel_north_west.resize(490, 30)
        self.panel_north_west.move(0, 0)
        self.panel_north_west.setStyleSheet(self.ctx.style_dialog_panel)
        self.panel_north_east = QFrame(self.frame)
        self.panel_north_east.resize(30, 30)
        self.panel_north_east.move(490, 0)
        self.panel_north_east.setStyleSheet(self.ctx.style_dialog_panel)
        self.panel_south = QFrame(self.frame)
        self.panel_south.resize(520, 120)
        self.panel_south.move(0, 30)
        self.panel_south.setStyleSheet(self.ctx.style_dialog_panel)

        self.label_title = QLabel(self.panel_north_west)
        self.label_title.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_title.resize(490, 30)
        self.label_title.move(30, 0)
        self.label_title.setStyleSheet(self.ctx.style_label_key)

        self.label_content = QLabel(self.panel_south)
        self.label_content.setWordWrap(True)
        self.label_content.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_content.resize(490, 120)
        self.label_content.move(30, 0)
        self.label_content.setStyleSheet(self.ctx.style_label_value)

        # btn_close
        btn_close = Button_General('X')
        self.btn_close = btn_close.init_compo(self.panel_north_east)
        self.btn_close.resize(30, 30)
        self.btn_close.move(0, 0)

        return self
