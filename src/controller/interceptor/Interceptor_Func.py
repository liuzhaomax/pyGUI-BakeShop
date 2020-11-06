#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Interceptor_Func.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Authorization function interceptor
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.interceptor.Interceptor import *

class Interceptor_Func(Interceptor):
    NAME = 'INTERCEPTOR_FUNCTION'

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
        Check permission
        @return:
        '''
        pass
