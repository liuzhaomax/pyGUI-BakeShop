#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Store.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Store entity
'''''''''''''''''''''''''''''''''''''''''''''''''''

class Store():
    NAME = 'ENTITY_STORE'

    def __init__(self):
        self.store_id = ''
        self.street = ''
        self.city = ''
        self.suburb = ''
        self.postal = ''
        self.phone = ''
        self.list_of_staff = []
        self.list_of_orders = []
        self.inventory = None

    def get_store_id (self):
        '''
        Return store id
        @return: self.store_id
        '''
        return self.store_id

    def get_street(self):
        '''
        Return street
        @return: self.street
        '''
        return self.street

    def get_city(self):
        '''
        Return city
        @return: self.city
        '''
        return self.city

    def get_suburb(self):
        '''
        Return suburb
        @return: self.suburb
        '''
        return self.suburb

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

    def get_list_of_staff(self):
        '''
        Return list of staff
        @return: self.list_of_staff
        '''
        return self.list_of_staff

    def get_list_of_orders(self):
        '''
        Return list of orders
        @return: self.list_of_orders
        '''
        return self.list_of_orders

    def get_inventory(self):
        '''
        Return inventory
        @return: self.inventory
        '''
        return self.inventory

    def set_store_id(self, new_store_id):
        '''
        Set store id
        @param new_store_id: str
        @return:
        '''
        self.store_id = new_store_id

    def set_street(self, new_street):
        '''
        Set street
        @param new_street: str
        @return:
        '''
        self.street = new_street

    def set_city(self, new_city):
        '''
        Set city
        @param new_city: str
        @return:
        '''
        self.city = new_city

    def set_suburb(self, new_suburb):
        '''
        Set suburb
        @param new_suburb: str
        @return:
        '''
        self.suburb = new_suburb

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

    def set_list_of_staff(self, new_list_of_staff):
        '''
        Set list of staff
        @param new_list_of_staff: list
        @return:
        '''
        self.list_of_staff = new_list_of_staff

    def set_list_of_orders(self, new_list_of_orders):
        '''
        Set list of orders
        @param new_list_of_orders: list
        @return:
        '''
        self.list_of_orders = new_list_of_orders

    def set_inventory(self, new_inventory):
        '''
        Set inventory
        @param new_inventory: dict
        @return:
        '''
        self.inventory = new_inventory