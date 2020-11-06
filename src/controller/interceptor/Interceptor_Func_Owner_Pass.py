#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Interceptor_Func_Owner_Pass.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      26-09-2020
@LastModified   26-09-2020
@Function       Authorization function interceptor owner pass
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.interceptor.Interceptor_Func import *

class Interceptor_Func_Owner_Pass(Interceptor_Func):
    NAME = 'INTERCEPTOR_FUNCTION_OWNER_PASS'

    def __init__(self):
        super().__init__()

    def deny(self):
        '''
        Permission deny
        @return:
        '''
        pass

    def check_permission(self):
        '''
        Only allowing owner permission
        @return: bool
        '''
        if self.permission == 'Owner':
            return True
        else:
            return False
