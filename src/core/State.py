#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       State.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-08-2020
@LastModified   29-08-2020
@Function       state machine
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Controller import *


class State(Controller):
    NAME = 'STATE'

    def __init__(self):
        super().__init__()
        self.states = {}

    def register_states(self, states_name):
        '''
        Register states
        @param states_name: str
        @return:
        '''
        self.states[states_name] = {}

    def delete_states(self, states_name):
        '''
        Delete states
        @param states_name: str
        @return:
        '''
        if self.states[states_name]:
            del self.states[states_name]

    def get_states(self, states_name):
        '''
        Return states
        @param states_name: str
        @return: self.states[states_name]
        '''
        return self.states[states_name]

    def set_states(self, states_name, val):
        '''
        Set states value
        @param states_name: str
        @param val: dict
        @return:
        '''
        self.states[states_name] = val

    def get_state(self, states_name, state_name):
        '''
        Return state
        @param states_name: str
        @param state_name: str
        @return: self.states[states_name][state_name]
        '''
        return self.states[states_name][state_name]

    def set_state(self, states_name, state_name, val):
        '''
        Set state
        @param states_name: str
        @param state_name: str
        @param val: Router
        @return:
        '''
        if states_name not in self.states:
            self.states[states_name] = {}
        self.states[states_name][state_name] = val

    def set_one_negate_others(self, states_name, state_name, bool, res_obj, func):
        '''
        If a function is activated, other states of the same level of the function will activate the negate functions
        @param states_name: str
        @param state_name: str
        @param bool: bool
        @param res_obj: Component (Component's children)
        @param func: str
        @return:
        '''
        if bool == True or bool == False:
            for kk in res_obj:
                if kk == states_name:
                    for key in res_obj[kk]:
                        if key != state_name:
                            fn = getattr(res_obj[kk][key], func)
                            fn(not bool)
                else:
                    for key in res_obj[kk]:
                        fn = getattr(res_obj[kk][key], func)
                        fn(not bool)
            fn = getattr(res_obj[states_name][state_name], func)
            fn(bool)
        else:
            print('Invalid var bool.')

