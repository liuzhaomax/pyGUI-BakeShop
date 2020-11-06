#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Item_Component.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      13-09-2020
@LastModified   13-09-2020
@Function       Order item component
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.order.Handler_Order_Item_Component import *
from src.controller.validator.Validator_Order_Submitting import *
from src.view.order.Order_Item_Name_List import *


class Order_Item_Component(Component):
    NAME = 'ORDER_ITEM_COMPONENT'

    def __init__(self):
        super().__init__()
        self.parent = None
        self.max = 9 # max page capacity of item components
        self.sender_item_name = None
        self.list_widget_items_name_selection_west = None
        self.list_widget_items_name_selection_east = None

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.parent = parent
        # frame for one item
        layout = QFrame()
        layout.resize(parent.form_layout_middle_west.geometry().width(), 70)
        layout.move(0, 0)
        layout.setStyleSheet(self.ctx.style_frame)
        # hbox for one item
        hbox_layout_item_data = QHBoxLayout(layout)
        # label_item_id_data
        frame_label_item_id_data = QFrame()
        frame_label_item_id_data.setFixedHeight(30)
        frame_label_item_id_data.setStyleSheet(self.ctx.style_frame)
        label_item_id_data = QLabel('', frame_label_item_id_data)
        label_item_id_data.setFixedSize(100, 30)
        label_item_id_data.move(60, 0)
        label_item_id_data.setStyleSheet(self.ctx.style_label_value)
        # line_item_name_data
        frame_line_item_name_data = QFrame()
        frame_line_item_name_data.setFixedHeight(30)
        frame_line_item_name_data.setStyleSheet(self.ctx.style_frame)
        line_item_name_data = QLineEdit('', frame_line_item_name_data)
        line_item_name_data.setFixedSize(200, 30)
        line_item_name_data.move(60, 0)
        line_item_name_data.setStyleSheet(self.ctx.style_line)
        line_item_name_data.editingFinished.connect(lambda: self.on_editing_finished_line_item_name_data())
        #line_item_quan_data
        frame_line_item_quan_data = QFrame()
        frame_line_item_quan_data.setFixedHeight(30)
        frame_line_item_quan_data.setStyleSheet(self.ctx.style_frame)
        line_item_quan_data = QLineEdit('', frame_line_item_quan_data)
        line_item_quan_data.setAlignment(QtCore.Qt.AlignCenter)
        line_item_quan_data.setFixedSize(80, 30)
        line_item_quan_data.move(45, 0)
        line_item_quan_data.setStyleSheet(self.ctx.style_line)
        line_item_quan_data.returnPressed.connect(lambda: self.on_return_pressed_line_quantity_data())
        line_item_quan_data.editingFinished.connect(lambda: self.on_editing_finished_line_quantity_data())
        # label_item_price_data
        frame_line_item_price_data = QFrame()
        frame_line_item_price_data.setFixedHeight(30)
        frame_line_item_price_data.setStyleSheet(self.ctx.style_frame)
        label_item_price_data = QLabel('', frame_line_item_price_data)
        label_item_price_data.setFixedSize(100, 30)
        label_item_price_data.setAlignment(QtCore.Qt.AlignRight)
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
        if parent.hbox_layout_item_data_array.__len__() < self.max:
            line_item_name_data.textChanged.connect(lambda: self.on_text_changed_line_item_name_data('west'))
            parent.form_layout_middle_west.addRow(layout)
        elif parent.hbox_layout_item_data_array.__len__() >= self.max and parent.hbox_layout_item_data_array.__len__() < self.max*2:
            line_item_name_data.textChanged.connect(lambda: self.on_text_changed_line_item_name_data('east'))
            parent.form_layout_middle_east.addRow(layout)
        parent.hbox_layout_item_data_array.append(layout)
        # focus
        line_item_name_data.setFocus()

        self.hide_list_widget()
        return self

    def on_text_changed_line_item_name_data(self, flag_sender_orientation):
        '''
        Callback when the input of the item name QLineEdit is changed
        @param flag_sender_orientation: str
        @return:
        '''
        # list view item name
        self.generate_list_widget_items_name_selection(flag_sender_orientation)
        # search item name matched
        items_name_queried_array = self.search_item_name_matched()
        # display item name matched
        self.display_item_name_matched(items_name_queried_array, flag_sender_orientation)

    def generate_list_widget_items_name_selection(self, flag_sender_orientation):
        '''
        Generate a list widget of items names for selection
        @param flag_sender_orientation: str
        @return:
        '''
        self.sender_item_name = self.parent.layout.main_middle.sender()
        distance_v = 60 + self.sender_item_name.parent().x() + self.sender_item_name.parent().parent().x()
        distance_h = 30 + self.sender_item_name.parent().y() + self.sender_item_name.parent().parent().y()
        if flag_sender_orientation == 'west':
            if self.list_widget_items_name_selection_west == None:
                list_widget_items_name_selection_west = Order_Item_Name_List()
                self.list_widget_items_name_selection_west = list_widget_items_name_selection_west.init_compo(self.sender_item_name.parent().parent().parent()).list_widget
                self.list_widget_items_name_selection_west.itemClicked.connect(lambda: self.on_click_list_widget_item())
                self.list_widget_items_name_selection_west.move(distance_v, distance_h)
                self.list_widget_items_name_selection_west.setVisible(True)
                self.list_widget_items_name_selection_west.raise_()
                if self.parent.hbox_layout_item_data_array.__len__() >= self.max and self.sender_item_name.parent().parent() == self.parent.hbox_layout_item_data_array[self.max - 1]:
                    self.list_widget_items_name_selection_west.move(distance_v, distance_h - 30 - 90)
            else:
                self.list_widget_items_name_selection_west.move(distance_v, distance_h)
                self.list_widget_items_name_selection_west.setVisible(True)
                self.list_widget_items_name_selection_west.raise_()
                if self.parent.hbox_layout_item_data_array.__len__() >= self.max and self.sender_item_name.parent().parent() == self.parent.hbox_layout_item_data_array[self.max - 1]:
                    self.list_widget_items_name_selection_west.move(distance_v, distance_h - 30 - 90)
            if self.list_widget_items_name_selection_east:
                self.list_widget_items_name_selection_east.setVisible(False)
        else:
            if self.list_widget_items_name_selection_east == None:
                list_widget_items_name_selection_east = Order_Item_Name_List()
                self.list_widget_items_name_selection_east = list_widget_items_name_selection_east.init_compo(self.sender_item_name.parent().parent().parent()).list_widget
                self.list_widget_items_name_selection_east.itemClicked.connect(lambda: self.on_click_list_widget_item())
                self.list_widget_items_name_selection_east.move(distance_v, distance_h)
                self.list_widget_items_name_selection_east.setVisible(True)
                self.list_widget_items_name_selection_east.raise_()
                if self.parent.hbox_layout_item_data_array.__len__() == self.max * 2 + 1 and self.sender_item_name.parent().parent() == self.parent.hbox_layout_item_data_array[self.max * 2 - 1]:
                    self.list_widget_items_name_selection_east.move(distance_v, distance_h - 30 - 90)
            else:
                self.list_widget_items_name_selection_east.move(distance_v, distance_h)
                self.list_widget_items_name_selection_east.setVisible(True)
                self.list_widget_items_name_selection_east.raise_()
                if self.parent.hbox_layout_item_data_array.__len__() == self.max * 2 + 1 and self.sender_item_name.parent().parent() == self.parent.hbox_layout_item_data_array[self.max * 2 - 1]:
                    self.list_widget_items_name_selection_east.move(distance_v, distance_h - 30 - 90)
            if self.list_widget_items_name_selection_west:
                self.list_widget_items_name_selection_west.setVisible(False)

    def search_item_name_matched(self):
        '''
        Search if the input is matched any item name
        @return: items_name_queried_array
        '''
        handler = Handler_Order_Item_Component(None, System.get_instance())
        text_queried = self.sender_item_name.text()
        items_name_queried_array = handler.search_item_name_matched(self.parent.mode, text_queried)
        return items_name_queried_array

    def display_item_name_matched(self, items_name_queried_array, flag_sender_orientation):
        '''
        Display the items name matched for selection
        @param items_name_queried_array: list
        @param flag_sender_orientation: str
        @return:
        '''
        self.eliminate_list_widget(flag_sender_orientation)
        list_widget_item = QListWidgetItem()
        if items_name_queried_array.__len__() == 0:
            list_widget_item.setText('<No item found>')
            if flag_sender_orientation == 'west':
                self.list_widget_items_name_selection_west.addItem(list_widget_item)
            else:
                self.list_widget_items_name_selection_east.addItem(list_widget_item)
        else:
            for i in range(items_name_queried_array.__len__()):
                list_widget_item = QListWidgetItem()
                list_widget_item.setText(items_name_queried_array[i])
                if flag_sender_orientation == 'west':
                    self.list_widget_items_name_selection_west.addItem(list_widget_item)
                else:
                    self.list_widget_items_name_selection_east.addItem(list_widget_item)

    def eliminate_list_widget(self, flag_sender_orientation):
        '''
        Clear the list widget
        @param flag_sender_orientation: str
        @return:
        '''
        if flag_sender_orientation == 'west':
            self.list_widget_items_name_selection_west.clear()
        else:
            self.list_widget_items_name_selection_east.clear()

    def on_click_list_widget_item(self):
        '''
        Callback when an item name showed in the list widget is clicked
        @return:
        '''
        text = self.parent.layout.main_middle.sender().selectedItems()[0].text()
        self.sender_item_name.setText(text)
        self.hide_list_widget()
        new_item = self.search_item_info(self.sender_item_name.text())
        if new_item != {}:
            self.display_item_info(new_item['item_id'], new_item['price'])

    def on_editing_finished_line_item_name_data(self):
        '''
        Callback when the focus is changed from the QLineEdit of items name to other place
        @return:
        '''
        self.hide_list_widget()
        if self.sender_item_name:
            new_item = self.search_item_info(self.sender_item_name.text())
            if new_item != {}:
                self.display_item_info(new_item['item_id'], new_item['price'])
            else:
                self.display_item_info('', '')
                self.update_total_cost()

    def search_item_info(self, item_name):
        '''
        Search item information when it has been selected
        @param item_name: str
        @return: new_item
        '''
        handler = Handler_Order_Item_Component(None, None)
        handler.set_model()
        item = handler.search_item_by_item_name(item_name)
        new_item = {}
        if item:
            quantity = handler.search_item_quantity_by_item_id(item.get_item_id())
            new_item['item_id'] = item.get_item_id()
            new_item['price'] = item.get_price()
            new_item['quantity_remaining'] = quantity
        return new_item

    def display_item_info(self, item_id, price):
        '''
        Display the item information: id, price
        @param item_id: str
        @param price: str
        @return:
        '''
        self.sender_item_name.parent().parent().children()[1].children()[0].setText(item_id)
        self.sender_item_name.parent().parent().children()[4].children()[0].setText(price)

    def hide_list_widget(self):
        '''
        Hide the list widget of items name
        @return: 
        '''
        if self.list_widget_items_name_selection_west != None:
            self.list_widget_items_name_selection_west.setVisible(False)
        if self.list_widget_items_name_selection_east != None:
            self.list_widget_items_name_selection_east.setVisible(False)

    def update_total_cost(self):
        '''
        Update the total cost
        @return: 
        '''
        total_cost = 0.0
        handler = Handler_Order_Item_Component(None, None)
        for i in range(self.parent.hbox_layout_item_data_array.__len__()):
            quantity_str = self.parent.hbox_layout_item_data_array[i].children()[3].children()[0].text()
            price_str = self.parent.hbox_layout_item_data_array[i].children()[4].children()[0].text()
            total_cost += handler.calculate_cost(quantity_str, price_str)
        total_cost = '%.2f' % total_cost
        self.parent.total_cost = total_cost
        self.parent.panel_north_west.label_total_cost_data.setText(str(self.parent.total_cost))

    def on_return_pressed_line_quantity_data(self):
        '''
        Callback when users press the enter key when the focus is in the QLineEdit of the quantity
        @return: 
        '''
        sender = self.parent.layout.main_middle.sender()
        new_item = self.search_item_info(sender.parent().parent().children()[2].children()[0].text())
        quantity = sender.text()
        if new_item and self.check_input_quantity_format() and quantity:
            if self.check_quantity_remaining(new_item['quantity_remaining']):
                self.parent.on_click_btn_add_an_item()

    def on_editing_finished_line_quantity_data(self):
        '''
        Callback when focus is changed from the QLineEdit of the quantity to other places
        @return:
        '''
        sender = self.parent.layout.main_middle.sender()
        quantity = sender.text()
        if quantity:
            self.handle_check_input_quantity_format()
            prev_total_cost = self.parent.total_cost
            self.update_total_cost()
            if prev_total_cost != self.parent.total_cost:
                self.handle_checking_quantity_remaining()

    def check_input_quantity_format(self):
        '''
        Check if the input quantity is in right format
        @return: bool
        '''
        sender = self.parent.layout.main_middle.sender()
        quantity = sender.text()
        validator = Validator_Order_Submitting.get_instance()
        return validator.check_input_quantity_format(quantity, self.parent.mode)

    def handle_check_input_quantity_format(self):
        '''
        Handle the check_input_quantity_format
        @return:
        '''
        sender = self.parent.layout.main_middle.sender()
        if not self.check_input_quantity_format():
            validator = Validator_Order_Submitting.get_instance()
            validator.deny_incorrect_quantity_format(sender)

    def check_quantity_remaining(self, quantity_remaining):
        '''
        Check if the input quantity is not greater than the quantity remaining
        @param quantity_remaining: str
        @return: bool
        '''
        sender = self.parent.layout.main_middle.sender()
        quantity = sender.text()
        validator = Validator_Order_Submitting.get_instance()
        return validator.check_quantity_remaining(quantity, quantity_remaining)

    def handle_checking_quantity_remaining(self):
        '''
        Handle the check_quantity_remaining function
        @return:
        '''
        sender = self.parent.layout.main_middle.sender()
        new_item = self.search_item_info(sender.parent().parent().children()[2].children()[0].text())
        if new_item:
            if not self.check_quantity_remaining(new_item['quantity_remaining']):
                validator = Validator_Order_Submitting.get_instance()
                validator.deny_insufficient_quantity(sender)
                self.update_total_cost()
