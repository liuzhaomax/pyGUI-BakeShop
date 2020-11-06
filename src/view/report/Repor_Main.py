#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Repor_Main.py
@Author         Yue Zhang
@StudId         30976316
@StartDate      30-09-2020
@LastModified   13-10-2020
@Function       Report main page
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.util.Layout_Table import *
from src.view.util.Button_General import *
from src.view.util.Table import *
from src.view.util.Paging import *

class Repor_Main(Component):
    NAME = 'REPORT_MAIN_PAGE'

    def __init__(self):
        super().__init__()
        self.row_len = 20
        self.page_num = 1
        self.current_data = []
        self.current_data_business = []

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.parent = parent
        # layout
        layout_table = Layout_Table()
        self.layout = layout_table.init_compo(parent.main)
        self.layout.main.setVisible(True)
        # btn_inventory (button for showing low inventory)
        btn_inventory = Button_General('Low Inventory')
        self.btn_inventory = btn_inventory.init_compo(self.layout.main_north_west)
        # change the size and move the position
        self.btn_inventory.resize(120, self.ctx.style_btn_general_height)
        self.btn_inventory.move(30, self.ctx.style_btn_general_space)
        # on click function
        self.btn_inventory.clicked.connect(lambda: self.on_click_btn_inventory())

        # btn_business (button for showing bussiness related information)
        btn_business = Button_General('Items Sale')
        self.btn_business = btn_business.init_compo(self.layout.main_north_west)
        # change the size and move the position
        self.btn_business.resize(120, self.ctx.style_btn_general_height)
        self.btn_business.move(180, self.ctx.style_btn_general_space)
        # on click function
        self.btn_business.clicked.connect(lambda: self.on_click_btn_business())

        # combobox for users to choose different store to view
        self.combo_stores = QComboBox(self.layout.main)
        # change the size, move the position and change the general view
        self.combo_stores.resize(450, self.ctx.style_btn_general_height)
        self.combo_stores.move(1080, self.ctx.style_btn_general_space)
        self.combo_stores.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Black))
        #current index change function
        self.combo_stores.currentIndexChanged.connect(self.on_current_index)

        # table_inventory (showing low inventory related information)
        table = Table()
        self.table_inventory = table.init_compo(self.layout.main_middle)
        # table_inventory special style
        self.table_inventory.setRowCount(self.row_len)
        self.table_inventory.setColumnCount(3)
        self.table_inventory.setHorizontalHeaderLabels(['Item ID','Iteam Name','Quantity'])
        self.table_inventory.horizontalHeader().setMinimumWidth(100)
        self.table_inventory.horizontalHeader().setMinimumWidth(100)
        for i in range(3):
            self.table_inventory.horizontalHeader().resizeSection(i, (self.layout.main_middle.geometry().width() - 70) / 3)  # 176   410 is the minimum width of the last cell
        self.table_inventory.horizontalHeader().setStretchLastSection(True)  # cells adapt table width
        # self.table_inventory.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # table_business (showing items sales related information)
        self.table_business = table.init_compo(self.layout.main_middle)
        self.table_business.horizontalHeader().setStretchLastSection(True)  # cells adapt table width
        self.table_business.setVisible(False)
        # table_inventory special style
        self.table_business.setRowCount(18)
        self.table_business.setColumnCount(6)
        self.table_business.setHorizontalHeaderLabels(
            ['Most Popular Coffee', 'Sales', 'Most Popular Coffee beans', 'Sales', 'Most Popular Food', 'Sales'])
        self.table_business.horizontalHeader().setMinimumWidth(100)
        self.table_business.horizontalHeader().setMinimumWidth(100)
        for i in range(6):
            self.table_business.horizontalHeader().resizeSection(i, (
                    self.layout.main_middle.geometry().width() - 70) / 6)
        self.table_business.horizontalHeader().setStretchLastSection(True)  # cells adapt table width
        # self.table_business.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_business.setVisible(False)

        # paging
        paging = Paging()
        self.paging = paging.init_compo(self.layout.main_south)
        self.paging.btn_next.clicked.connect(lambda: self.on_click_btn_next())
        self.paging.btn_prev.clicked.connect(lambda: self.on_click_btn_prev())
        self.paging.btn_prev.setVisible(False)

        return self

    def on_current_index(self):
        '''
        when index changed, the table view will change
        @return:
        '''
        if self.combo_stores.currentIndex() != 0:
            self.init_data_table_report_inventory()
            self.init_data_table_report_business()

    def load_store_list(self, store_list):
        '''
        load each store's information in the combobox
        @param store_list: str
        @return:
        '''
        self.combo_stores.addItems(store_list)

    def init_data_table_report_inventory(self):
        '''
        showing low inventory information in the inventory table
        @return:
        '''
        self.current_data = self.data[0][self.combo_stores.currentIndex() + 1]
        #only onw page, paging not showing
        if self.current_data.__len__() <= self.row_len:
            self.paging.btn_next.setVisible(False)
        #data start in current page
        row_data_start = self.row_len * (self.page_num - 1)
        #the last page
        if self.page_num > int(self.current_data.__len__() / self.row_len):
            row_data_end = self.current_data.__len__()
        #last data in current page(not last page)
        else:
            row_data_end = self.row_len * self.page_num
        for row_num in range(row_data_start, self.row_len * self.page_num):
            if row_num < row_data_end:
                #add data in table
                for i in range(3):
                    newItem = QTableWidgetItem(self.current_data[row_num][i])
                    newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    newItem.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Black))
                    self.table_inventory.setItem(row_num % self.row_len, i, newItem)
            else:
                break

    def on_click_btn_next(self):
        '''
        turn to next page's view for the table
        @return:
        '''
        self.page_num += 1
        if self.page_num > 1:
            self.paging.btn_prev.setVisible(True)
        if self.page_num >= self.current_data.__len__() / self.row_len and self.data.__len__() % self.row_len >= 0:
            self.paging.btn_next.setVisible(False)
        if self.current_data.__len__() <= self.row_len:
            self.paging.btn_next.setVisible(False)
        self.init_data_table_report_inventory()

    def on_click_btn_prev(self):
        '''
        turn to previous page's view for the table
        @return:
        '''
        self.page_num -= 1
        if self.page_num == 1:
            self.paging.btn_prev.setVisible(False)
        if self.page_num <= self.current_data.__len__() / self.row_len:
            self.paging.btn_next.setVisible(True)
        self.init_data_table_report_inventory()

    def on_click_btn_business(self):
        '''
        when btn_business is clicked, change to business table (inventory info hide)
        @return:
        '''
        self.table_inventory.setVisible(False)
        self.table_business.setVisible(True)
        self.init_data_table_report_business()

    def on_click_btn_inventory(self):
        '''
        when btn_inventory is clicked, change to inventory table (business info hide)
        @return:
        '''
        self.table_business.setVisible(False)
        self.table_inventory.setVisible(True)
        self.init_data_table_report_inventory()

    def init_data_table_report_business(self):
        '''
        show business info in business table
        @return:
        '''
        self.current_data_business = self.data[1][self.combo_stores.currentIndex() + 1]
        #sort the rank for each kinds of items sale
        coffee_rank = sorted(self.current_data_business[3][0].items(), key=lambda x:x[1],reverse=True)
        beans_rank = sorted(self.current_data_business[3][1].items(), key=lambda x:x[1],reverse=True)
        food_rank = sorted(self.current_data_business[3][2].items(), key=lambda x:x[1],reverse=True)
        #show most 15 popular items sepearted by kinds
        for i in range(15):
            if i < coffee_rank.__len__():
                for j in range(2):
                    newItem = QTableWidgetItem(str(coffee_rank[i][j]))
                    newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    newItem.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Black))
                    self.table_business.setItem(i, j, newItem)
            if i < beans_rank.__len__():
                for j in range(2):
                    newItem = QTableWidgetItem(str(beans_rank[i][j]))
                    newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    newItem.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Black))
                    self.table_business.setItem(i, j+2, newItem)
            if i < food_rank.__len__():
                for j in range(2):
                    newItem = QTableWidgetItem(str(food_rank[i][j]))
                    newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    newItem.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Black))
                    self.table_business.setItem(i, j+4, newItem)
        #change table layout for showing other infomations
        self.table_business.setSpan(15,0,1,6)
        titles = ('Revenue','Coffee sold','Coffee beans sold','Food sold','Days sell most in a week')
        #showing other business information
        for i in range(len(titles)):
            newItem = QTableWidgetItem(titles[i])
            newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            newItem.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Bold))
            self.table_business.setItem(16, i, newItem)
            self.table_business.item(16,i).setBackground(QBrush(QColor(136, 201, 234)))
        self.table_business.setSpan(16,4,1,2)
        weekday = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        contents = (self.current_data_business[0],self.current_data_business[1][0],self.current_data_business[1][1],self.current_data_business[1][2],weekday[self.current_data_business[2]])
        for i in range(len(titles)):
            newItem = QTableWidgetItem(str(contents[i]))
            newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            newItem.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Black))
            self.table_business.setItem(17, i, newItem)
        self.table_business.setSpan(17,4,1,2)





