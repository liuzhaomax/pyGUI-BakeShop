#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       App.py
@Author         Zhao Liu, Yue Zhang
@StudId         30822750, 30976316
@StartDate      20-08-2020
@LastModified   21-10-2020
@Function       application main entrance
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.Handler_Navi import *
from src.controller.handler.Handler_South_Panel import *
from src.model.entity.inventory.Inventory import *
from src.view.login.Login import *
from src.view.navi.Navi import *
from src.app.Main_Body import *
from src.controller.interceptor.Interceptor_Login import *
from src.model.Model_Staff import *
from src.model.Model_Store import *
from src.model.Model_Order import *
from src.model.entity.System import *
from src.model.entity.item.Item_Bean import *
from src.model.entity.item.Item_Coffee import *
from src.model.entity.item.Item_Food import *
from src.model.entity.item.Item_Material import *
from src.model.entity.order.Order_Common import *
from src.model.entity.order.Order_Bean import *
from src.model.entity.staff.Staff_Owner import *
from src.model.entity.staff.Staff_Manager import *
from src.model.entity.staff.Staff_General import *
from src.model.entity.store.Store import *


class App(QMainWindow, Component, Controller):
    NAME = 'App'
    interceptor = Interceptor_Login.get_instance()

    def __init__(self):
        super().__init__()
        self.navi = None
        self.south_panel = None
        self.permission = ''

    def init_window(self):
        '''
        Initilise the window
        @return:
        '''
        self.resize(1600, 1024) # 1600*1024 1920*1080
        self.setWindowTitle(self.ctx.app_name)
        self.setObjectName("MainWindow")
        self.setStyleSheet(self.ctx.style_bg_image)
        screen = QDesktopWidget().screenGeometry()
        self.move((screen.width() - self.geometry().width()) / 2, (screen.height() - self.geometry().height()) / 2) # center
        # window
        self.window = QWidget()
        self.window.setMinimumSize(800, 600)
        self.setCentralWidget(self.window)
        Component.WINDOW = self.window
        # data
        data = self.init_data()
        # login
        self.display_login(data)
        Interceptor_Login.get_instance().register_observer(self)

    def set_permission(self, permission):
        '''
        Listening the permission changing
        @param permission: str
        @return:
        '''
        prev_permission = self.permission
        self.permission = permission
        interceptor = Interceptor_Login.get_instance()
        if prev_permission:
            self.login.main.setVisible(True)
            self.south_panel.main.setVisible(False)
            self.navi.bar.setVisible(False)
        else:
            if interceptor.check_permission():
                self.login.main.setVisible(False)
            interceptor.set_denied_dialog_parent(self.window)
            self.display_content()

    def display_login(self, data):
        '''
        Displaying login page
        @param data: System
        @return:
        '''
        # login
        login = Login()
        login_handler = Handler_Login(login, data)
        self.login = login_handler.update_view_data(self.window)

    @interceptor.do_check_before(interceptor, 'check_permission', interceptor, 'deny')
    def display_content(self):
        '''
        Displaying the main page
        @return:
        '''
        # main body
        south_panel = Main_Body()
        south_panel_handler = Handler_South_Panel(south_panel, None)
        self.south_panel = south_panel_handler.update_view_data(self.window)
        self.south_panel.main.setVisible(True)
        # navi
        navi = Navi()
        navi_handler = Handler_Navi(navi, None)
        self.navi = navi_handler.update_view_data(self.window)
        self.navi.bar.setVisible(True)
        # login succeed message
        message = Message_Submitting('Login Succeed', f'Welcome, {self.login.staff.get_staff_name()}.')
        message.init_compo(Component.WINDOW)
        message.auto_disappear(2)

    def init_data(self):
        '''
        Initialise the data
        @return: system_data
        '''
        # reading
        model_store = Model_Store.get_model(self.ctx.data_file_name, 'stores')
        model_store.read_excel()
        model_store.transform_for_system()
        df_store = model_store.table
        model_staff = Model_Staff.get_model(self.ctx.data_file_name, 'users')
        model_staff.read_excel()
        model_staff.transform_for_system()
        df_staff = model_staff.table
        model_order = Model_Order.get_model(self.ctx.data_file_name, 'orders')
        model_order.read_excel()
        model_order.transform_for_system()
        df_order = model_order.table
        model_inven = Model_Inven.get_model(self.ctx.data_file_name, 'inventory')
        model_inven.read_excel()
        model_inven.transform_for_system()
        df_inven = model_inven.table
        # next_order_id
        self.ctx.next_order_id = str(int(df_order['order_id'][0]) + 1)
        # allocating
        system_data = System()
        # form Store entities
        for i in range(df_store.shape[0]):
            store = Store()
            for k in df_store.columns:
                if hasattr(store, k):
                    func = getattr(store, 'set_' + k)
                    func(df_store[k][i])
            inventory = Inventory()
            store.set_inventory(inventory)
            system_data.get_list_of_stores().append(store)
        # form Staff entities
        for i in range(df_staff.shape[0]):
            staff_owner = Staff_Owner()
            staff_manager = Staff_Manager()
            staff_general = Staff_General()
            if df_staff['type'][i] == 'Owner':
                for k in df_staff.columns:
                    if hasattr(staff_owner, k):
                        func = getattr(staff_owner, 'set_' + k)
                        func(df_staff[k][i])
            if df_staff['type'][i] == 'Manager':
                for k in df_staff.columns:
                    if hasattr(staff_manager, k):
                        func = getattr(staff_manager, 'set_' + k)
                        func(df_staff[k][i])
            if df_staff['type'][i] == 'Staff':
                for k in df_staff.columns:
                    if hasattr(staff_general, k):
                        func = getattr(staff_general, 'set_' + k)
                        func(df_staff[k][i])
            for j in range(system_data.get_list_of_stores().__len__()):
                if staff_owner.get_staff_id():
                    system_data.get_list_of_stores()[j].get_list_of_staff().append(staff_owner)
                if staff_manager.get_staff_id():
                    for element in staff_manager.get_store_id().split('|'):
                        if system_data.get_list_of_stores()[j].store_id == element:
                            system_data.get_list_of_stores()[j].get_list_of_staff().append(staff_manager)
                            break
                    break
                if staff_general.get_staff_id():
                    for element in staff_general.get_store_id().split('|'):
                        if system_data.get_list_of_stores()[j].store_id == element:
                            system_data.get_list_of_stores()[j].get_list_of_staff().append(staff_general)
                            break
                    break
        # form Order entities
        for i in range(df_order.shape[0]):
            order_common = Order_Common()
            order_bean = Order_Bean()
            if df_order['type'][i] == 'Common':
                for k in df_order.columns:
                    if hasattr(order_common, k):
                        func = getattr(order_common, 'set_' + k)
                        func(df_order[k][i])
                self.load_items_in_order(df_order, df_inven, order_common, i)
            if df_order['type'][i] == 'Bean':
                for k in df_order.columns:
                    if hasattr(order_bean, k):
                        func = getattr(order_bean, 'set_' + k)
                        func(df_order[k][i])
                self.load_items_in_order(df_order, df_inven, order_bean, i)
            for j in range(system_data.get_list_of_stores().__len__()):
                if order_common.get_order_id() and system_data.get_list_of_stores()[j].store_id == order_common.get_store_id():
                    system_data.get_list_of_stores()[j].get_list_of_orders().append(order_common)
                    break
                if order_bean.get_order_id() and system_data.get_list_of_stores()[j].store_id == order_bean.get_store_id():
                    system_data.get_list_of_stores()[j].get_list_of_orders().append(order_bean)
                    break
        # form Inventory entities
        for i in range(df_inven.shape[0]):
            item_bean = Item_Bean()
            item_coffee = Item_Coffee()
            item_food = Item_Food()
            item_material = Item_Material()
            if df_inven['type'][i] == 'Bean':
                for k in df_inven.columns:
                    if hasattr(item_bean, k):
                        func = getattr(item_bean, 'set_' + k)
                        func(df_inven[k][i])
            if df_inven['type'][i] == 'Coffee':
                for k in df_inven.columns:
                    if hasattr(item_coffee, k):
                        func = getattr(item_coffee, 'set_' + k)
                        func(df_inven[k][i])
            if df_inven['type'][i] == 'Food':
                for k in df_inven.columns:
                    if hasattr(item_food, k):
                        func = getattr(item_food, 'set_' + k)
                        func(df_inven[k][i])
            if df_inven['type'][i] == 'Material':
                for k in df_inven.columns:
                    if hasattr(item_material, k):
                        func = getattr(item_material, 'set_' + k)
                        func(df_inven[k][i])
            for j in range(system_data.get_list_of_stores().__len__()):
                if df_inven['store_id'][i] == str(j + 1):
                    if item_bean.get_item_id():
                        system_data.get_list_of_stores()[j].get_inventory().get_list_of_items().append(item_bean)
                        system_data.get_list_of_stores()[j].get_inventory().get_quantities()[item_bean.get_item_id()] = df_inven['quantity'][i]
                        system_data.get_list_of_stores()[j].get_inventory().get_dates()[item_bean.get_item_id()] = df_inven['date'][i]
                    if item_coffee.get_item_id():
                        system_data.get_list_of_stores()[j].get_inventory().get_list_of_items().append(item_coffee)
                        system_data.get_list_of_stores()[j].get_inventory().get_quantities()[item_coffee.get_item_id()] = df_inven['quantity'][i]
                        system_data.get_list_of_stores()[j].get_inventory().get_dates()[item_coffee.get_item_id()] = df_inven['date'][i]
                    if item_food.get_item_id():
                        system_data.get_list_of_stores()[j].get_inventory().get_list_of_items().append(item_food)
                        system_data.get_list_of_stores()[j].get_inventory().get_quantities()[item_food.get_item_id()] = df_inven['quantity'][i]
                        system_data.get_list_of_stores()[j].get_inventory().get_dates()[item_food.get_item_id()] = df_inven['date'][i]
                    if item_material.get_item_id():
                        system_data.get_list_of_stores()[j].get_inventory().get_list_of_items().append(item_material)
                        system_data.get_list_of_stores()[j].get_inventory().get_quantities()[item_material.get_item_id()] = df_inven['quantity'][i]
                        system_data.get_list_of_stores()[j].get_inventory().get_dates()[item_material.get_item_id()] = df_inven['date'][i]
        System.set_instance(system_data)
        return system_data

    def load_items_in_order(self, df_order, df_inven, order, i):
        '''
        Load items in order and generate entities
        @param df_order: Dataframe
        @param df_inven: Dataframe
        @param order: Order
        @param i: int
        @return:
        '''
        items_name = df_order['items_name'][i].split(',')
        quantity = df_order['quantity'][i].split(',')
        price = df_order['price'][i].split('|')
        for p in range(items_name.__len__()):
            item_bean = Item_Bean()
            item_coffee = Item_Coffee()
            item_food = Item_Food()
            item_material = Item_Material()
            quantity_key = ''
            quantity_value = ''
            for m in range(df_inven.shape[0]):
                if df_inven['item_name'][m].lower() == items_name[p].strip().lower():
                    if df_inven['type'][m] == 'Bean':
                        for n in df_inven.columns:
                            if hasattr(item_bean, n):
                                func = getattr(item_bean, 'set_' + n)
                                func(df_inven[n][m])
                            if n == 'quantity':
                                quantity_key = item_bean.get_item_id()
                                quantity_value = quantity[p].strip()
                            if n == 'price':
                                item_bean.set_price(price[p].strip())
                    if df_inven['type'][m] == 'Coffee':
                        for n in df_inven.columns:
                            if hasattr(item_coffee, n):
                                func = getattr(item_coffee, 'set_' + n)
                                func(df_inven[n][m])
                            if n == 'quantity':
                                quantity_key = item_coffee.get_item_id()
                                quantity_value = quantity[p].strip()
                            if n == 'price':
                                item_coffee.set_price(price[p].strip())
                    if df_inven['type'][m] == 'Food':
                        for n in df_inven.columns:
                            if hasattr(item_food, n):
                                func = getattr(item_food, 'set_' + n)
                                func(df_inven[n][m])
                            if n == 'quantity':
                                quantity_key = item_food.get_item_id()
                                quantity_value = quantity[p].strip()
                            if n == 'price':
                                item_food.set_price(price[p].strip())
                    if df_inven['type'][m] == 'Material':
                        for n in df_inven.columns:
                            if hasattr(item_material, n):
                                func = getattr(item_material, 'set_' + n)
                                func(df_inven[n][m])
                            if n == 'quantity':
                                quantity_key = item_material.get_item_id()
                                quantity_value = quantity[p].strip()
                            if n == 'price':
                                item_material.set_price(price[p].strip())
                    break
            order.get_quantities()[quantity_key] = quantity_value
            if item_bean.get_item_id():
                order.get_list_of_items().append(item_bean)
            elif item_coffee.get_item_id():
                order.get_list_of_items().append(item_coffee)
            elif item_food.get_item_id():
                order.get_list_of_items().append(item_food)
            elif item_material.get_item_id():
                order.get_list_of_items().append(item_material)

    # responsive layout
    def resizeEvent(self, e):
        '''
        inherit from QMainWindow to deal with the responsive layout by listening the size changing of the window
        @param e: Signal
        @return:
        '''
        # login
        self.login.main.resize(self.window.geometry().width() * 5/7, self.window.geometry().height() - 400)
        self.login.main.move(self.window.geometry().width() * 1/7, 100)
        self.login.north.resize(self.login.main.geometry().width(), 150)
        self.login.south.resize(self.login.main.geometry().width(), self.login.main.geometry().height() - 150)
        self.login.label_app_name.resize(self.login.north.geometry().width(), self.login.north.geometry().height())
        self.login.label_login_zone.resize(self.login.south.geometry().width() * 3/7, self.login.south.geometry().height() - 100)
        self.login.label_login_zone.move(self.login.south.geometry().width() * 2/7, 100)
        self.login.label_login_text.resize(self.login.label_login_zone.geometry().width(), self.login.label_login_zone.geometry().height() * 1/9)
        self.login.label_login_text.move(0, self.login.label_login_zone.geometry().height() * 1/9)
        self.login.line_staff_id.resize(self.login.label_login_zone.geometry().width(), self.login.label_login_zone.geometry().height() * 1/9)
        self.login.line_staff_id.move(0, self.login.label_login_zone.geometry().height() * 3/9)
        self.login.line_password.resize(self.login.label_login_zone.geometry().width(), self.login.label_login_zone.geometry().height() * 1/9)
        self.login.line_password.move(0, self.login.label_login_zone.geometry().height() * 5/9)
        self.login.btn_login.resize(100, self.login.label_login_zone.geometry().height() * 1/9)
        self.login.btn_login.move(self.login.label_login_zone.geometry().width()/2 - 50, self.login.label_login_zone.geometry().height() * 7/9)
        # if App.interceptor.dialog:
        #     App.interceptor.dialog.dialog.frame.resize(self.window.geometry().width(), self.window.geometry().height())
        #     App.interceptor.dialog.dialog.panel.move(self.window.geometry().width() / 2 - 520 / 2, 200)
        if self.navi:
            # navi
            self.navi.bar.resize(self.window.geometry().width(), 60)
            self.navi.btn_navi_logout.move(self.navi.bar.geometry().width() - 140, 0)
            self.navi.btn_navi_profi.move(self.navi.bar.geometry().width() - 200, 0)
        if self.south_panel:
            # south_panel
            self.south_panel.main.resize(self.window.geometry().width(), self.window.geometry().height() - 60)
            # order main
            self.south_panel.order_main.layout.main.resize(self.south_panel.main.geometry().width() - 40, self.south_panel.main.geometry().height() - 60)
            self.south_panel.order_main.layout.main_north.resize(self.south_panel.order_main.layout.main.geometry().width(), self.south_panel.order_main.layout.main.geometry().height() * 1 / 9)
            self.south_panel.order_main.layout.main_middle.resize(self.south_panel.order_main.layout.main.geometry().width(), self.south_panel.order_main.layout.main.geometry().height() * 7 / 9)
            self.south_panel.order_main.layout.main_middle.move(0, self.south_panel.order_main.layout.main.geometry().height() * 1 / 9)
            self.south_panel.order_main.layout.main_south.resize(self.south_panel.order_main.layout.main.geometry().width(), self.south_panel.order_main.layout.main.geometry().height() * 1 / 9)
            self.south_panel.order_main.layout.main_south.move(0, self.south_panel.order_main.layout.main.geometry().height() * 8 / 9)
            self.south_panel.order_main.layout.main_north_west.resize(self.south_panel.order_main.layout.main.geometry().width() * 2 / 3, self.south_panel.order_main.layout.main_north.geometry().height())
            self.south_panel.order_main.layout.main_north_east.resize(self.south_panel.order_main.layout.main.geometry().width() - self.south_panel.order_main.layout.main_north_west.geometry().width(), self.south_panel.order_main.layout.main_north.geometry().height())
            self.south_panel.order_main.layout.main_north_east.move(self.south_panel.order_main.layout.main.geometry().width() * 2 / 3, 0)
            self.south_panel.order_main.table_order.resize(self.south_panel.order_main.layout.main_middle.geometry().width() - 60, self.south_panel.order_main.layout.main_middle.geometry().height())
            self.south_panel.order_main.paging.btn_next.move(self.south_panel.order_main.layout.main_south.geometry().width() - self.ctx.style_btn_general_space * 2 - 100, self.ctx.style_btn_general_space)
            self.south_panel.order_main.paging.btn_prev.move(self.south_panel.order_main.layout.main_south.geometry().width() - self.ctx.style_btn_general_space * 2 - 100 - self.ctx.style_btn_general_space - 100, self.ctx.style_btn_general_space)
            for i in range(self.south_panel.order_main.col_len - 1):
                self.south_panel.order_main.table_order.horizontalHeader().resizeSection(i, (self.south_panel.order_main.layout.main_middle.geometry().width() - 40 - 445) / (self.south_panel.order_main.col_len - 1)) # 176   445 is the minimum width of the last cell
            self.south_panel.order_main.table_order.horizontalHeader().setStretchLastSection(True)  # cells adapt table width
            if self.south_panel.order_main.order_create_bean != None:
                # order create bean
                self.south_panel.order_main.order_create_bean.layout.main.resize(self.south_panel.main.geometry().width() - 40, self.south_panel.main.geometry().height() - 60)
                self.south_panel.order_main.order_create_bean.layout.main_north.resize(self.south_panel.order_main.order_create_bean.layout.main.geometry().width(), self.south_panel.order_main.order_create_bean.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_create_bean.layout.main_middle.resize( self.south_panel.order_main.order_create_bean.layout.main.geometry().width(), self.south_panel.order_main.order_create_bean.layout.main.geometry().height() * 7 / 9)
                self.south_panel.order_main.order_create_bean.layout.main_middle.move(0, self.south_panel.order_main.order_create_bean.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_create_bean.layout.main_south.resize(self.south_panel.order_main.order_create_bean.layout.main.geometry().width(), self.south_panel.order_main.order_create_bean.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_create_bean.layout.main_south.move(0, self.south_panel.order_main.order_create_bean.layout.main.geometry().height() * 8 / 9)
                self.south_panel.order_main.order_create_bean.layout.main_north_west.resize(self.south_panel.order_main.order_create_bean.layout.main_north.geometry().width() / 2, self.south_panel.order_main.order_create_bean.layout.main_north.geometry().height())
                self.south_panel.order_main.order_create_bean.layout.main_north_east.resize(self.south_panel.order_main.order_create_bean.layout.main_north.geometry().width() - self.south_panel.order_main.order_create_bean.layout.main_north_west.geometry().width(), self.south_panel.order_main.order_create_bean.layout.main_north.geometry().height())
                self.south_panel.order_main.order_create_bean.layout.main_north_east.move(self.south_panel.order_main.order_create_bean.layout.main_north.geometry().width() / 2, 0)
                self.south_panel.order_main.order_create_bean.layout.main_middle_west.resize(self.south_panel.order_main.order_create_bean.layout.main_middle.geometry().width() / 2, self.south_panel.order_main.order_create_bean.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_create_bean.layout.main_middle_east.resize(self.south_panel.order_main.order_create_bean.layout.main_middle.geometry().width() - self.south_panel.order_main.order_create_bean.layout.main_middle_west.geometry().width(), self.south_panel.order_main.order_create_bean.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_create_bean.layout.main_middle_east.move(self.south_panel.order_main.order_create_bean.layout.main_middle.geometry().width() / 2, 0)

                self.south_panel.order_main.order_create_bean.panel_south.btn_confirm.move(self.south_panel.order_main.order_create_bean.layout.main_south.geometry().width() / 2 - 115, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_create_bean.panel_south.btn_cancel.move(self.south_panel.order_main.order_create_bean.layout.main_south.geometry().width() / 2 + 15, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_create_bean.panel_north_west.layout_north_west_west.resize(self.south_panel.order_main.order_create_bean.layout.main_north_west.geometry().width() * 1 / 3, self.south_panel.order_main.order_create_bean.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_create_bean.panel_north_west.layout_north_west_east.resize(self.south_panel.order_main.order_create_bean.layout.main_north_west.geometry().width() * 2 / 3, self.south_panel.order_main.order_create_bean.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_create_bean.panel_north_west.layout_north_west_east.move(self.south_panel.order_main.order_create_bean.layout.main_north_west.geometry().width() * 1 / 3, 0)

                self.south_panel.order_main.order_create_bean.panel_north_west.label_total_cost_label.move(self.south_panel.order_main.order_create_bean.panel_north_west.layout_north_west_east.geometry().width() - 250, 0)
                self.south_panel.order_main.order_create_bean.panel_north_west.label_total_cost_data.move(self.south_panel.order_main.order_create_bean.panel_north_west.layout_north_west_east.geometry().width() - 130, 0)
                self.south_panel.order_main.order_create_bean.panel_north_west.label_status_label.move(self.south_panel.order_main.order_create_bean.panel_north_west.layout_north_west_east.geometry().width() - 480, 0)
                self.south_panel.order_main.order_create_bean.panel_north_west.label_status_data.move(self.south_panel.order_main.order_create_bean.panel_north_west.layout_north_west_east.geometry().width() - 400, 0)

                self.south_panel.order_main.order_create_bean.panel_north_east.line_cust_name_data.resize(self.south_panel.order_main.order_create_bean.layout.main_north_east.geometry().width() / 4, 30)
                self.south_panel.order_main.order_create_bean.panel_north_east.line_cust_name_data.move(170, self.south_panel.order_main.order_create_bean.layout.main_north_east.geometry().height() / 2 - 30 / 2)
                self.south_panel.order_main.order_create_bean.panel_north_east.label_cust_phone_label.move(self.south_panel.order_main.order_create_bean.layout.main_north_east.geometry().width() / 4 + 230, 0)
                self.south_panel.order_main.order_create_bean.panel_north_east.line_cust_phone_data.resize(self.south_panel.order_main.order_create_bean.layout.main_north_east.geometry().width() / 4, 30)
                self.south_panel.order_main.order_create_bean.panel_north_east.line_cust_phone_data.move(self.south_panel.order_main.order_create_bean.layout.main_north_east.geometry().width() / 4 + 360, self.south_panel.order_main.order_create_bean.layout.main_north_east.geometry().height() / 2 - 30 / 2)

                self.south_panel.order_main.order_create_bean.panel_middle_west.layout_middle.resize(self.south_panel.order_main.order_create_bean.layout.main_middle_west.geometry().width() - 40, self.south_panel.order_main.order_create_bean.layout.main_middle_west.geometry().height())
                self.south_panel.order_main.order_create_bean.panel_middle_east.layout_middle.resize(self.south_panel.order_main.order_create_bean.layout.main_middle_east.geometry().width() - 40, self.south_panel.order_main.order_create_bean.layout.main_middle_east.geometry().height())

            if self.south_panel.order_main.order_create_common != None:
                # order create common
                self.south_panel.order_main.order_create_common.layout.main.resize(self.south_panel.main.geometry().width() - 40, self.south_panel.main.geometry().height() - 60)
                self.south_panel.order_main.order_create_common.layout.main_north.resize(self.south_panel.order_main.order_create_common.layout.main.geometry().width(), self.south_panel.order_main.order_create_common.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_create_common.layout.main_middle.resize(self.south_panel.order_main.order_create_common.layout.main.geometry().width(), self.south_panel.order_main.order_create_common.layout.main.geometry().height() * 7 / 9)
                self.south_panel.order_main.order_create_common.layout.main_middle.move(0, self.south_panel.order_main.order_create_common.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_create_common.layout.main_south.resize(self.south_panel.order_main.order_create_common.layout.main.geometry().width(), self.south_panel.order_main.order_create_common.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_create_common.layout.main_south.move(0, self.south_panel.order_main.order_create_common.layout.main.geometry().height() * 8 / 9)
                self.south_panel.order_main.order_create_common.layout.main_north_west.resize(self.south_panel.order_main.order_create_common.layout.main_north.geometry().width() / 2, self.south_panel.order_main.order_create_common.layout.main_north.geometry().height())
                self.south_panel.order_main.order_create_common.layout.main_north_east.resize(self.south_panel.order_main.order_create_common.layout.main_north.geometry().width() - self.south_panel.order_main.order_create_common.layout.main_north_west.geometry().width(), self.south_panel.order_main.order_create_common.layout.main_north.geometry().height())
                self.south_panel.order_main.order_create_common.layout.main_north_east.move(self.south_panel.order_main.order_create_common.layout.main_north.geometry().width() / 2, 0)
                self.south_panel.order_main.order_create_common.layout.main_middle_west.resize(self.south_panel.order_main.order_create_common.layout.main_middle.geometry().width() / 2, self.south_panel.order_main.order_create_common.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_create_common.layout.main_middle_east.resize(self.south_panel.order_main.order_create_common.layout.main_middle.geometry().width() - self.south_panel.order_main.order_create_common.layout.main_middle_west.geometry().width(), self.south_panel.order_main.order_create_common.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_create_common.layout.main_middle_east.move(self.south_panel.order_main.order_create_common.layout.main_middle.geometry().width() / 2, 0)

                self.south_panel.order_main.order_create_common.panel_south.btn_confirm.move(self.south_panel.order_main.order_create_common.layout.main_south.geometry().width() / 2 - 115, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_create_common.panel_south.btn_cancel.move(self.south_panel.order_main.order_create_common.layout.main_south.geometry().width() / 2 + 15, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_create_common.panel_north_west.layout_north_west_west.resize(self.south_panel.order_main.order_create_common.layout.main_north_west.geometry().width() * 1 / 3, self.south_panel.order_main.order_create_common.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_create_common.panel_north_west.layout_north_west_east.resize(self.south_panel.order_main.order_create_common.layout.main_north_west.geometry().width() * 2 / 3, self.south_panel.order_main.order_create_common.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_create_common.panel_north_west.layout_north_west_east.move(self.south_panel.order_main.order_create_common.layout.main_north_west.geometry().width() * 1 / 3, 0)

                self.south_panel.order_main.order_create_common.panel_north_west.label_total_cost_label.move(self.south_panel.order_main.order_create_common.panel_north_west.layout_north_west_east.geometry().width() - 250, 0)
                self.south_panel.order_main.order_create_common.panel_north_west.label_total_cost_data.move(self.south_panel.order_main.order_create_common.panel_north_west.layout_north_west_east.geometry().width() - 130, 0)
                self.south_panel.order_main.order_create_common.panel_north_west.label_status_label.move(self.south_panel.order_main.order_create_common.panel_north_west.layout_north_west_east.geometry().width() - 480, 0)
                self.south_panel.order_main.order_create_common.panel_north_west.label_status_data.move(self.south_panel.order_main.order_create_common.panel_north_west.layout_north_west_east.geometry().width() - 400, 0)

                self.south_panel.order_main.order_create_common.panel_north_east.line_cust_name_data.resize(self.south_panel.order_main.order_create_common.layout.main_north_east.geometry().width() / 4, 30)
                self.south_panel.order_main.order_create_common.panel_north_east.line_cust_name_data.move(170, self.south_panel.order_main.order_create_common.layout.main_north_east.geometry().height() / 2 - 30 / 2)

                self.south_panel.order_main.order_create_common.panel_middle_west.layout_middle.resize(self.south_panel.order_main.order_create_common.layout.main_middle_west.geometry().width() - 40, self.south_panel.order_main.order_create_common.layout.main_middle_west.geometry().height())
                self.south_panel.order_main.order_create_common.panel_middle_east.layout_middle.resize(self.south_panel.order_main.order_create_common.layout.main_middle_east.geometry().width() - 40, self.south_panel.order_main.order_create_common.layout.main_middle_east.geometry().height())

            if self.south_panel.order_main.order_modi != None:
                # order modify
                self.south_panel.order_main.order_modi.layout.main.resize(self.south_panel.main.geometry().width() - 40, self.south_panel.main.geometry().height() - 60)
                self.south_panel.order_main.order_modi.layout.main_north.resize(self.south_panel.order_main.order_modi.layout.main.geometry().width(), self.south_panel.order_main.order_modi.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_modi.layout.main_middle.resize(self.south_panel.order_main.order_modi.layout.main.geometry().width(), self.south_panel.order_main.order_modi.layout.main.geometry().height() * 7 / 9)
                self.south_panel.order_main.order_modi.layout.main_middle.move(0, self.south_panel.order_main.order_modi.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_modi.layout.main_south.resize(self.south_panel.order_main.order_modi.layout.main.geometry().width(), self.south_panel.order_main.order_modi.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_modi.layout.main_south.move(0, self.south_panel.order_main.order_modi.layout.main.geometry().height() * 8 / 9)
                self.south_panel.order_main.order_modi.layout.main_north_west.resize(self.south_panel.order_main.order_modi.layout.main_north.geometry().width() / 2, self.south_panel.order_main.order_modi.layout.main_north.geometry().height())
                self.south_panel.order_main.order_modi.layout.main_north_east.resize(self.south_panel.order_main.order_modi.layout.main_north.geometry().width() - self.south_panel.order_main.order_modi.layout.main_north_west.geometry().width(), self.south_panel.order_main.order_modi.layout.main_north.geometry().height())
                self.south_panel.order_main.order_modi.layout.main_north_east.move(self.south_panel.order_main.order_modi.layout.main_north.geometry().width() / 2, 0)
                self.south_panel.order_main.order_modi.layout.main_middle_west.resize(self.south_panel.order_main.order_modi.layout.main_middle.geometry().width() / 2, self.south_panel.order_main.order_modi.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_modi.layout.main_middle_east.resize(self.south_panel.order_main.order_modi.layout.main_middle.geometry().width() - self.south_panel.order_main.order_modi.layout.main_middle_west.geometry().width(), self.south_panel.order_main.order_modi.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_modi.layout.main_middle_east.move(self.south_panel.order_main.order_modi.layout.main_middle.geometry().width() / 2, 0)

                self.south_panel.order_main.order_modi.btn_confirm.move(self.south_panel.order_main.order_modi.layout.main_south.geometry().width() / 2 - 115, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_modi.btn_cancel.move(self.south_panel.order_main.order_modi.layout.main_south.geometry().width() / 2 + 15, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_modi.layout_north_west_west.resize(self.south_panel.order_main.order_modi.layout.main_north_west.geometry().width() * 1 / 3, self.south_panel.order_main.order_modi.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_modi.layout_north_west_east.resize(self.south_panel.order_main.order_modi.layout.main_north_west.geometry().width() * 2 / 3, self.south_panel.order_main.order_modi.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_modi.layout_north_west_east.move(self.south_panel.order_main.order_modi.layout.main_north_west.geometry().width() * 1 / 3, 0)

                self.south_panel.order_main.order_modi.label_total_cost_label.move(self.south_panel.order_main.order_modi.layout_north_west_east.geometry().width() - 250, 0)
                self.south_panel.order_main.order_modi.label_total_cost_data.move(self.south_panel.order_main.order_modi.layout_north_west_east.geometry().width() - 130, 0)
                self.south_panel.order_main.order_modi.label_status_label.move(self.south_panel.order_main.order_modi.layout_north_west_east.geometry().width() - 480, 0)
                self.south_panel.order_main.order_modi.label_status_data.move(self.south_panel.order_main.order_modi.layout_north_west_east.geometry().width() - 400, 0)

                self.south_panel.order_main.order_modi.line_cust_name_data.resize(self.south_panel.order_main.order_modi.layout.main_north_east.geometry().width() / 4, 30)
                self.south_panel.order_main.order_modi.line_cust_name_data.move(170, self.south_panel.order_main.order_modi.layout.main_north_east.geometry().height() / 2 - 30 / 2)
                if self.south_panel.order_main.order_modi.data['cust_phone'] != 'nan':
                    self.south_panel.order_main.order_modi.label_cust_phone_label.move(self.south_panel.order_main.order_modi.layout.main_north_east.geometry().width() / 4 + 230, 0)
                    self.south_panel.order_main.order_modi.line_cust_phone_data.resize(self.south_panel.order_main.order_modi.layout.main_north_east.geometry().width() / 4, 30)
                    self.south_panel.order_main.order_modi.line_cust_phone_data.move(self.south_panel.order_main.order_modi.layout.main_north_east.geometry().width() / 4 + 360, self.south_panel.order_main.order_modi.layout.main_north_east.geometry().height() / 2 - 30 / 2)

                self.south_panel.order_main.order_modi.layout_middle_west.resize(self.south_panel.order_main.order_modi.layout.main_middle_west.geometry().width() - 40, self.south_panel.order_main.order_modi.layout.main_middle_west.geometry().height())
                self.south_panel.order_main.order_modi.layout_middle_east.resize(self.south_panel.order_main.order_modi.layout.main_middle_east.geometry().width() - 40, self.south_panel.order_main.order_modi.layout.main_middle_east.geometry().height())

            if self.south_panel.order_main.order_view != None:
                # order view
                self.south_panel.order_main.order_view.layout.main.resize(self.south_panel.main.geometry().width() - 40, self.south_panel.main.geometry().height() - 60)
                self.south_panel.order_main.order_view.layout.main_north.resize(self.south_panel.order_main.order_view.layout.main.geometry().width(), self.south_panel.order_main.order_view.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_view.layout.main_middle.resize(self.south_panel.order_main.order_view.layout.main.geometry().width(), self.south_panel.order_main.order_view.layout.main.geometry().height() * 7 / 9)
                self.south_panel.order_main.order_view.layout.main_middle.move(0, self.south_panel.order_main.order_view.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_view.layout.main_south.resize(self.south_panel.order_main.order_view.layout.main.geometry().width(), self.south_panel.order_main.order_view.layout.main.geometry().height() * 1 / 9)
                self.south_panel.order_main.order_view.layout.main_south.move(0, self.south_panel.order_main.order_view.layout.main.geometry().height() * 8 / 9)
                self.south_panel.order_main.order_view.layout.main_north_west.resize(self.south_panel.order_main.order_view.layout.main_north.geometry().width() / 2, self.south_panel.order_main.order_view.layout.main_north.geometry().height())
                self.south_panel.order_main.order_view.layout.main_north_east.resize(self.south_panel.order_main.order_view.layout.main_north.geometry().width() - self.south_panel.order_main.order_view.layout.main_north_west.geometry().width(), self.south_panel.order_main.order_view.layout.main_north.geometry().height())
                self.south_panel.order_main.order_view.layout.main_north_east.move(self.south_panel.order_main.order_view.layout.main_north.geometry().width() / 2, 0)
                self.south_panel.order_main.order_view.layout.main_middle_west.resize(self.south_panel.order_main.order_view.layout.main_middle.geometry().width() / 2, self.south_panel.order_main.order_view.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_view.layout.main_middle_east.resize(self.south_panel.order_main.order_view.layout.main_middle.geometry().width() - self.south_panel.order_main.order_view.layout.main_middle_west.geometry().width(), self.south_panel.order_main.order_view.layout.main_middle.geometry().height())
                self.south_panel.order_main.order_view.layout.main_middle_east.move(self.south_panel.order_main.order_view.layout.main_middle.geometry().width() / 2, 0)

                self.south_panel.order_main.order_view.btn_confirm.move(self.south_panel.order_main.order_view.layout.main_south.geometry().width() / 2 - 115, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_view.btn_cancel.move(self.south_panel.order_main.order_view.layout.main_south.geometry().width() / 2 + 15, self.ctx.style_btn_general_space)
                self.south_panel.order_main.order_view.layout_north_west_west.resize(self.south_panel.order_main.order_view.layout.main_north_west.geometry().width() * 1 / 3, self.south_panel.order_main.order_view.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_view.layout_north_west_east.resize(self.south_panel.order_main.order_view.layout.main_north_west.geometry().width() * 2 / 3, self.south_panel.order_main.order_view.layout.main_north_west.geometry().height())
                self.south_panel.order_main.order_view.layout_north_west_east.move(self.south_panel.order_main.order_view.layout.main_north_west.geometry().width() * 1 / 3, 0)

                self.south_panel.order_main.order_view.label_total_cost_label.move(self.south_panel.order_main.order_view.layout_north_west_east.geometry().width() - 250, 0)
                self.south_panel.order_main.order_view.label_total_cost_data.move(self.south_panel.order_main.order_view.layout_north_west_east.geometry().width() - 130, 0)
                self.south_panel.order_main.order_view.label_status_label.move(self.south_panel.order_main.order_view.layout_north_west_east.geometry().width() - 480, 0)
                self.south_panel.order_main.order_view.label_status_data.move(self.south_panel.order_main.order_view.layout_north_west_east.geometry().width() - 400, 0)

                self.south_panel.order_main.order_view.line_cust_name_data.resize(self.south_panel.order_main.order_view.layout.main_north_east.geometry().width() / 4, 30)
                self.south_panel.order_main.order_view.line_cust_name_data.move(170, self.south_panel.order_main.order_view.layout.main_north_east.geometry().height() / 2 - 30 / 2)
                if self.south_panel.order_main.order_view.data['cust_phone'] != 'nan':
                    self.south_panel.order_main.order_view.label_cust_phone_label.move(self.south_panel.order_main.order_view.layout.main_north_east.geometry().width() / 4 + 230, 0)
                    self.south_panel.order_main.order_view.line_cust_phone_data.resize(self.south_panel.order_main.order_view.layout.main_north_east.geometry().width() / 4, 30)
                    self.south_panel.order_main.order_view.line_cust_phone_data.move(self.south_panel.order_main.order_view.layout.main_north_east.geometry().width() / 4 + 360, self.south_panel.order_main.order_view.layout.main_north_east.geometry().height() / 2 - 30 / 2)

                self.south_panel.order_main.order_view.layout_middle_west.resize(self.south_panel.order_main.order_view.layout.main_middle_west.geometry().width() - 40, self.south_panel.order_main.order_view.layout.main_middle_west.geometry().height())
                self.south_panel.order_main.order_view.layout_middle_east.resize(self.south_panel.order_main.order_view.layout.main_middle_east.geometry().width() - 40, self.south_panel.order_main.order_view.layout.main_middle_east.geometry().height())

            if self.south_panel.order_main.order_dele != None:
                # order view
                self.south_panel.order_main.order_dele.dialog.frame.resize(self.window.geometry().width(), self.window.geometry().height())
                self.south_panel.order_main.order_dele.dialog.panel.move(self.window.geometry().width() / 2 - 520 / 2, 200)

            # report_main responsive design
            # main layout
            self.south_panel.repor_main.layout.main.resize(self.south_panel.main.geometry().width() - 40,
                                                           self.south_panel.main.geometry().height() - 60)
            self.south_panel.repor_main.layout.main_north.resize(
                self.south_panel.order_main.layout.main.geometry().width(),
                self.south_panel.order_main.layout.main.geometry().height() * 1 / 9)
            self.south_panel.repor_main.layout.main_middle.resize(
                self.south_panel.order_main.layout.main.geometry().width(),
                self.south_panel.order_main.layout.main.geometry().height() * 7 / 9)
            self.south_panel.repor_main.layout.main_middle.move(0,
                                                                self.south_panel.order_main.layout.main.geometry().height() * 1 / 9)
            self.south_panel.repor_main.layout.main_south.resize(
                self.south_panel.repor_main.layout.main.geometry().width(),
                self.south_panel.repor_main.layout.main.geometry().height() * 1 / 9)
            self.south_panel.repor_main.layout.main_south.move(0,
                                                               self.south_panel.order_main.layout.main.geometry().height() * 8 / 9)
            self.south_panel.repor_main.layout.main_north_west.resize(
                self.south_panel.repor_main.layout.main.geometry().width() * 2 / 3,
                self.south_panel.repor_main.layout.main_north.geometry().height())
            self.south_panel.repor_main.layout.main_north_east.resize(
                self.south_panel.repor_main.layout.main.geometry().width() - self.south_panel.order_main.layout.main_north_west.geometry().width(),
                self.south_panel.repor_main.layout.main_north.geometry().height())
            self.south_panel.repor_main.layout.main_north_east.move(
                self.south_panel.repor_main.layout.main.geometry().width() * 2 / 3, 0)
            # responsive design for inventory table
            self.south_panel.repor_main.table_inventory.resize(
                self.south_panel.repor_main.layout.main_middle.geometry().width() - 60,
                self.south_panel.repor_main.layout.main_middle.geometry().height())
            for i in range(3):
                self.south_panel.repor_main.table_inventory.horizontalHeader().resizeSection(i, (
                            self.south_panel.repor_main.layout.main_middle.geometry().width() - 70) / 3)
            self.south_panel.repor_main.table_inventory.horizontalHeader().setStretchLastSection(True)  # cells adapt table width
            # self.table_inventory.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            # responsive design for business table
            self.south_panel.repor_main.table_business.resize(
                self.south_panel.repor_main.layout.main_middle.geometry().width() - 60,
                self.south_panel.repor_main.layout.main_middle.geometry().height())
            for i in range(6):
                self.south_panel.repor_main.table_business.horizontalHeader().resizeSection(i, (
                        self.south_panel.repor_main.layout.main_middle.geometry().width() - 70) / 6)
            self.south_panel.repor_main.table_business.horizontalHeader().setStretchLastSection(True)  # cells adapt table width
            # self.table_business.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            # responsive design for paging button
            self.south_panel.repor_main.paging.btn_next.move(
                self.south_panel.repor_main.layout.main_south.geometry().width() - self.ctx.style_btn_general_space * 2 - 100,
                self.ctx.style_btn_general_space)
            self.south_panel.repor_main.paging.btn_prev.move(
                self.south_panel.repor_main.layout.main_south.geometry().width() - self.ctx.style_btn_general_space * 2 - 100 - self.ctx.style_btn_general_space - 100,
                self.ctx.style_btn_general_space)
            self.south_panel.repor_main.combo_stores.move(
                self.south_panel.repor_main.layout.main_south.geometry().width() - self.ctx.style_btn_general_space * 2 - 290 - self.ctx.style_btn_general_space - 100,
                self.ctx.style_btn_general_space)

