#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Login_Failed_Dialog.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Login Failed dialog
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Dialog_Alert import *

class Login_Failed_Dialog(Component):
    NAME = 'LOGIN_FAILED_DIALOG'

    def __init__(self, title, content):
        super().__init__()
        self.title = title
        self.content = content

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        dialog = Dialog_Alert()
        self.dialog = dialog.init_compo(parent)
        self.dialog.frame.setVisible(False)
        self.dialog.label_title.setText(self.title)
        self.dialog.label_content.setText(self.content)
        self.dialog.btn_ok.clicked.connect(lambda: self.on_click_btn_ok())
        return self

    def on_click_btn_ok(self):
        '''
        Callback when the OK button is clicked
        @return:
        '''
        self.dialog.frame.close()