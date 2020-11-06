#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Submitting_Middle_Item.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Order submitting page middle item panel
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *


class Order_Submitting_Middle_Item(Component):
    NAME = 'ORDER_SUBMITTING_PAGE_MIDDLE_ITEM_PANEL'

    def __init__(self):
        super().__init__()

    def init_compo(self, bro):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        hbox_layout_item_label = QHBoxLayout()
        label_item_id_label = QLabel('Item ID')
        label_item_id_label.setStyleSheet(self.ctx.style_label_key)
        label_item_id_label.setAlignment(QtCore.Qt.AlignCenter)
        label_item_name_label = QLabel('Item Name')
        label_item_name_label.setStyleSheet(self.ctx.style_label_key)
        label_item_name_label.setAlignment(QtCore.Qt.AlignCenter)
        if bro.parent.mode == 'bean':
            label_item_quan_label = QLabel('Quantity (g)')
        else:
            label_item_quan_label = QLabel('Quantity')
        label_item_quan_label.setStyleSheet(self.ctx.style_label_key)
        label_item_quan_label.setAlignment(QtCore.Qt.AlignCenter)
        label_item_price_label = QLabel('Price')
        label_item_price_label.setStyleSheet(self.ctx.style_label_key)
        label_item_price_label.setAlignment(QtCore.Qt.AlignCenter)
        hbox_layout_item_label.addWidget(label_item_id_label)
        hbox_layout_item_label.addWidget(label_item_name_label)
        hbox_layout_item_label.addWidget(label_item_quan_label)
        hbox_layout_item_label.addWidget(label_item_price_label)
        hbox_layout_item_label.setStretchFactor(label_item_id_label, 1)
        hbox_layout_item_label.setStretchFactor(label_item_name_label, 2)
        hbox_layout_item_label.setStretchFactor(label_item_quan_label, 1)
        hbox_layout_item_label.setStretchFactor(label_item_price_label, 1)
        bro.form_layout_middle.addRow(hbox_layout_item_label)
        return self