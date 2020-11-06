#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Message_Submitting.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      13-09-2020
@LastModified   13-09-2020
@Function       Message Submitting
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Message import *


class Message_Submitting(Component):
    NAME = 'MESSAGE_SUBMITTING'

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
        message = Message()
        self.message = message.init_compo(parent)
        self.message.frame.setVisible(True)
        self.message.label_title.setText(self.text_title)
        self.message.label_content.setText(self.text_content)
        self.message.btn_close.clicked.connect(lambda: self.on_click_btn_close())

    def on_click_btn_close(self):
        '''
        Callback when the button is clicked
        @return:
        '''
        self.message.frame.close()

    def auto_disappear(self, second):
        '''
        Automatically close the message frame in given second
        @param second: int
        @return:
        '''
        QtCore.QTimer().singleShot(second * 1000, self.on_click_btn_close)
