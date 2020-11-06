#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Staff.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Staff entity
'''''''''''''''''''''''''''''''''''''''''''''''''''

class Staff():
    NAME = 'ENTITY_STAFF'

    def __init__(self):
        self.staff_id = ''
        self.staff_name = ''
        self.email = ''
        self.password = ''
        self.city = ''
        self.state = ''
        self.postal = ''
        self.phone = ''
        self.store_id = ''

    def get_staff_id (self):
        '''
        Return staff id
        @return: self.staff_id
        '''
        return self.staff_id

    def get_staff_name(self):
        '''
        Return staff name
        @return: self.staff_name
        '''
        return self.staff_name

    def get_email(self):
        '''
        Return email
        @return: self.email
        '''
        return self.email

    def get_password(self):
        '''
        Return password
        @return: self.password
        '''
        return self.password

    def get_city(self):
        '''
        Return city
        @return: self.city
        '''
        return self.city

    def get_state(self):
        '''
        Return state
        @return: self.state
        '''
        return self.state

    def get_postal(self):
        '''
        Return postal
        @return: self.postal
        '''
        return self.postal

    def get_phone(self):
        '''
        Return phone
        @return: self.phone
        '''
        return self.phone

    def get_store_id(self):
        '''
        Return store id
        @return: self.store_id
        '''
        return self.store_id

    def set_staff_id(self, new_staff_id):
        '''
        Set staff id
        @param new_staff_id: str
        @return:
        '''
        self.staff_id = new_staff_id

    def set_staff_name(self, new_staff_name):
        '''
        Set staff name
        @param new_staff_name: str
        @return:
        '''
        self.staff_name = new_staff_name

    def set_email(self, new_email):
        '''
        Set email
        @param new_email: str
        @return:
        '''
        self.email = new_email

    def set_password(self, new_password):
        '''
        Set password
        @param new_password: str
        @return:
        '''
        self.password = new_password

    def set_city(self, new_city):
        '''
        Set city
        @param new_city: str
        @return:
        '''
        self.city = new_city

    def set_state(self, new_state):
        '''
        Set state
        @param new_state: str
        @return:
        '''
        self.state = new_state

    def set_postal(self, new_postal):
        '''
        Set postal
        @param new_postal: str
        @return:
        '''
        self.postal = new_postal

    def set_phone(self, new_phone):
        '''
        Set phone
        @param new_phone: str
        @return:
        '''
        self.phone = new_phone

    def set_store_id(self, new_store_id):
        '''
        Set store id
        @param new_store_id: str
        @return:
        '''
        self.store_id = new_store_id