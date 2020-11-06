#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Controller.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       Controller base class  
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Object import *


class Controller(Object):
    NAME = 'CONTROLLER'

    def __init__(self):
        super().__init__()
        self.observers = []

    def register_observer(self, observer):
        '''
        Register observer
        @param observer: Object (Object's children)
        @return:
        '''
        self.observers.append(observer)

