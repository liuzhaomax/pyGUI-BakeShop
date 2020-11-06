#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Main.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      30-08-2020
@LastModified   02-09-2020
@Function       Order main page
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.order.Order_Create import *
from src.view.order.Order_Delete import *
from src.view.order.Order_View import *
from src.view.order.Order_Modify import *
from src.view.util.Button_General import *
from src.view.util.Table import *
from src.view.util.Layout_Table import *
from src.view.util.Paging import *

class Order_Main(Component):
    NAME = 'ORDER_MAIN_PAGE'

    def __init__(self):
        super().__init__()
        self.header_list = ['Order ID', 'Store ID', 'Staff ID', 'Order Date', 'Order Time', 'Total Cost $', 'Order Type', 'Status', 'Operations']
        self.indices = ['order_id', 'store_id', 'staff_id', 'date', 'time', 'total_cost', 'type', 'status']
        self.row_len = 20
        self.col_len = self.header_list.__len__()
        self.page_num = 1
        self.order_create_bean = None
        self.order_create_common = None
        self.order_view = None
        self.order_modi = None
        self.order_dele = None

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
        # widgets
        # btn_create_common
        btn_create_common = Button_General('Create')
        self.btn_create_common = btn_create_common.init_compo(self.layout.main_north_west)
        self.btn_create_common.resize(100, self.ctx.style_btn_general_height)
        self.btn_create_common.move(30, self.ctx.style_btn_general_space)
        self.btn_create_common.clicked.connect(lambda: self.on_click_btn_create_common())
        # btn_create_bean
        btn_create_bean = Button_General('Create Bean Orders')
        self.btn_create_bean = btn_create_bean.init_compo(self.layout.main_north_west)
        self.btn_create_bean.resize(200, self.ctx.style_btn_general_height)
        self.btn_create_bean.move(160, self.ctx.style_btn_general_space)
        self.btn_create_bean.clicked.connect(lambda: self.on_click_btn_create_bean())
        # paging
        paging = Paging()
        self.paging = paging.init_compo(self.layout.main_south)
        self.paging.btn_next.clicked.connect(lambda: self.on_click_btn_next())
        self.paging.btn_prev.clicked.connect(lambda: self.on_click_btn_prev())
        self.paging.btn_prev.setVisible(False)
        # table_order
        table = Table()
        self.table_order = table.init_compo(self.layout.main_middle)
        # table_order special style
        self.table_order.setRowCount(self.row_len)
        self.table_order.setColumnCount(self.col_len)
        self.table_order.setHorizontalHeaderLabels(self.header_list)
        self.table_order.horizontalHeader().setMinimumWidth(100)
        for i in range(self.col_len - 1):
            self.table_order.horizontalHeader().resizeSection(i, (self.layout.main_middle.geometry().width() - 40 - 410) / (self.col_len - 1)) # 176   410 is the minimum width of the last cell
        self.table_order.horizontalHeader().setStretchLastSection(True)  # cells adapt table width
        # self.table_order.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        return self

    def init_data_table_order(self):
        '''
        Initialise the data on the table
        @return:
        '''
        if self.data.__len__() <= self.row_len:
            self.paging.btn_next.setVisible(False)
        row_data_start = self.row_len * (self.page_num - 1)
        if self.page_num > int(self.data.__len__() / self.row_len):
            row_data_end = self.data.__len__()
        else:
            row_data_end = self.row_len * self.page_num
        for row in range(row_data_start, self.row_len * self.page_num):
            if row < row_data_end:
                for col in range(len(self.indices)):
                    func = getattr(self.data[row], 'get_' +  self.indices[col])
                    str_data = func()
                    item = QTableWidgetItem(str_data)
                    item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    item.setFont(QtGui.QFont('Microsoft YaHei', 13, QtGui.QFont.Black))
                    if self.indices[col] == 'status':
                        item.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                    self.table_order.setItem(row if row_data_start == 0 else row % row_data_start , col, item)
            else:
                for col in range(len(self.indices)):
                    item = QTableWidgetItem('')
                    self.table_order.setItem(row if row_data_start == 0 else row % row_data_start, col, item)
        self.init_row_btn()

    def init_row_btn(self):
        '''
        Initialise the buttons in each row
        @return:
        '''
        for row in range(self.row_len):
            for col in range(self.col_len - 1, self.col_len):
                frame_btn_row = QFrame()
                if (self.page_num - 1) * self.row_len + row < self.data.__len__():
                    self.init_row_btn_view(frame_btn_row)
                    if self.data[(self.page_num - 1) * self.row_len + row].get_status() == 'CONFIRMED':
                        self.init_row_btn_modi(frame_btn_row)
                        self.init_row_btn_dele(frame_btn_row)
                        self.init_row_btn_take(frame_btn_row)
                    elif self.data[(self.page_num - 1) * self.row_len + row].get_status() == 'PREPARING':
                        self.init_row_btn_modi(frame_btn_row)
                        self.init_row_btn_dele(frame_btn_row)
                        self.init_row_btn_finish(frame_btn_row)
                # load frame_btn_row
                self.table_order.setCellWidget(row, col, frame_btn_row)

    def init_row_btn_view(self, parent):
        '''
        Initialise the View button
        @param parent: QFrame
        @return:
        '''
        # btn_row_view
        btn_row_view = QPushButton('View', parent)
        btn_row_view.resize(80, self.ctx.style_btn_table_height)
        btn_row_view.move(self.ctx.style_btn_table_space, 3)
        btn_row_view.setCursor(QtCore.Qt.PointingHandCursor)
        btn_row_view.setStyleSheet(self.ctx.style_btn_table_view)
        btn_row_view.clicked.connect(lambda: self.on_click_btn_row_view(self.table_order))

    def init_row_btn_modi(self, parent):
        '''
        Initialise the Modify button
        @param parent: QFrame
        @return:
        '''
        # btn_row_modi
        btn_row_modi = QPushButton('Modify', parent)
        btn_row_modi.resize(80, self.ctx.style_btn_table_height)
        btn_row_modi.move(self.ctx.style_btn_table_space*2 + 80*1, 3)
        btn_row_modi.setCursor(QtCore.Qt.PointingHandCursor)
        btn_row_modi.setStyleSheet(self.ctx.style_btn_table_modi)
        btn_row_modi.clicked.connect(lambda: self.on_click_btn_row_modi(self.table_order))

    def init_row_btn_dele(self, parent):
        '''
        Initialise the Delete button
        @param parent: QFrame
        @return:
        '''
        # btn_row_dele
        btn_row_dele = QPushButton('Delete', parent)
        btn_row_dele.resize(80, self.ctx.style_btn_table_height)
        btn_row_dele.move(self.ctx.style_btn_table_space*3 + 80*2, 3)
        btn_row_dele.setCursor(QtCore.Qt.PointingHandCursor)
        btn_row_dele.setStyleSheet(self.ctx.style_btn_table_dele)
        btn_row_dele.clicked.connect(lambda: self.on_click_btn_row_dele(self.table_order))

    def init_row_btn_take(self, parent):
        '''
        Initialise the Take button
        @param parent: QFrame
        @return:
        '''
        # btn_row_take
        btn_row_take = QPushButton('Take', parent)
        btn_row_take.resize(80, self.ctx.style_btn_table_height)
        btn_row_take.move(self.ctx.style_btn_table_space*4 + 80*3, 3)
        btn_row_take.setCursor(QtCore.Qt.PointingHandCursor)
        btn_row_take.setStyleSheet(self.ctx.style_btn_table_gene)
        btn_row_take.clicked.connect(lambda: self.on_click_btn_row_take(self.table_order))

    def init_row_btn_finish(self, parent):
        '''
        Initialise the Finish button
        @param parent: QFrame
        @return:
        '''
        # btn_row_take
        btn_row_take = QPushButton('Finish', parent)
        btn_row_take.resize(80, self.ctx.style_btn_table_height)
        btn_row_take.move(self.ctx.style_btn_table_space * 4 + 80 * 3, 3)
        btn_row_take.setCursor(QtCore.Qt.PointingHandCursor)
        btn_row_take.setStyleSheet(self.ctx.style_btn_table_gene)
        btn_row_take.clicked.connect(lambda: self.on_click_btn_row_take(self.table_order))

    def on_click_btn_create_common(self):
        '''
        Callback when the Create button is clicked
        @return:
        '''
        self.order_create_common = Order_Create('common').init_compo(self)
        Component.register_mb(self.layout.main, 'order_main', 'order')
        Component.register_mb(self.order_create_common.layout.main, 'order_create_common', 'order')
        Router('common', 'order', 'order_create_common').do_action()

    def on_click_btn_create_bean(self):
        '''
        Callback when the Create Bean button is clicked
        @return:
        '''
        self.order_create_bean = Order_Create('bean').init_compo(self)
        Component.register_mb(self.layout.main, 'order_main', 'order')
        Component.register_mb(self.order_create_bean.layout.main, 'order_create_bean', 'order')
        Router('common', 'order', 'order_create_bean').do_action()

    def on_click_btn_row_view(self, event_widget):
        '''
        Callback when the View button in each row is clicked
        @param event_widget: QFrame
        @return:
        '''
        pos = event_widget.sender().parent().pos()
        item_index = event_widget.indexAt(pos)
        row = item_index.row()
        self.order_view = Order_View().init_compo(self, row)
        Component.register_mb(self.layout.main, 'order_main', 'order')
        Component.register_mb(self.order_view.layout.main, 'order_view', 'order')
        Router('common', 'order', 'order_view').do_action()

    def on_click_btn_row_modi(self, event_widget):
        '''
        Callback when the Modify button in each row is clicked
        @param event_widget: QFrame
        @return:
        '''
        pos = event_widget.sender().parent().pos()
        item_index = event_widget.indexAt(pos)
        row = item_index.row()
        self.order_modi = Order_Modify().init_compo(self, row)
        Component.register_mb(self.layout.main, 'order_main', 'order')
        Component.register_mb(self.order_modi.layout.main, 'order_modi', 'order')
        Router('common', 'order', 'order_modi').do_action()

    def on_click_btn_row_dele(self, event_widget):
        '''
        Callback when the Delete button in each row is clicked
        @param event_widget: QFrame
        @return:
        '''
        pos = event_widget.sender().parent().pos()
        item_index = event_widget.indexAt(pos)
        row = item_index.row()
        self.order_dele = Order_Delete().init_compo(self, row)
        self.order_dele.dialog.frame.setVisible(True)

    def on_click_btn_row_take(self, event_widget):
        pass

    def on_click_btn_row_finish(self, event_widget):
        pass

    def on_click_btn_next(self):
        '''
        Callback when the Next button is clicked
        @return:
        '''
        self.page_num += 1
        if self.page_num > 1:
            self.paging.btn_prev.setVisible(True)
        if self.page_num >= self.data.__len__() / self.row_len and self.data.__len__() % self.row_len >= 0:
            self.paging.btn_next.setVisible(False)
        if self.data.__len__() <= self.row_len:
            self.paging.btn_next.setVisible(False)
        self.init_data_table_order()

    def on_click_btn_prev(self):
        '''
        Callback when the Prev button is clicked
        @return:
        '''
        self.page_num -= 1
        if self.page_num == 1:
            self.paging.btn_prev.setVisible(False)
        if self.page_num <= self.data.__len__() / self.row_len:
            self.paging.btn_next.setVisible(True)
        self.init_data_table_order()
