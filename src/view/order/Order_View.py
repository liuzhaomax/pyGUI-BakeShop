#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_View.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       Order view page
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.core.Router import *
from src.view.util.Button_General import *
from src.view.util.Button_Insignificant import *
from src.view.util.Layout_Form import *

class Order_View(Component):
    NAME = 'ORDER_VIEW_PAGE'

    def __init__(self):
        super().__init__()

    def init_compo(self, bro, row):
        '''
        Initialise the component
        @param bro: QFrame
        @param row: int
        @return: self
        '''
        self.page_num = bro.page_num
        self.row = row
        self.data = bro.data[(bro.page_num - 1) * bro.row_len + row]
        # layout
        layout_form = Layout_Form()
        self.layout = layout_form.init_compo(bro.parent.main)
        self.layout.main.setVisible(False)

        # widgets: form layout west + form layout east + frame south
        # layout_north_west_west
        self.layout_north_west_west = QFrame(self.layout.main_north_west)
        self.layout_north_west_west.setMinimumWidth(240)
        self.layout_north_west_west.resize(self.layout.main_north_west.geometry().width() * 1 / 3, self.layout.main_north_west.geometry().height())
        self.layout_north_west_west.move(0, 0)
        self.layout_north_west_west.setStyleSheet(self.ctx.style_frame)
        # btn_add_an_item
        # btn_add_an_item = Button_General('Add an Item')
        # self.btn_add_an_item = btn_add_an_item.init_compo(self.layout_north_west_west)
        # self.btn_add_an_item.resize(120, self.ctx.style_btn_general_height)
        # self.btn_add_an_item.move(30, self.ctx.style_btn_general_space)
        # self.btn_add_an_item.clicked.connect(lambda: self.on_click_btn_add_an_item())
        # layout_north_west_east
        self.layout_north_west_east = QFrame(self.layout.main_north_west)
        self.layout_north_west_west.setMinimumWidth(500)
        self.layout_north_west_east.resize(self.layout.main_north_west.geometry().width() * 2 / 3, self.layout.main_north_west.geometry().height())
        self.layout_north_west_east.move(self.layout.main_north_west.geometry().width() * 1 / 3, 0)
        self.layout_north_west_east.setStyleSheet(self.ctx.style_frame)
        # label_total_cost_label
        self.label_total_cost_label = QLabel(self.layout_north_west_east)
        self.label_total_cost_label.setText('Total Cost:')
        self.label_total_cost_label.setStyleSheet(self.ctx.style_big_label)
        self.label_total_cost_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_total_cost_label.resize(120, self.layout.main_north_west.geometry().height())
        self.label_total_cost_label.move(self.layout_north_west_east.geometry().width() - 250, 0)
        # label_total_cost_data
        self.label_total_cost_data = QLabel(self.layout_north_west_east)
        self.label_total_cost_data.setText(self.data.get_total_cost())
        self.label_total_cost_data.setStyleSheet(self.ctx.style_big_label)
        self.label_total_cost_data.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_total_cost_data.resize(100, self.layout.main_north_west.geometry().height())
        self.label_total_cost_data.move(self.layout_north_west_east.geometry().width() - 130, 0)
        # label_status_label
        self.label_status_label = QLabel(self.layout_north_west_east)
        self.label_status_label.setText('Status:')
        self.label_status_label.setStyleSheet(self.ctx.style_big_label)
        self.label_status_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_status_label.resize(90, self.layout.main_north_west.geometry().height())
        self.label_status_label.move(self.layout_north_west_east.geometry().width() - 480, 0)
        # label_status_data
        self.label_status_data = QLabel(self.layout_north_west_east)
        self.label_status_data.setText(self.data.get_status())
        self.label_status_data.setStyleSheet(self.ctx.style_big_red_label)
        self.label_status_data.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_status_data.resize(120, self.layout.main_north_west.geometry().height())
        self.label_status_data.move(self.layout_north_west_east.geometry().width() - 400, 0)

        # label_cust_name_label
        self.label_cust_name_label = QLabel(self.layout.main_north_east)
        self.label_cust_name_label.setText('Customer Name:')
        self.label_cust_name_label.setStyleSheet(self.ctx.style_label_key)
        self.label_cust_name_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_cust_name_label.resize(140, self.layout.main_north_east.geometry().height())
        self.label_cust_name_label.move(30, 0)
        # label_cust_name_data
        self.label_cust_name_data = QLabel(self.layout.main_north_east)
        self.label_cust_name_data.setText(self.data.get_cust_name())
        self.label_cust_name_data.setStyleSheet(self.ctx.style_label_value)
        self.label_cust_name_data.setAlignment(QtCore.Qt.AlignVCenter)
        self.label_cust_name_data.resize(self.layout.main_north_east.geometry().width() / 4, 30)
        self.label_cust_name_data.move(170, self.layout.main_north_east.geometry().height()/2-30/2)

        if self.data.get_type() == 'Bean':
            # label_cust_phone_label
            self.label_cust_phone_label = QLabel(self.layout.main_north_east)
            self.label_cust_phone_label.setText('Phone number:')
            self.label_cust_phone_label.setStyleSheet(self.ctx.style_label_key)
            self.label_cust_phone_label.setAlignment(QtCore.Qt.AlignVCenter)
            self.label_cust_phone_label.resize(140, self.layout.main_north_east.geometry().height())
            self.label_cust_phone_label.move(self.layout.main_north_east.geometry().width() / 4 + 230, 0)
            # label_cust_phone_data
            self.label_cust_phone_data = QLabel(self.layout.main_north_east)
            self.label_cust_phone_data.setText(self.data.get_cust_phone())
            self.label_cust_phone_data.setStyleSheet(self.ctx.style_label_value)
            self.label_cust_phone_data.setAlignment(QtCore.Qt.AlignVCenter)
            self.label_cust_phone_data.resize(self.layout.main_north_east.geometry().width() / 4, 30)
            self.label_cust_phone_data.move(self.layout.main_north_east.geometry().width() / 4 + 360, self.layout.main_north_east.geometry().height()/2-30/2)

        # btn_ok
        btn_confirm = Button_General('OK')
        self.btn_confirm = btn_confirm.init_compo(self.layout.main_south)
        self.btn_confirm.resize(100, self.ctx.style_btn_general_height)
        self.btn_confirm.move(self.layout.main_south.geometry().width()/2 - 50, self.ctx.style_btn_general_space)
        self.btn_confirm.clicked.connect(lambda: self.on_click_btn_ok())

        # layout_middle_west
        self.layout_middle_west = QFrame(self.layout.main_middle_west)
        self.layout_middle_west.resize(self.layout.main_middle_west.geometry().width() - 40, self.layout.main_middle_west.geometry().height())
        self.layout_middle_west.move(30, 0)
        self.layout_middle_west.setStyleSheet(self.ctx.style_frame)
        # form_layout_middle_west
        self.form_layout_middle_west = QFormLayout(self.layout_middle_west)
        self.form_layout_middle_west.setSpacing(20)
        self.form_layout_middle_west.setLabelAlignment(QtCore.Qt.AlignRight)
        self.form_layout_middle_west.setFormAlignment(QtCore.Qt.AlignLeft)
        hbox_layout_attr = QHBoxLayout()
        label_order_id_label = QLabel('Order ID:')
        label_order_id_label.setStyleSheet(self.ctx.style_label_key)
        label_order_id_label.setFixedHeight(30)
        label_order_id_data = QLabel(self.data.get_order_id())
        label_order_id_data.setStyleSheet(self.ctx.style_label_value)
        label_order_id_data.setFixedHeight(30)
        label_store_id_label = QLabel('Store ID:')
        label_store_id_label.setStyleSheet(self.ctx.style_label_key)
        label_store_id_label.setFixedHeight(30)
        label_store_id_data = QLabel(self.data.get_store_id())
        label_store_id_data.setStyleSheet(self.ctx.style_label_value)
        label_store_id_data.setFixedHeight(30)
        label_staff_id_label = QLabel('Staff ID:')
        label_staff_id_label.setStyleSheet(self.ctx.style_label_key)
        label_staff_id_label.setFixedHeight(30)
        label_staff_id_data = QLabel(self.data.get_staff_id())
        label_staff_id_data.setStyleSheet(self.ctx.style_label_value)
        label_staff_id_data.setFixedHeight(30)
        label_datetime_label = QLabel('Date-time:')
        label_datetime_label.setStyleSheet(self.ctx.style_label_key)
        label_datetime_label.setFixedHeight(30)
        label_datetime_data = QLabel(self.data.get_date() + ' ' + self.data.get_time())
        label_datetime_data.setStyleSheet(self.ctx.style_label_value)
        label_datetime_data.setFixedHeight(30)
        hbox_layout_attr.addWidget(label_order_id_label)
        hbox_layout_attr.addWidget(label_order_id_data)
        hbox_layout_attr.addWidget(label_store_id_label)
        hbox_layout_attr.addWidget(label_store_id_data)
        hbox_layout_attr.addWidget(label_staff_id_label)
        hbox_layout_attr.addWidget(label_staff_id_data)
        hbox_layout_attr.addWidget(label_datetime_label)
        hbox_layout_attr.addWidget(label_datetime_data)
        hbox_layout_item_label = QHBoxLayout()
        label_item_id_label = QLabel('Item ID')
        label_item_id_label.setStyleSheet(self.ctx.style_label_key)
        label_item_id_label.setAlignment(QtCore.Qt.AlignCenter)
        label_item_name_label = QLabel('Item Name')
        label_item_name_label.setStyleSheet(self.ctx.style_label_key)
        label_item_name_label.setAlignment(QtCore.Qt.AlignCenter)
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
        self.form_layout_middle_west.addRow(hbox_layout_attr)
        self.form_layout_middle_west.addRow(hbox_layout_item_label)

        # layout_middle_east
        self.layout_middle_east = QFrame(self.layout.main_middle_east)
        self.layout_middle_east.resize(self.layout.main_middle_east.geometry().width() - 40, self.layout.main_middle_east.geometry().height())
        self.layout_middle_east.move(30, 0)
        self.layout_middle_east.setStyleSheet(self.ctx.style_frame)
        # form_layout_middle_east
        self.form_layout_middle_east = QFormLayout(self.layout_middle_east)
        self.form_layout_middle_east.setSpacing(20)
        self.form_layout_middle_east.setLabelAlignment(QtCore.Qt.AlignRight)
        self.form_layout_middle_east.setFormAlignment(QtCore.Qt.AlignLeft)
        hbox_layout_attr = QLabel()
        hbox_layout_attr.setFixedHeight(30)
        hbox_layout_item_label = QHBoxLayout()
        label_item_id_label = QLabel('Item ID')
        label_item_id_label.setStyleSheet(self.ctx.style_label_key)
        label_item_id_label.setAlignment(QtCore.Qt.AlignCenter)
        label_item_name_label = QLabel('Item Name')
        label_item_name_label.setStyleSheet(self.ctx.style_label_key)
        label_item_name_label.setAlignment(QtCore.Qt.AlignCenter)
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
        self.form_layout_middle_east.addRow(hbox_layout_attr)
        self.form_layout_middle_east.addRow(hbox_layout_item_label)

        self.hbox_layout_item_data_array = []
        self.load_items()
        return self

    def load_items(self):
        '''
        Load the items into the FE
        @return:
        '''
        items_name = []
        quantity = []
        price = []
        for element in self.data.get_list_of_items():
            items_name.append(element.get_item_name())
            quantity.append(self.data.get_quantities()[element.get_item_id()])
            price.append(element.get_price())
        for i in range(items_name.__len__()):
            # frame for one item
            layout_an_item = QFrame()
            layout_an_item.resize(self.form_layout_middle_west.geometry().width(), 70)
            layout_an_item.move(0, 0)
            layout_an_item.setStyleSheet(self.ctx.style_frame)
            # hbox for one item
            hbox_layout_item_data = QHBoxLayout(layout_an_item)
            # label_item_id_data
            frame_label_item_id_data = QFrame()
            frame_label_item_id_data.setFixedHeight(30)
            frame_label_item_id_data.setStyleSheet(self.ctx.style_frame)
            label_item_id_data = QLabel('I-001', frame_label_item_id_data)
            label_item_id_data.setFixedSize(100, 30)
            label_item_id_data.move(60, 0)
            label_item_id_data.setStyleSheet(self.ctx.style_label_value)
            # line_item_name_data
            frame_line_item_name_data = QFrame()
            frame_line_item_name_data.setFixedHeight(30)
            frame_line_item_name_data.setStyleSheet(self.ctx.style_frame)
            label_item_name_data = QLabel(items_name[i], frame_line_item_name_data)
            label_item_name_data.setFixedSize(200, 30)
            label_item_name_data.move(60, 0)
            label_item_name_data.setStyleSheet(self.ctx.style_label_value)
            #line_item_quan_data
            frame_line_item_quan_data = QFrame()
            frame_line_item_quan_data.setFixedHeight(30)
            frame_line_item_quan_data.setStyleSheet(self.ctx.style_frame)
            label_item_quan_data = QLabel(quantity[i], frame_line_item_quan_data)
            label_item_quan_data.setAlignment(QtCore.Qt.AlignCenter)
            label_item_quan_data.setFixedSize(80, 30)
            label_item_quan_data.move(45, 0)
            label_item_quan_data.setStyleSheet(self.ctx.style_label_value)
            # label_item_price_data
            frame_line_item_price_data = QFrame()
            frame_line_item_price_data.setFixedHeight(30)
            frame_line_item_price_data.setStyleSheet(self.ctx.style_frame)
            label_item_price_data = QLabel(price[i], frame_line_item_price_data)
            label_item_price_data.setAlignment(QtCore.Qt.AlignRight)
            label_item_price_data.setFixedSize(100, 30)
            label_item_price_data.move(15, 5)
            label_item_price_data.setStyleSheet(self.ctx.style_label_value)
            # add and stretch
            hbox_layout_item_data.addWidget(frame_label_item_id_data)
            hbox_layout_item_data.addWidget(frame_line_item_name_data)
            hbox_layout_item_data.addWidget(frame_line_item_quan_data)
            hbox_layout_item_data.addWidget(frame_line_item_price_data)
            hbox_layout_item_data.setStretchFactor(frame_label_item_id_data, 1)
            hbox_layout_item_data.setStretchFactor(frame_line_item_name_data, 2)
            hbox_layout_item_data.setStretchFactor(frame_line_item_quan_data, 1)
            hbox_layout_item_data.setStretchFactor(frame_line_item_price_data, 1)
            # control the quantity of hboxes
            max = 9
            if self.hbox_layout_item_data_array.__len__() < max:
                self.form_layout_middle_west.addRow(layout_an_item)
            elif self.hbox_layout_item_data_array.__len__() >= max and self.hbox_layout_item_data_array.__len__() < max*2:
                self.form_layout_middle_east.addRow(layout_an_item)
            self.hbox_layout_item_data_array.append(layout_an_item)

    def on_click_btn_ok(self):
        '''
        Callback when the OK button is clicked
        @return:
        '''
        Router('navi', 'navi', 'order').do_action()
