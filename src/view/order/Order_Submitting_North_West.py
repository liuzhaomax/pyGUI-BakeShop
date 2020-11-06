#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Submitting_North_West.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Order submitting page north west panel
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Button_General import *


class Order_Submitting_North_West(Component):
    NAME = 'ORDER_SUBMITTING_PAGE_NORTH_WEST_PANEL'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        # layout_north_west_west
        self.layout_north_west_west = QFrame(parent.layout.main_north_west)
        self.layout_north_west_west.setMinimumWidth(240)
        self.layout_north_west_west.resize(parent.layout.main_north_west.geometry().width() * 1 / 3, parent.layout.main_north_west.geometry().height())
        self.layout_north_west_west.move(0, 0)
        self.layout_north_west_west.setStyleSheet(self.ctx.style_frame)
        # btn_add_an_item
        btn_add_an_item = Button_General('Add an Item')
        self.btn_add_an_item = btn_add_an_item.init_compo(self.layout_north_west_west)
        self.btn_add_an_item.resize(120, self.ctx.style_btn_general_height)
        self.btn_add_an_item.move(30, self.ctx.style_btn_general_space)
        # layout_north_west_east
        self.layout_north_west_east = QFrame(parent.layout.main_north_west)
        self.layout_north_west_west.setMinimumWidth(500)
        self.layout_north_west_east.resize(parent.layout.main_north_west.geometry().width() * 2 / 3, parent.layout.main_north_west.geometry().height())
        self.layout_north_west_east.move(parent.layout.main_north_west.geometry().width() * 1 / 3, 0)
        self.layout_north_west_east.setStyleSheet(self.ctx.style_frame)
        # label_total_cost_label
        self.label_total_cost_label = QLabel(self.layout_north_west_east)
        self.label_total_cost_label.setText('Total Cost:')
        self.label_total_cost_label.setStyleSheet(self.ctx.style_big_label)
        self.label_total_cost_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_total_cost_label.resize(120, parent.layout.main_north_west.geometry().height())
        self.label_total_cost_label.move(self.layout_north_west_east.geometry().width() - 250, 0)
        # label_total_cost_data
        self.label_total_cost_data = QLabel(self.layout_north_west_east)
        self.label_total_cost_data.setText(str(parent.total_cost))
        self.label_total_cost_data.setStyleSheet(self.ctx.style_big_red_label)
        self.label_total_cost_data.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_total_cost_data.resize(100, parent.layout.main_north_west.geometry().height())
        self.label_total_cost_data.move(self.layout_north_west_east.geometry().width() - 130, 0)
        # label_status_label
        self.label_status_label = QLabel(self.layout_north_west_east)
        self.label_status_label.setText('Status:')
        self.label_status_label.setStyleSheet(self.ctx.style_big_label)
        self.label_status_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_status_label.resize(90, parent.layout.main_north_west.geometry().height())
        self.label_status_label.move(self.layout_north_west_east.geometry().width() - 480, 0)
        # label_status_data
        self.label_status_data = QLabel(self.layout_north_west_east)
        self.label_status_data.setText('/')
        self.label_status_data.setStyleSheet(self.ctx.style_big_red_label)
        self.label_status_data.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_status_data.resize(120, parent.layout.main_north_west.geometry().height())
        self.label_status_data.move(self.layout_north_west_east.geometry().width() - 400, 0)
        return self