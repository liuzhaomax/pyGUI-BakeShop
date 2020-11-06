#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Interceptor_Data.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Authorization data interceptor
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.interceptor.Interceptor import *


class Interceptor_Data(Interceptor):
    NAME = 'INTERCEPTOR_DATA'

    def __init__(self):
        super().__init__()


