#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Component.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-08-2020
@LastModified   04-09-2020
@Function       base class
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.State import *

class Component(Object):
    NAME = 'Component'
    SM = State()
    MAIN_BODIES = {}
    WINDOW = None

    def __init__(self):
        super().__init__()

    def init_compo(self, *args):
        '''
        Abstract init_compo
        '''
        pass

    @staticmethod
    def register_mb(main_body, main_body_name, main_bodies_name):
        '''
        Register main body to MAIN_BODIES
        @param main_body: Component's children
        @param main_body_name: str
        @param main_bodies_name: str
        @return:
        '''
        if main_bodies_name in Component.MAIN_BODIES:
            Component.MAIN_BODIES[main_bodies_name][main_body_name] = main_body
        else:
            Component.MAIN_BODIES[main_bodies_name] = {}
            Component.MAIN_BODIES[main_bodies_name][main_body_name] = main_body

    @staticmethod
    def delete_mb_except(main_bodies_name):
        '''
        Delete the main body except navi
        @param main_bodies_name: str
        @return:
        '''
        keys = []
        for key in Component.MAIN_BODIES:
            if key != main_bodies_name:
                keys.append(key)
        if keys.__len__():
            for item in keys:
                del Component.MAIN_BODIES[item]

    @staticmethod
    def delete_mb():
        '''
        Eliminate MAIN_BODIES
        @return:
        '''
        Component.MAIN_BODIES = {}

    def register_data(self, data):
        '''
        Register data to a view
        @param data: System
        @return:
        '''
        self.data = data