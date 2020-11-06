#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Context.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-08-2020
@LastModified   29-08-2020
@Function       utilities
'''''''''''''''''''''''''''''''''''''''''''''''''''
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import json

class Context():
    NAME = 'CONTEXT'

    def __init__(self):
        self.app_name = 'Bake Shop Management System'
        self.store_id = '-1' # assume in store 1
        self.staff_id = '-1' # lztodo need to get login info
        self.next_order_id = '0'
        self.style_bg_image = "#MainWindow{border-image: url(./static/bg.jpg)}"
        self.data_file_name = './static/test.xlsx'
        self.data_label_json_name = './src/config/config.json'
        self.style_mian_body = 'background-color: rgba(255, 255, 255, 0.9);'
        self.style_frame = 'background-color: rgba(0, 0, 0, 0);'
        self.style_navi_bar = 'background-color: rgba(58, 166, 221, 0.6);'
        self.style_btn_navi = 'QPushButton{background-color: rgba(58, 166, 221, 0); border: none; font-size: 22px; font-weight: bold; font-family: Microsoft YaHei; color: white}' \
                              'QPushButton:hover{background-color: rgba(255, 255, 255, 0.3); border: none; font-size: 22px; font-weight: bold; font-family: Microsoft YaHei;}' \
                              'QPushButton:pressed{background-color: rgba(255, 255, 255, 0.3); border: none; font-size: 21px; font-weight: bold; font-family: Microsoft YaHei;}'
        self.style_btn_general = 'QPushButton{background-color: rgba(58, 166, 221, 1); border: none; font-size: 16px; font-weight: bold; font-family: Microsoft YaHei; color: white}' \
                                 'QPushButton:hover{background-color: rgba(58, 166, 221, 0.75); border: none; font-size: 16px; font-weight: bold; font-family: Microsoft YaHei;}' \
                                 'QPushButton:pressed{background-color: rgba(58, 166, 221, 0.75); border: none; font-size: 15px; font-weight: bold; font-family: Microsoft YaHei;}'
        self.style_btn_general_space = 30
        self.style_btn_general_height = 40
        self.style_btn_table_gene = 'QPushButton{background-color: rgba(58, 166, 221, 1); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei; color: white;}' \
                                    'QPushButton:hover{background-color: rgba(58, 166, 221, 0.75); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei;}' \
                                    'QPushButton:pressed{background-color: rgba(58, 166, 221, 0.75); border: none; font-size: 13px; font-weight: bold; font-family: Microsoft YaHei;}'
        self.style_btn_table_view = 'QPushButton{background-color: rgba(25, 190, 107, 1); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei; color: white;}' \
                                    'QPushButton:hover{background-color: rgba(25, 190, 107, 0.75); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei;}' \
                                    'QPushButton:pressed{background-color: rgba(25, 190, 107, 0.75); border: none; font-size: 13px; font-weight: bold; font-family: Microsoft YaHei;}'
        self.style_btn_table_modi = 'QPushButton{background-color: rgba(255, 153, 0, 1); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei; color: white;}' \
                                    'QPushButton:hover{background-color: rgba(255, 153, 0, 0.75); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei;}' \
                                    'QPushButton:pressed{background-color: rgba(255, 153, 0, 0.75); border: none; font-size: 13px; font-weight: bold; font-family: Microsoft YaHei;}'
        self.style_btn_table_dele = 'QPushButton{background-color: rgba(237, 64, 20, 1); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei; color: white;}' \
                                    'QPushButton:hover{background-color: rgba(237, 64, 20, 0.75); border: none; font-size: 14px; font-weight: bold; font-family: Microsoft YaHei;}'\
                                    'QPushButton:pressed{background-color: rgba(237, 64, 20, 0.75); border: none; font-size: 13px; font-weight: bold; font-family: Microsoft YaHei;}'
        self.style_btn_insignificant = 'QPushButton{background-color: white; border: 2px solid rgba(58, 166, 221, 1); font-size: 16px; font-weight: ' \
                                            'bold; font-family: Microsoft YaHei; color: rgba(58, 166, 221, 1);}' \
                                       'QPushButton:hover{background-color: rgba(58, 166, 221, 1); border: 2px solid rgba(58, 166, 221, 1); font-size: 16px; font-weight: ' \
                                            'bold; font-family: Microsoft YaHei; color: white;}' \
                                       'QPushButton:pressed{background-color: rgba(58, 166, 221, 1); border: 2px solid rgba(58, 166, 221, 1); font-size: 15px; font-weight: ' \
                                            'bold; font-family: Microsoft YaHei; color: white;}'
        self.style_btn_login = 'QPushButton{background-color: rgba(58, 166, 221, 1); border: none; font-size: 16px; font-weight: bold; font-family: Microsoft YaHei; color: white;}' \
                               'QPushButton:hover{background-color: rgba(58, 166, 221, 0.75); border: none; font-size: 16px; font-weight: bold; font-family: Microsoft YaHei;}' \
                               'QPushButton:pressed{background-color: rgba(58, 166, 221, 0.75); border: none; font-size: 15px; font-weight: bold; font-family: Microsoft YaHei;}'
        self.style_btn_table_space = 20
        self.style_btn_table_height = 26
        self.style_label_value = 'border: none; font-size: 14px; font-family: Microsoft YaHei; padding: 0px 10px;'
        self.style_label_key = 'border: none; font-size: 14px; font-family: Microsoft YaHei; font-weight: bold;'
        self.style_super_big_label = 'border: none; font-size: 48px; font-family: Microsoft YaHei; background-color: rgba(255, 255, 255, 0.9); border-radius:30px;'
        self.style_login_label = 'border: none; font-size: 20px; font-family: Microsoft YaHei; background-color: rgba(255, 255, 255, 0); padding:0px 20px;'
        self.style_login_line = 'background-color: white; font-size: 14px; font-family: Microsoft YaHei; margin:0px 50px; border-radius:10px; padding: 0px 10px;'
        self.style_big_label = 'border: none; font-size: 20px; font-family: Microsoft YaHei;'
        self.style_big_red_label = 'border: none; font-size: 20px; font-family: Microsoft YaHei; color: red;'
        self.style_line = 'background-color: white; font-size: 14px; font-family: Microsoft YaHei;'
        self.style_dialog_bg = 'background-color: rgba(0, 0, 0, 0.8);'
        self.style_dialog_panel = 'background-color: rgba(255, 255, 255, 1);'
        self.style_list_widget_item_name = 'background-color: white; border: 1px solid black; cursor:pointer'

    @classmethod
    def get_instance(cls):
        '''
        Return the instance of Context
        @return:
        '''
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def load_data_label_json(self):
        '''
        Transform the json to dict
        @return: format
        '''
        file_json = open(self.data_label_json_name, encoding='utf-8')
        format = json.load(file_json)
        file_json.close()
        return format