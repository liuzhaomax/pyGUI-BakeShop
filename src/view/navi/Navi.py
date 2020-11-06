#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Navi.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      20-08-2020
@LastModified   20-08-2020
@Function       Navi 
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.interceptor.Interceptor_Func_Owner_Pass import *
from src.controller.interceptor.Interceptor_Login import *
from src.core.Router import *
from src.view.util.Button_Navi import *

class Navi(Component):
    NAME = 'NAVIGATION'
    interceptor_owner_pass = Interceptor_Func_Owner_Pass.get_instance()

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.bar = QFrame(parent)
        self.bar.setMinimumSize(800, 60)
        self.bar.resize(parent.geometry().width(), 60)
        self.bar.move(0, 0)
        self.bar.setStyleSheet(self.ctx.style_navi_bar)
        # btn_navi
        self.display_btn_navi_order()
        self.display_btn_navi_inven()
        self.display_btn_navi_repor()
        self.display_btn_navi_staff()

        btn_navi_logout = Button_Navi('Logout')
        self.btn_navi_logout = btn_navi_logout.init_compo(self.bar)
        self.btn_navi_logout.setFixedSize(140, 60)
        self.btn_navi_logout.move(self.bar.geometry().width() - 140, 0)
        self.btn_navi_logout.clicked.connect(self.on_click_btn_navi_logout)

        btn_navi_profi = Button_Navi('三')
        self.btn_navi_profi = btn_navi_profi.init_compo(self.bar)
        self.btn_navi_profi.setFixedSize(60, 60)
        self.btn_navi_profi.move(self.bar.geometry().width() - 200, 0)

        self.on_click_btn_navi_order()
        return self

    def display_btn_navi_order(self):
        '''
        Display the Order button in navi bar
        @return:
        '''
        btn_navi_order = Button_Navi('Order')
        self.btn_navi_order = btn_navi_order.init_compo(self.bar)
        self.btn_navi_order.setFixedSize(140, 60)
        self.btn_navi_order.move(0, 0)
        self.btn_navi_order.clicked.connect(self.on_click_btn_navi_order)

    def display_btn_navi_inven(self):
        '''
        Display the Inventory button in navi bar
        @return:
        '''
        btn_navi_inven = Button_Navi('Inventory')
        self.btn_navi_inven = btn_navi_inven.init_compo(self.bar)
        self.btn_navi_inven.setFixedSize(140, 60)
        self.btn_navi_inven.move(140, 0)
        self.btn_navi_inven.clicked.connect(self.on_click_btn_navi_inven)

    @interceptor_owner_pass.do_check_before(interceptor_owner_pass, 'check_permission', interceptor_owner_pass, 'deny')
    def display_btn_navi_repor(self):
        '''
        Display the Report button in navi bar
        @return:
        '''
        btn_navi_repor = Button_Navi('Report')
        self.btn_navi_repor = btn_navi_repor.init_compo(self.bar)
        self.btn_navi_repor.setFixedSize(140, 60)
        self.btn_navi_repor.move(280, 0)
        self.btn_navi_repor.clicked.connect(self.on_click_btn_navi_report)

    @interceptor_owner_pass.do_check_before(interceptor_owner_pass, 'check_permission', interceptor_owner_pass, 'deny')
    def display_btn_navi_staff(self):
        '''
        Display the Staff button in navi bar
        @return:
        '''
        btn_navi_staff = Button_Navi('Staff')
        self.btn_navi_staff = btn_navi_staff.init_compo(self.bar)
        self.btn_navi_staff.setFixedSize(140, 60)
        self.btn_navi_staff.move(420, 0)
        self.btn_navi_staff.clicked.connect(self.on_click_btn_navi_staff)

    def on_click_btn_navi_order(self):
        '''
        Callback when the Order button is clicked
        @return:
        '''
        Router('navi', 'navi', 'order').do_action()

    def on_click_btn_navi_inven(self):
        '''
        Callback when the Inventory button is clicked
        @return:
        '''
        Router('navi', 'navi', 'inven').do_action()

    def on_click_btn_navi_report(self):
        '''
        Callback when the Report button is clicked
        @return:
        '''
        Router('navi', 'navi', 'repor').do_action()

    def on_click_btn_navi_staff(self):
        '''
        Callback when the Staff button is clicked
        @return:
        '''
        Router('navi', 'navi', 'staff').do_action()

    def on_click_btn_navi_logout(self):
        '''
        Callback when the Logout button is clicked
        @return:
        '''
        Interceptor_Login.get_instance().set_permission('')