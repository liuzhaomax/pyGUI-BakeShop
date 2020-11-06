#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Dialog_Warning.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      13-09-2020
@LastModified   13-09-2020
@Function       Order warning dialog
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Dialog_Alert import *

class Order_Dialog_Warning(Component):
    NAME = 'ORDER_DIALOG_WARNING'

    def __init__(self, text_title, text_content):
        super().__init__()
        self.text_title = text_title
        self.text_content = text_content

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        dialog = Dialog_Alert()
        dialog = dialog.init_compo(parent)
        dialog.frame.setVisible(True)
        dialog.label_title.setText(self.text_title)
        dialog.label_content.setText(self.text_content)
        dialog.btn_ok.clicked.connect(lambda: self.on_click_btn_ok(dialog))

    def on_click_btn_ok(self, dialog):
        '''
        Callback when the OK button is clicked
        @param dialog: Dialog_Alert
        @return:
        '''
        dialog.frame.close()