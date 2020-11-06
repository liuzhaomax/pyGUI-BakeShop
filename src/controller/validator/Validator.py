#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Validator.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Validator
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Aspect import *

class Validator(Aspect):
    NAME = 'VALIDATOR'

    def __init__(self):
        super().__init__()

    @classmethod
    def get_instance(cls):
        '''
        Return the instance of the class
        @return: cls._instance
        '''
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def is_existing(self, target):
        '''
        Check if the target is existing
        @param target: any type
        @return: bool
        '''
        if target:
            return True
        else:
            return False



