#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Handler_Repor_Main.py
@Author         Yue Zhang
@StudId         30976316
@StartDate      30-09-2020
@LastModified   13-10-2020
@Function       Handler_Repor_Main
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler import *
import datetime

class Handler_Repor_Main(Handler):
    NAME = 'HANDLER_REPOR_MAIN_PAGE'

    def __init__(self, view, model):
        super().__init__(view, model)

    def update_view_data(self):
        '''
        update view in report model by adding data
        @return: self.view
        '''
        store_list = self.get_store_info()
        self.view.load_store_list(store_list)
        #low inventory related data
        data_inventory = self.search_low_inventory_item()
        #business related data
        data_business = self.searh_last_month_sale(str(datetime.date.today().year),str(datetime.date.today().month))
        # update the data in view
        self.view.register_data([data_inventory,data_business])
        self.view.init_data_table_report_inventory()
        return self.view

    def search_low_inventory_item(self):
        '''
        get the low inventory item data from entity class (inventory)
        @return: low_inventory_infos (list)
        '''
        low_inventory_infos = {}
        for store in self.model.get_list_of_stores():
            inventory = store.get_inventory().get_quantities()
            items = store.get_inventory().get_list_of_items()
            low_inventory_info = []
            for item in items:
                # low inventory = item quantity less than 20
                if (int(inventory[item.get_item_id()]) < 20):
                    low_inventory_info.append([item.get_item_id(), item.get_item_name(), inventory[item.get_item_id()]])
                #sort the list to make users see the low inventory infomation from the lowest quantity left to the highest
                low_inventory_info = sorted(low_inventory_info, key = lambda x: int(x[2]))
            low_inventory_infos[int(store.get_store_id())] = low_inventory_info
        return low_inventory_infos

    def get_store_info(self):
        '''
        get every stores information
        @return: stores (list)
        '''
        stores = []
        for store in self.model.get_list_of_stores():
            store_info = []
            store_info.append('Store ID:')
            store_info.append(store.get_store_id())
            store_info.append('Address:')
            store_info.append(store.get_street())
            store_info.append(store.get_suburb())
            stores.append(' '.join(store_info))
        return stores

    def searh_last_month_sale(self, current_year, current_month):
        '''
        search the sales information (coffee sales, beans sales, food sales, revenue, days sell most, most popular rank for food, coffee and beans)
        @param current_year: str
        @param current_month: str
        @return: last_month_sales (dict)
        '''
        last_month_sales = {}
        for store in self.model.get_list_of_stores():
            orders = store.get_list_of_orders()
            revenue = 0.0
            item_sold = [0,0.0,0]
            sales_info = []
            weekday_sale = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
            item_sale_coffee = {}
            item_sale_bean = {}
            item_sale_food = {}
            for order in orders:
                # select the orders that were ready
                if (order.get_status().find('READY')):
                    # calculate which is the last month (when current month is not Jan)
                    if current_month != '1':
                        if (int(current_month)-1) < 10 :
                            last_month = '0' + str(int(current_month)-1)
                        else:
                            last_month = str(int(current_month)-1)
                    # calculate which is the last month (when current month is Jan)
                    else:
                        last_month = '12'
                        current_year = str(int(current_year) - 1)
                    # select the orders that waere ready in last month
                    if (order.get_date().split("/")[0] == last_month and order.get_date().split("/")[2] == current_year):
                        #calculate revenue
                        revenue += float(order.get_total_cost())
                        #transfor the day from actual date to what weekday it is
                        day = datetime.datetime.strptime(order.get_date(),"%m/%d/%Y").weekday()
                        #calculate the revenue for each day
                        weekday_sale[day] += float(order.get_total_cost())
                        #calculate sales for each kind of items and calculate sales for each item
                        items = order.get_list_of_items()
                        for item in items:
                            if(item.get_type() == 'Food'):
                                item_sold[2] += int(order.get_quantities()[item.get_item_id()])
                                # when the item is already in the key list
                                if item.get_item_name() in item_sale_food.keys():
                                    item_sale_food[item.get_item_name()] += int(order.get_quantities()[item.get_item_id()])
                                # when the item has not been in the key list
                                else:
                                    item_sale_food[item.get_item_name()] = int(order.get_quantities()[item.get_item_id()])
                            if (item.get_type() == 'Bean'):
                                item_sold[1] += float(order.get_quantities()[item.get_item_id()])
                                # when the item is already in the key list
                                if item.get_item_name() in item_sale_bean.keys():
                                    item_sale_bean[item.get_item_name()] += int(
                                        order.get_quantities()[item.get_item_id()])
                                # when the item has not been in the key list
                                else:
                                    item_sale_bean[item.get_item_name()] = float(
                                        order.get_quantities()[item.get_item_id()])
                            if (item.get_type() == 'Coffee'):
                                item_sold[0] += int(order.get_quantities()[item.get_item_id()])
                                # when the item is already in the key list
                                if item.get_item_name() in item_sale_coffee.keys():
                                    item_sale_coffee[item.get_item_name()] += int(
                                        order.get_quantities()[item.get_item_id()])
                                # when the item has not been in the key list
                                else:
                                    item_sale_coffee[item.get_item_name()] = int(
                                        order.get_quantities()[item.get_item_id()])
            sales_info.append(revenue)
            sales_info.append(item_sold)
            sales_info.append(weekday_sale.index(max(weekday_sale)))
            sales_info.append([item_sale_coffee,item_sale_bean,item_sale_food])
            #add all related information
            last_month_sales[int(store.get_store_id())] = sales_info
        return last_month_sales

