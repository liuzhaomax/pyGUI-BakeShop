#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Validator_Numeric.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Validator for numeric
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.validator.Validator import *


class Validator_Numeric(Validator):
    NAME = 'VALIDATOR_NUMERIC'

    def __init__(self):
        super().__init__()

    def is_numerical(self, target):
        '''
        Check if the target is numeric
        @param target: any type
        @return: bool
        '''
        try:
            float(target)
        except:
            return False
        else:
            return True

    def is_numeric_positive(self, target):
        '''
        Check if the target is a positive numeric
        @param target: any type
        @return: bool
        '''
        if self.is_numerical(target):
            if float(target) > 0:
                return True
        else:
            return False

    def is_numeric_positive_integer(self, target):
        '''
        Check if the target is a positive integer
        @param target: any type
        @return: bool
        '''
        if self.is_numerical(target):
            if float(target) == int(float(target)) and int(float(target)) > 0:
                return True
        else:
            return False


