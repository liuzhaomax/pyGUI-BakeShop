#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Submitting_North_East.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Order Submitting page north east panel
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *


class Order_Submitting_North_East(Component):
    NAME = 'ORDER_SUBMITTING_PAGE_NORTH_EAST_PANEL'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        # label_cust_name_label
        self.label_cust_name_label = QLabel(parent.layout.main_north_east)
        self.label_cust_name_label.setText('Customer Name:')
        self.label_cust_name_label.setStyleSheet(self.ctx.style_label_key)
        self.label_cust_name_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_cust_name_label.resize(140, parent.layout.main_north_east.geometry().height())
        self.label_cust_name_label.move(30, 0)
        # line_cust_name_data
        self.line_cust_name_data = QLineEdit(parent.layout.main_north_east)
        self.line_cust_name_data.setStyleSheet(self.ctx.style_line)
        self.line_cust_name_data.resize(parent.layout.main_north_east.geometry().width() / 4, 30)
        self.line_cust_name_data.move(170, parent.layout.main_north_east.geometry().height()/2-30/2)
        if parent.mode == 'bean':
            # label_cust_phone_label
            self.label_cust_phone_label = QLabel(parent.layout.main_north_east)
            self.label_cust_phone_label.setText('Phone number:')
            self.label_cust_phone_label.setStyleSheet(self.ctx.style_label_key)
            self.label_cust_phone_label.setAlignment(QtCore.Qt.AlignVCenter)
            self.label_cust_phone_label.resize(140, parent.layout.main_north_east.geometry().height())
            self.label_cust_phone_label.move(parent.layout.main_north_east.geometry().width() / 4 + 230, 0)
            # line_cust_phone_data
            self.line_cust_phone_data = QLineEdit(parent.layout.main_north_east)
            self.line_cust_phone_data.setStyleSheet(self.ctx.style_line)
            self.line_cust_phone_data.resize(parent.layout.main_north_east.geometry().width() / 4, 30)
            self.line_cust_phone_data.move(parent.layout.main_north_east.geometry().width() / 4 + 360, parent.layout.main_north_east.geometry().height()/2-30/2)
        return self