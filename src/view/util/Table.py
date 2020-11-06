#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Table.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      31-08-2020
@LastModified   31-08-2020
@Function       table component
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Component import *

class Table(Component):
    NAME = 'TABLE'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self.table
        '''
        self.table = QTableWidget(parent)
        self.table.resize(parent.geometry().width() - 60, parent.geometry().height())
        self.table.move(30, 0)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # cells cannot be edited
        self.table.setStyleSheet('background-color: rgba(255, 255, 255, 1); font-family: Microsoft YaHei; color: black;')
        self.table.setStyleSheet('selection-background-color: rgba(58, 166, 221, 0.6);')  # bg color when selected
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.verticalHeader().setVisible(False)  # vertical header set to hidden
        self.table.verticalHeader().setStretchLastSection(True)  # cells adapt table height
        self.table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setFixedHeight(30)
        hori_header_font = self.table.horizontalHeader().font()
        hori_header_font.setBold(True)
        self.table.horizontalHeader().setFont(hori_header_font)  # horizontal header set to bold
        self.table.horizontalHeader().setStyleSheet('::section{background-color: rgba(58, 166, 221, 0.6); border: 1px; font-weight: bold; font-size: 14px; font-family: Microsoft YaHei;}')
        return self.table