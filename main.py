#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       main.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      20-08-2020
@LastModified   22-09-2020
@Function       application main entrance
'''''''''''''''''''''''''''''''''''''''''''''''''''
import sys
from src.app.App import *
from src.core.Controller import *


class Main(Controller):
    NAME = 'MAIN'

    def __init__(self):
        super().__init__()

    def launch(self, app):
        '''
        Launch the application
        @param app: QApplication
        @return:
        '''
        self.window = App()
        self.window.init_window()
        self.window.show()  # window.showMaximized()
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main().launch(app)