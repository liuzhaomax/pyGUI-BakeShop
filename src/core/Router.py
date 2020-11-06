#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Router.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      30-08-2020
@LastModified   30-08-2020
@Function       Router
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *

class Router(Controller):
    NAME = 'Router'

    def __init__(self, mode, states_name, state_name):
        super().__init__()
        self.mode = mode # navi, common
        self.states_name = states_name
        self.state_name = state_name

    def do_action(self):
        '''
        Route
        @return:
        '''
        self.handle()
        if self.mode == 'navi':
            self.toggle_main_body_navi()
        elif self.mode == 'common':
            self.toggle_main_body_common()
        else:
            print('Invalid mode input')

    def handle(self):
        '''
        Register state to SM
        @return:
        '''
        Component.SM.set_state(self.states_name, self.state_name, self)

    def toggle_main_body_navi(self):
        '''
        Toggle the main body by pressing buttons on navi bar
        @return:
        '''
        Component.SM.set_one_negate_others(self.states_name, self.state_name, True, Component.MAIN_BODIES, 'setVisible')
        Component.delete_mb_except(self.states_name)

    def toggle_main_body_common(self):
        '''
        Toggle the main body by pressing buttons in the main body
        @return:
        '''
        Component.SM.set_one_negate_others(self.states_name, self.state_name, True, Component.MAIN_BODIES, 'setVisible')