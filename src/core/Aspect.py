#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Aspect.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      04-09-2020
@LastModified   07-09-2020
@Function       Aop methods
'''''''''''''''''''''''''''''''''''''''''''''''''''
import functools
from src.core.Controller import *


class Aspect(Controller):
    NAME = 'ASPECT'

    def __init__(self):
        super().__init__()

    def do_before(self, adviser, execution, *params):
        '''
        Run the function decorated after running a function
        @param adviser: Object
        @param execution: str
        @param params: *params
        @return: weave
        '''
        def weave(joint):
            @functools.wraps(joint)
            def wrap(*arg, **kwargs):
                advise = getattr(adviser, execution)
                advise(*params)
                result = joint(*arg, **kwargs)
                return result
            return wrap
        return weave

    def do_after(self, adviser, execution, *params):
        '''
        Run the function decorated before running a function
        @param adviser: Object
        @param execution: str
        @param params: *params
        @return: weave
        '''
        def weave(joint):
            @functools.wraps(joint)
            def wrap(*arg, **kwargs):
                advise = getattr(adviser, execution)
                result = joint(*arg, **kwargs)
                advise(*params)
                return result
            return wrap
        return weave

    def do_around(self, adviser, execution, *params):
        '''
        Run the function decorated before and after running a function
        @param adviser: Object
        @param execution: str
        @param params: *params
        @return: weave
        '''
        def weave(joint):
            @functools.wraps(joint)
            def wrap(*arg, **kwargs):
                advise = getattr(adviser, execution)
                advise(*params)
                result = joint(*arg, **kwargs)
                advise(*params)
                return result
            return wrap
        return weave

    def do_check_before(self, adviser, execution, adviser_deny, execution_deny, *params):
        '''
        Run a checking function before the function decorated
        @param adviser: Object
        @param execution: str
        @param adviser_deny: Object
        @param execution_deny: str
        @param params: *params for adviser
        @return:
        '''
        def weave(joint):
            @functools.wraps(joint)
            def wrap(*arg, **kwargs):
                advise = getattr(adviser, execution)
                if advise(*params):
                    joint(*arg, **kwargs)
                else:
                    advise_deny = getattr(adviser_deny, execution_deny)
                    advise_deny()
            return wrap
        return weave