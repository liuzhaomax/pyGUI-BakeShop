#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Main_Body.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      30-08-2020
@LastModified   30-08-2020
@Function       main body
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.handler.inventory.Handler_Inven_Main import *
from src.controller.handler.order.Handler_Order_Main import *
from src.controller.handler.report.Handler_Repor_Main import *
from src.controller.handler.staff.Handler_Staff_Main import *
from src.model.entity.System import *
from src.model.Model_Inven import *
from src.view.order.Order_Main import *
from src.view.inventory.Inven_Main import *
from src.view.report.Repor_Main import *
from src.view.staff.Staff_Main import *


class Main_Body(Component, Controller):
    NAME = 'MAIN_BODY'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.parent = parent
        self.main = QFrame(parent)
        self.main.setMinimumSize(800, 600)
        self.main.resize(parent.geometry().width(), parent.geometry().height() - 60)
        self.main.move(0, 60)
        # view
        self.view_order_main = Order_Main()
        self.view_inven_main = Inven_Main()
        self.view_repor_main = Repor_Main()
        self.view_staff_main = Staff_Main()
        # model
        self.model = System.get_instance()
        # controller
        self.handler_order_main = Handler_Order_Main(self.view_order_main, self.model)
        self.handler_inven_main = Handler_Inven_Main(self.view_inven_main, self.model)
        self.handler_repor_main = Handler_Repor_Main(self.view_repor_main, self.model)
        self.handler_staff_main = Handler_Staff_Main(self.view_staff_main, None)
        # loading view
        self.order_main = self.handler_order_main.update_view(self)
        self.inven_main = self.handler_inven_main.update_view(self)
        self.repor_main = self.handler_repor_main.update_view(self)
        self.staff_main = self.handler_staff_main.update_view(self)
        # loading data
        self.handler_order_main.update_view_data()
        self.handler_inven_main.update_view_data()
        self.handler_repor_main.update_view_data()
        self.handler_staff_main.update_view_data()
        # router
        self.register_mb(self.order_main.layout.main, 'order', 'navi')
        self.register_mb(self.inven_main.layout.main, 'inven', 'navi')
        self.register_mb(self.repor_main.layout.main, 'repor', 'navi')
        self.register_mb(self.staff_main.layout.main, 'staff', 'navi')
        return self

