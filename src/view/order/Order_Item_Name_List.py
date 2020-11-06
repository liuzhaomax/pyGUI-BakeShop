#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Item_Name_List.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      13-09-2020
@LastModified   13-09-2020
@Function       Order item name list
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *


class Order_Item_Name_List(Component):
    NAME = 'ORDER_ITEM_NAME_LIST'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.list_widget = QListWidget(parent)  # .parent().parent().parent()
        self.list_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_widget.resize(300, 90)
        self.list_widget.setStyleSheet(self.ctx.style_list_widget_item_name)
        self.list_widget.raise_()
        return self