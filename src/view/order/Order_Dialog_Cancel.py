#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Dialog_Cancel.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      13-09-2020
@LastModified   13-09-2020
@Function       Order cancel dialog
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.order.Handler_Order_Create import *
from src.core.Router import *
from src.view.util.Dialog_Confirm import *

class Order_Dialog_Cancel(Component):
    NAME = 'ORDER_DIALOG_CANCEL'

    def __init__(self, text_title, text_content):
        super().__init__()
        self.text_title = text_title
        self.text_content = text_content

    def init_compo(self, bro):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        dialog = Dialog_Confirm()
        dialog = dialog.init_compo(bro.parent.main.parent())
        dialog.frame.setVisible(True)
        dialog.label_title.setText('Leaving Before Saving Confirmation')
        dialog.label_content.setText('Are you sure you want to leave this page before saving information entered?')
        dialog.btn_confirm.clicked.connect(lambda: self.on_click_btn_yes(dialog))
        dialog.btn_cancel.clicked.connect(lambda: self.on_click_btn_no(dialog))

    def on_click_btn_yes(self, dialog):
        '''
        Callback when the Yes button is clicked
        @param dialog: Dialog_Confirm
        @return:
        '''
        Router('navi', 'navi', 'order').do_action()
        dialog.frame.sender().parent().parent().parent().deleteLater()
        handler_order_create = Handler_Order_Create(None, None)
        handler_order_create.pop_message_for_submitting_canceled()

    def on_click_btn_no(self, dialog):
        '''
        Callback when the No button is clicked
        @param dialog: Dialog_Confirm
        @return:
        '''
        dialog.frame.close()