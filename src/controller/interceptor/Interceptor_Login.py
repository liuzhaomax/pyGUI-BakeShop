#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Interceptor_Login.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Authorization login interceptor
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.interceptor.Interceptor import *
from src.view.login.Login_Failed_Dialog import *


class Interceptor_Login(Interceptor):
    NAME = 'INTERCEPTOR_LOGIN'

    def __init__(self):
        super().__init__()
        self.denied_dialog_parent = None
        self.dialog = None

    def deny(self):
        '''
        Permission deny
        @return:
        '''
        dialog = Login_Failed_Dialog('Login Failed', 'Your permission is inadequate. Please retype your staff ID and password.')
        self.dialog = dialog.init_compo(self.denied_dialog_parent)
        self.dialog.dialog.frame.setVisible(True)

    def check_permission(self):
        '''
        A non-empty permission is enough
        @return: bool
        '''
        if self.permission == '':
            return False
        else:
            return True

    def set_denied_dialog_parent(self, denied_dialog_parent):
        '''
        Set the denied dialog's parent
        @param denied_dialog_parent: QFrame
        @return:
        '''
        self.denied_dialog_parent = denied_dialog_parent

    def get_denied_dialog_parent(self):
        '''
        Return the denied dialog's parent
        @return: self.denied_dialog_parent
        '''
        return self.denied_dialog_parent


