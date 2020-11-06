#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Delete.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      06-09-2020
@LastModified   07-09-2020
@Function       Order delete dialog
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Dialog_Confirm import *

class Order_Delete(Component):
    NAME = 'ORDER_DELETE_DIALOG'

    def __init__(self):
        super().__init__()

    def init_compo(self, bro, row):
        '''
        Initialise the component
        @param bro: QFrame
        @param row: int
        @return: self
        '''
        self.bro = bro
        self.page_num = bro.page_num
        self.row = row
        self.data = bro.data[(bro.page_num - 1) * bro.row_len + row]

        dialog = Dialog_Confirm()
        self.dialog = dialog.init_compo(bro.parent.main.parent())
        self.dialog.label_title.setText('Deleting Confirmation')
        self.dialog.label_content.setText('Are you sure you want to delete order (ID):  ' + self.data.get_order_id() + '  ?')
        self.dialog.btn_confirm.clicked.connect(lambda: self.on_click_btn_confirm())
        self.dialog.btn_cancel.clicked.connect(lambda: self.on_click_btn_cancel())
        return self

    def on_click_btn_confirm(self):
        '''
        Callback when the Yes button is clicked
        @return:
        '''
        self.dialog.frame.close()

    def on_click_btn_cancel(self):
        '''
        Callback when the No button is clicked
        @return:
        '''
        self.dialog.frame.close()