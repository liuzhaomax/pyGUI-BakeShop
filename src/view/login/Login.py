#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Login.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      24-09-2020
@LastModified   24-09-2020
@Function       Login page 
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.controller.interceptor.Interceptor_Func_Manager_Pass import *
from src.controller.interceptor.Interceptor_Func_Owner_Pass import *
from src.controller.interceptor.Interceptor_Login import *
from src.controller.handler.login.Handler_Login import *
from src.core.Component import *


class Login(Component):
    NAME = 'LOGIN'

    def __init__(self):
        super().__init__()
        self.staff = None

    def init_compo(self, parent):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.main = QFrame(parent)
        self.main.setMinimumSize(700, 600)
        self.main.resize(parent.geometry().width() - 600, parent.geometry().height() - 400)
        self.main.move(300, 100)
        self.main.setStyleSheet(self.ctx.style_frame)
        self.north = QFrame(self.main)
        self.north.resize(self.main.geometry().width(), 150)
        self.north.move(0, 0)
        self.north.setStyleSheet(self.ctx.style_frame)
        self.south = QFrame(self.main)
        self.south.resize(self.main.geometry().width(), self.main.geometry().height() - 150)
        self.south.move(0, 150)
        self.south.setStyleSheet(self.ctx.style_frame)
        # label_app_name
        self.label_app_name = QLabel(self.north)
        self.label_app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_app_name.setText(self.ctx.app_name)
        self.label_app_name.resize(self.north.geometry().width(), self.north.geometry().height())
        self.label_app_name.move(0, 0)
        self.label_app_name.setStyleSheet(self.ctx.style_super_big_label)
        # label_login_zone
        self.label_login_zone = QLabel(self.south)
        self.label_login_zone.resize(self.south.geometry().width() * 3/7, self.south.geometry().height() - 100)
        self.label_login_zone.move(self.south.geometry().width() * 2/7, 50)
        self.label_login_zone.setStyleSheet(self.ctx.style_super_big_label)
        # label_login_text
        self.label_login_text = QLabel(self.label_login_zone)
        self.label_login_text.setText('Login')
        self.label_login_text.resize(self.label_login_zone.geometry().width(), self.label_login_zone.geometry().height() * 1/9)
        self.label_login_text.move(0, self.label_login_zone.geometry().height() * 1/9)
        self.label_login_text.setStyleSheet(self.ctx.style_login_label)
        # line_staff_id
        self.line_staff_id = QLineEdit(self.label_login_zone)
        self.line_staff_id.setClearButtonEnabled(True)
        self.line_staff_id.setPlaceholderText('Please enter your staff ID')
        self.line_staff_id.resize(self.label_login_zone.geometry().width(), self.label_login_zone.geometry().height() * 1/9)
        self.line_staff_id.move(0, self.label_login_zone.geometry().height() * 3/9)
        self.line_staff_id.setStyleSheet(self.ctx.style_login_line)
        self.line_staff_id.returnPressed.connect(lambda: self.on_pressed_enter())
        # line_password
        self.line_password = QLineEdit(self.label_login_zone)
        self.line_password.setEchoMode(QLineEdit.Password)
        self.line_password.setClearButtonEnabled(True)
        self.line_password.setPlaceholderText('Please enter your password')
        self.line_password.resize(self.label_login_zone.geometry().width(), self.label_login_zone.geometry().height() * 1/9)
        self.line_password.move(0, self.label_login_zone.geometry().height() * 5/9)
        self.line_password.setStyleSheet(self.ctx.style_login_line)
        self.line_password.returnPressed.connect(lambda: self.on_pressed_enter())
        # btn_login
        self.btn_login = QPushButton(self.label_login_zone)
        self.btn_login.setText('Login')
        self.btn_login.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_login.resize(100, self.label_login_zone.geometry().height() * 1/9)
        self.btn_login.move(self.label_login_zone.geometry().width()/2 - 50, self.label_login_zone.geometry().height() * 7/9)
        self.btn_login.setStyleSheet(self.ctx.style_btn_login)
        self.btn_login.clicked.connect(lambda: self.on_pressed_enter())
        return self

    def on_pressed_enter(self):
        '''
        Callback when the enter key is pressed when the focus is on the QLineEdit of password and staff id
        @return:
        '''
        staff_id = self.line_staff_id.text().strip()
        password = self.line_password.text()
        handler_login = Handler_Login(None, None)
        handler_login.register_observer(Interceptor_Func_Owner_Pass.get_instance())
        handler_login.register_observer(Interceptor_Func_Manager_Pass.get_instance())
        handler_login.register_observer(Interceptor_Login.get_instance())
        self.staff = handler_login.match_login_info(staff_id, password)
        if self.staff:
            permission = self.staff.get_type()
        else:
            permission = ''
        handler_login.set_permission(permission)
        self.line_password.setText('')

