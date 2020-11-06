#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Object.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      08-09-2020
@LastModified   08-09-2020
@Function       Object
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Context import *


class Object():
    NAME = 'OBJECT'

    def __init__(self):
        self.ctx = Context.get_instance()

