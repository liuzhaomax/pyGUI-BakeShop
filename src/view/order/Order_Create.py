#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Create.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      02-09-2020
@LastModified   11-09-2020
@Function       Order create order page
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.order.Order_Submitting_Middle import *
from src.view.order.Order_Submitting_North_East import *
from src.view.order.Order_Submitting_North_West import *
from src.view.order.Order_Submitting_South import *
from src.view.order.Order_Dialog_Cancel import *
from src.view.order.Order_Dialog_Confirm import *
from src.view.order.Order_Item_Component import *
from src.view.util.Layout_Form import *
import datetime as dt


class Order_Create(Component):
    NAME = 'ORDER_CREATE_ORDER_PAGE'

    def __init__(self, mode):
        super().__init__()
        self.mode = mode
        self.new_data = []
        self.hbox_layout_item_data_array = []
        self.total_cost = 0.0

    def init_compo(self, bro):
        '''
        Initialise the component
        @param bro: QFrame
        @return: self
        '''
        self.bro = bro
        # layout
        layout_form = Layout_Form()
        self.layout = layout_form.init_compo(bro.parent.main)
        self.layout.main.setVisible(False)
        # widgets: form layout west + form layout east + frame south
        panel_north_west = Order_Submitting_North_West()
        self.panel_north_west = panel_north_west.init_compo(self)
        self.panel_north_west.btn_add_an_item.clicked.connect(lambda: self.on_click_btn_add_an_item())
        panel_north_east = Order_Submitting_North_East()
        self.panel_north_east = panel_north_east.init_compo(self)
        panel_south = Order_Submitting_South()
        self.panel_south = panel_south.init_compo(self)
        self.panel_south.btn_confirm.clicked.connect(lambda: self.on_click_btn_confirm())
        self.panel_south.btn_cancel.clicked.connect(lambda: self.on_click_btn_cancel())
        panel_middle_west = Order_Submitting_Middle()
        self.panel_middle_west = panel_middle_west.init_compo(self, self.layout.main_middle_west)
        self.form_layout_middle_west = self.panel_middle_west.form_layout_middle
        panel_middle_east = Order_Submitting_Middle()
        self.panel_middle_east = panel_middle_east.init_compo(self, self.layout.main_middle_east)
        self.form_layout_middle_east = self.panel_middle_east.form_layout_middle
        # initialise the item layout
        self.on_click_btn_add_an_item()
        return self

    def on_click_btn_add_an_item(self):
        '''
        Callback when the button "Add an item" is clicked
        @return:
        '''
        layout_an_item = Order_Item_Component()
        self.layout_an_item = layout_an_item.init_compo(self)

    def on_click_btn_confirm(self):
        '''
        Call back when the Confirm button is clicked
        @return:
        '''
        format = self.ctx.load_data_label_json()
        handler = Handler_Order_Create(None, None)
        handler.set_model()
        validator = Validator_Order_Submitting.get_instance()
        items_id, items_name, quantity, price, items_name_inexistent, items_name_quantity_inexistent = handler.reform_item_info(self.hbox_layout_item_data_array)
        if validator.is_existing(items_id):
            if not validator.is_existing(items_name_inexistent) and not validator.is_existing(items_name_quantity_inexistent):
                self.new_data.append(format['order'])
                self.new_data[0]['order_id'] = self.ctx.next_order_id
                self.new_data[0]['store_id'] = self.panel_middle_west.label_store_id_data.text()
                self.new_data[0]['staff_id'] = self.ctx.staff_id
                self.new_data[0]['date'] = dt.datetime.now().strftime('%D')
                self.new_data[0]['time'] = dt.datetime.now().strftime('%T')
                self.new_data[0]['cust_name'] = self.panel_north_east.line_cust_name_data.text()
                self.new_data[0]['status'] = 'CONFIRMED'
                self.new_data[0]['items_id'] = items_id
                self.new_data[0]['items_name'] = items_name
                self.new_data[0]['quantity'] = quantity
                self.new_data[0]['price'] = price
                self.new_data[0]['total_cost'] = str(self.total_cost)
                if self.mode == 'bean':
                    self.new_data[0]['cust_phone'] = self.panel_north_east.line_cust_phone_data.text()
                else:
                    self.new_data[0]['cust_phone'] = ''
                if validator.check_before_submitting(self):
                    # total cost confirmation
                    self.layout_an_item.update_total_cost()
                    dialog = Order_Dialog_Confirm('Total Cost Confirmation', 'The total cost of the order: ' + str(self.total_cost))
                    dialog.init_compo(self)
            elif validator.is_existing(items_name_inexistent):
                validator.deny_item_name_not_existed(items_name_inexistent)
            elif validator.is_existing(items_name_quantity_inexistent):
                validator.deny_quantity_not_existed(items_name_quantity_inexistent)
        else:
            validator.deny_no_item_existed()
    
    def on_click_btn_cancel(self):
        '''
        Callback when the Cancel button is clicked
        @return:
        '''
        if self.hbox_layout_item_data_array[0].children()[2].children()[0].text():
            dialog = Order_Dialog_Cancel('Leaving Before Saving Confirmation', 'Are you sure you want to leave this page before saving information entered?')
            dialog.init_compo(self.bro)
        else:
            Router('navi', 'navi', 'order').do_action()
