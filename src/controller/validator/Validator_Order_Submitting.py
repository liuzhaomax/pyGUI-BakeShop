#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Validator_Order_Submitting.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Validator for order submitting
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.validator.Validator_Numeric import *
from src.view.order.Order_Dialog_Warning import *
import re


class Validator_Order_Submitting(Validator):
    NAME = 'VALIDATOR_ORDER_SUBMITTING'

    def __init__(self):
        super().__init__()

    def deny_insufficient_quantity(self, sender):
        '''
        Deny handler for insufficient quantity remaining
        @param sender: QLineEdit
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', 'Insufficient quantity for the item in the inventory. Please retype the quantity.')
        dialog.init_compo(Component.WINDOW)
        sender.setText('')

    def deny_incorrect_quantity_format(self, sender):
        '''
        Deny handler for incorrect quantity format
        @param sender: QLineEdit
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', f'Quantity has to be a positive integer. Please re-enter the quantity.')
        dialog.init_compo(Component.WINDOW)
        sender.setText('')

    def deny_item_name_not_existed(self, items_name_inexistent):
        '''
        Deny handler for item name is not existed, and display them
        @param items_name_inexistent: list
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', f'Not existed for the item name: {", ".join(items_name_inexistent)}.')
        dialog.init_compo(Component.WINDOW)

    def deny_quantity_not_existed(self, items_name_quantity_inexistent):
        '''
        Deny handler for item name is existed but quantity is not filled in, and display them
        @param items_name_inexistent: list
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', f'Quantity not entered for the item name: {", ".join(items_name_quantity_inexistent)}.')
        dialog.init_compo(Component.WINDOW)

    def deny_no_item_existed(self):
        '''
        Deny handler for no item exist
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', f'No item in the order.')
        dialog.init_compo(Component.WINDOW)

    def deny_cust_name_empty(self):
        '''
        Deny handler for customer name is empty
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', 'Customer\'s name must be filled in.')
        dialog.init_compo(Component.WINDOW)

    def deny_cust_phone_empty(self):
        '''
        Deny handler for customer phone number is empty
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', 'Customer\' phone number must be filled in.')
        dialog.init_compo(Component.WINDOW)

    def deny_cust_phone_format(self):
        '''
        Deny handler for customer phone number has a wrong format
        @return:
        '''
        dialog = Order_Dialog_Warning('Warning', 'Customer\' phone number can only include + ( ) space and digit.\n'
                                                 'For example: \n'
                                                 '(xx)xxxxxxxx [(2 digits) and 8 digits] (01)12345678\n'
                                                 '+xxxxxxxxxxx [+ and 11 digits] +61123456789\n'
                                                 'xxxxxxxxxx [10 digits] 0123456789')
        dialog.init_compo(Component.WINDOW)

    def check_quantity_remaining(self, quantity_entered, quantity_remaining):
        '''
        Check if the quantity remaining is enough
        @param quantity_entered: str
        @param quantity_remaining: str
        @return: float(quantity_entered) <= float(quantity_remaining) and float(quantity_entered) > 0.0
        '''
        if not quantity_entered:
            quantity_entered = 0
        if not quantity_remaining:
            quantity_remaining = 0
        return float(quantity_entered) <= float(quantity_remaining) and float(quantity_entered) > 0.0

    def check_input_quantity_format(self, quantity, mode):
        '''
        Check if the input quantity is a positive integer
        @param quantity: str
        @param mode: str
        @return: validator_num.is_numeric_positive_integer(quantity)
        '''
        validator_num = Validator_Numeric.get_instance()
        if mode == 'bean':
            return validator_num.is_numeric_positive(quantity)
        return validator_num.is_numeric_positive_integer(quantity)

    def check_cust_name(self, view):
        '''
        Check if the customer name is filled in
        @param view: Order_Create
        @return: bool
        '''
        if view.new_data[0]['cust_name']:
            return True
        return False

    def check_cust_phone(self, view):
        '''
        Check if the customer phone number is filled in
        @param view: Order_Create
        @return: bool
        '''
        if view.mode == 'bean' and not view.new_data[0]['cust_phone']:
            return False
        return True

    def check_cust_phone_format(self, view):
        '''
        Check if the customer phone number is in right format
        customer phone can only include + ( ) space and digit, (xx)xxxxxxxx [8] or +xxxxxxxxxxx [11] or xxxxxxxxxx [10]
        @param view: Order_Create
        @return: bool
        '''
        cust_phone = view.new_data[0]['cust_phone']
        cust_phone = cust_phone.replace(' ', '')
        exp = r'^$|^[\(\d]\d\d[\d\)]\d{8}$|^\d{10}$|^\+\d{11}$'
        reg = re.match(exp, cust_phone)
        if reg:
            return True
        return False

    def check_before_submitting(self, view):
        '''
        Final check function running set
        @param view: Order_Create
        @return: bool
        '''
        if not self.check_cust_name(view):
            self.deny_cust_name_empty()
            return False
        if not self.check_cust_phone(view):
            self.deny_cust_phone_empty()
            return False
        if not self.check_cust_phone_format(view):
            self.deny_cust_phone_format()
            return False
        if (view.new_data[0]['items_id'] and view.new_data[0]['cust_name'] and view.mode != 'bean') \
            or (view.new_data[0]['items_id'] and view.new_data[0]['cust_name'] and view.mode == 'bean' and view.new_data[0]['cust_phone']):
            return True
        return False