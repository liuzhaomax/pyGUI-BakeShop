#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Login.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       Handler_Login
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *
from src.model.entity.System import *


class Handler_Login(Handler):
    NAME = 'HANDLER_LOGIN'
    permission = ''

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_view_data(self, parent):
        '''
        Update view by adding data
        @return: self.view
        '''
        return self.view.init_compo(parent)

    def get_permission(self):
        '''
        Return the permission
        @return: Handler_Login.permission
        '''
        return Handler_Login.permission

    def set_permission(self, permission):
        '''
        Set the permission
        @param permission: str
        @return:
        '''
        Handler_Login.permission = permission
        self.on_permission_update()

    def on_permission_update(self):
        '''
        Listening the permission update
        @return:
        '''
        for element in self.observers:
            element.set_permission(Handler_Login.permission)

    def match_login_info(self, staff_id, password):
        '''
        Check if the staff_id and the password are matched and existing
        @param staff_id: str
        @param password: str
        @return: Staff or None
        '''
        data = System.get_instance()
        for i in range(data.list_of_stores.__len__()):
            for j in range(data.list_of_stores[i].list_of_staff.__len__()):
                if data.list_of_stores[i].list_of_staff[j].get_staff_id() == staff_id and data.list_of_stores[i].list_of_staff[j].get_password() == password:
                    self.ctx.staff_id = data.list_of_stores[i].list_of_staff[j].get_staff_id()
                    self.ctx.store_id = data.list_of_stores[i].list_of_staff[j].get_store_id()
                    return data.list_of_stores[i].list_of_staff[j]
        return None