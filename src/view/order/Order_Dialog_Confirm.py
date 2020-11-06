#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Dialog_Confirm.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      13-09-2020
@LastModified   13-09-2020
@Function       Order confirm dialog
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.order.Handler_Order_Create import *
from src.core.Router import *
from src.view.util.Dialog_Confirm import *

class Order_Dialog_Confirm(Component):
    NAME = 'ORDER_DIALOG_CONFIRM'

    def __init__(self, text_title, text_content):
        super().__init__()
        self.text_title = text_title
        self.text_content = text_content
        self.new_data = None

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.new_data = parent.new_data
        dialog = Dialog_Confirm()
        dialog = dialog.init_compo(parent.bro.parent.main.parent())
        dialog.frame.setVisible(True)
        dialog.label_title.setText(self.text_title)
        dialog.label_content.setText(self.text_content)
        dialog.btn_confirm.setText('Submit')
        dialog.btn_confirm.clicked.connect(lambda: self.on_click_btn_submit(dialog, parent.bro))
        dialog.btn_cancel.clicked.connect(lambda: self.on_click_btn_no(dialog))

    def on_click_btn_submit(self, dialog, bro):
        '''
        Callback when the Submit button is clicked
        @param dialog: Dialog_Confirm
        @param bro: QFrame
        @return:
        '''
        handler_order_create = Handler_Order_Create(self, None)
        handler_order_create.set_model()
        handler_order_create.update_model_data()
        bro.parent.handler_order_main.update_view_data()
        Router('navi', 'navi', 'order').do_action()
        dialog.frame.sender().parent().parent().parent().deleteLater()
        handler_order_create.pop_message_for_submitting_succeed(self.new_data)
        handler_order_create.pop_message_for_bean_order(self.new_data)

    def on_click_btn_no(self, dialog):
        '''
        Callback when the Cancel button is clicked
        @param dialog: Dialog_Confirm
        @return:
        '''
        dialog.frame.close()