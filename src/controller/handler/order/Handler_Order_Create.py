#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Order_Create.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      07-09-2020
@LastModified   07-09-2020
@Function       Handler_Order_Create
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.login.Handler_Login import *
from src.controller.interceptor.Interceptor_Func_Manager_Pass import *
from src.model.Model_Inven import *
from src.model.Model_Order import *
from src.model.entity.System import *
from src.model.entity.order.Order_Bean import *
from src.model.entity.order.Order_Common import *
from src.view.util.Message_Submitting import *


class Handler_Order_Create(Handler):
    NAME = 'HANDLER_ORDER_CREATE'
    interceptor = Interceptor_Func_Manager_Pass.get_instance()

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_model_data(self):
        '''
        Update model data
        @return:
        '''
        new_data = self.view.new_data
        new_order_data, new_quantities_remaining = self.form_new_data()
        new_order_data_transformed = self.model_order.transform_to_excel_axis(new_data)
        new_order_table_to_write = self.model_order.prepare_to_write(new_order_data_transformed)
        new_inven_data_transformed = self.model_inven.transform_to_excel_axis_for_update(new_quantities_remaining)
        new_inven_table_to_write = self.model_inven.prepare_to_update(new_inven_data_transformed)
        try:
            self.model_order.write_excel(new_order_table_to_write)
            self.model_inven.write_excel(new_inven_table_to_write)
        except:
            print('Excel writing failed.')
        else:
            self.update_order_entity(new_order_data)
            self.update_item_entity(new_quantities_remaining)
            self.model_order.read_excel()
            self.model_order.transform_for_system()
            self.model_inven.read_excel()
            self.model_inven.transform_for_system()
            id = int(self.ctx.next_order_id)
            self.ctx.next_order_id = str(id + 1)

    def set_model(self):
        '''
        Set model data
        @return:
        '''
        self.model = System.get_instance()
        self.model_order = Model_Order.get_model(self.ctx.data_file_name, 'orders')
        self.model_inven = Model_Inven.get_model(self.ctx.data_file_name, 'inventory')

    def form_new_data(self):
        '''
        Form new data
        @return: order, new_quantities_remaining
        '''
        if self.view.new_data[0]['cust_phone']:
            order = Order_Bean()
        else:
            order = Order_Common()
        for k in self.view.new_data[0]:
            if hasattr(order, k):
                func = getattr(order, 'set_' + k)
                func(self.view.new_data[0][k])
        items, new_quantities_in_order, new_quantities_remaining = self.form_new_item_data()
        order.set_list_of_items(items)
        order.set_quantities(new_quantities_in_order)
        return order, new_quantities_remaining

    def update_order_entity(self, new_system_data):
        '''
        Update order entity
        @param new_system_data: Order
        @return:
        '''
        for store in System.get_instance().get_list_of_stores():
            if store.get_store_id() == self.ctx.store_id:
                store.get_list_of_orders().append(new_system_data)
                break

    def form_new_item_data(self):
        '''
        Form new item data
        @return: items, new_quantities_in_order, new_quantities_remaining
        '''
        items_name = self.view.new_data[0]['items_name'].split(',')
        quantities = self.view.new_data[0]['quantity'].split(',')
        items = []
        new_quantities_in_order = {}
        new_quantities_remaining = {}
        for i in range(items_name.__len__()):
            item = self.search_item_by_item_name(items_name[i].strip())
            quantity_remaining = self.search_item_quantity_by_item_id(item.get_item_id())
            new_quantity_remaining = str(int(quantity_remaining) - int(quantities[i].strip()))
            items.append(item)
            new_quantities_in_order[item.get_item_id()] = quantities[i].strip()
            new_quantities_remaining[item.get_item_id()] = new_quantity_remaining
        return items, new_quantities_in_order, new_quantities_remaining

    def update_item_entity(self, new_quantities_remaining):
        '''
        Update inventory entity
        @param new_quantities_remaining: dict
        @return:
        '''
        for store in System.get_instance().get_list_of_stores():
            if store.get_store_id() == self.ctx.store_id:
                for key in store.get_inventory().get_quantities():
                    for kk in new_quantities_remaining:
                        if kk == key:
                            store.get_inventory().get_quantities()[key] = new_quantities_remaining[kk]
                            break
                break
    
    def reform_item_info(self, item_row_widget_array):
        '''
        Reform item information for order to write to excel
        @param item_row_widget_array: list
        @return: ', '.join(items_id), ', '.join(items_name), ', '.join(quantity), '|'.join(price), items_name_inexistent, items_name_quantity_inexistent
        '''
        items_id = []
        items_name = []
        quantity = []
        price = []
        items_name_inexistent = []
        items_name_quantity_inexistent = []
        for i in range(len(item_row_widget_array)):
            item_name = item_row_widget_array[i].children()[2].children()[0].text().strip()
            if item_name:
                item = self.search_item_by_item_name(item_name)
                if item:
                    items_id.append(item_row_widget_array[i].children()[1].children()[0].text())
                    items_name.append(item_row_widget_array[i].children()[2].children()[0].text())
                    quantity.append(item_row_widget_array[i].children()[3].children()[0].text())
                    price.append(item_row_widget_array[i].children()[4] .children()[0].text())
                    if not item_row_widget_array[i].children()[3].children()[0].text():
                        items_name_quantity_inexistent.append(item_row_widget_array[i].children()[2].children()[0].text())
                else:
                    item_row_widget_array[i].children()[1].children()[0].setText('')
                    item_row_widget_array[i].children()[3].children()[0].setText('')
                    item_row_widget_array[i].children()[4].children()[0].setText('')
                    items_name_inexistent.append(item_row_widget_array[i].children()[2].children()[0].text())
        return ', '.join(items_id), ', '.join(items_name), ', '.join(quantity), '|'.join(price), items_name_inexistent, items_name_quantity_inexistent

    @interceptor.do_check_before(interceptor, 'check_permission', interceptor, 'deny')
    def pop_message_for_bean_order(self, new_data):
        '''
        Pop message dialog after creating bean order
        @param new_data: list
        @return:
        '''
        if new_data[0]['cust_phone']:
            message = Message_Submitting('Order Creating Succeed', f'The bean order {new_data[0]["order_id"]} has been created successfully.\n'
                                                                   f'Items Name: {new_data[0]["items_name"]}\n'
                                                                   f'Quantities: {new_data[0]["quantity"]}')
            message.init_compo(Component.WINDOW)
            message.auto_disappear(7)

    def pop_message_for_submitting_succeed(self, new_data):
        '''
        Pop message dialog after submitting a new order successfully
        @param new_data: list
        @return:
        '''
        message = Message_Submitting('Order Creating Succeed', f'The order {new_data[0]["order_id"]} has been created successfully.')
        message.init_compo(Component.WINDOW)
        message.auto_disappear(2)

    def pop_message_for_submitting_canceled(self):
        '''
        Pop message dialog after canceling a new order successfully
        @return:
        '''
        message = Message_Submitting('Order Creating Canceled', 'The order creating has been canceled.')
        message.init_compo(Component.WINDOW)
        message.auto_disappear(2)

