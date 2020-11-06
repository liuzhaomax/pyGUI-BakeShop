#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Dialog_Confirm.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       confirm dialog
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Button_General import *
from src.view.util.Button_Insignificant import *

class Dialog_Confirm(Component):
    NAME = 'CONFIRM_DIALOG'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.frame = QFrame(parent)
        self.frame.resize(parent.geometry().width(), parent.geometry().height())
        self.frame.move(0, 0)
        self.frame.setStyleSheet(self.ctx.style_dialog_bg)

        self.panel = QFrame(self.frame)
        self.panel.resize(520, 230)
        self.panel.move(parent.geometry().width() / 2 - 520 / 2, 200)
        self.panel.setStyleSheet(self.ctx.style_dialog_panel)

        self.panel_north = QFrame(self.panel)
        self.panel_north.resize(520, 50)
        self.panel_north.move(0, 0)
        self.panel_north.setStyleSheet(self.ctx.style_dialog_panel)
        self.panel_middle = QFrame(self.panel)
        self.panel_middle.resize(520, 100)
        self.panel_middle.move(0, 50)
        self.panel_middle.setStyleSheet(self.ctx.style_dialog_panel)
        self.panel_south = QFrame(self.panel)
        self.panel_south.resize(520, 80)
        self.panel_south.move(0, 150)
        self.panel_south.setStyleSheet(self.ctx.style_dialog_panel)

        self.label_title = QLabel(self.panel_north)
        self.label_title.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_title.resize(490, 50)
        self.label_title.move(30, 0)
        self.label_title.setStyleSheet(self.ctx.style_label_key)

        self.label_content = QLabel(self.panel_middle)
        self.label_content.setWordWrap(True)
        self.label_content.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_content.resize(490, 100)
        self.label_content.move(30, 0)
        self.label_content.setStyleSheet(self.ctx.style_label_value)

        # btn_confirm
        btn_confirm = Button_General('Yes')
        self.btn_confirm = btn_confirm.init_compo(self.panel_south)
        self.btn_confirm.resize(100, self.ctx.style_btn_general_height)
        self.btn_confirm.move(self.panel_south.geometry().width() - (self.ctx.style_btn_general_space + 100) * 2, 20)
        # btn_cancel
        btn_cancel = Button_Insignificant('No')
        self.btn_cancel = btn_cancel.init_compo(self.panel_south)
        self.btn_cancel.resize(100, self.ctx.style_btn_general_height)
        self.btn_cancel.move(self.panel_south.geometry().width() - self.ctx.style_btn_general_space - 100, 20)

        return self
