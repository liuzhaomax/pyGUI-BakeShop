#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Order_Submitting_Middle.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      29-09-2020
@LastModified   29-09-2020
@Function       Order submitting page middle panel
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.view.order.Order_Submitting_Middle_Item import *


class Order_Submitting_Middle(Component):
    NAME = 'ORDER_SUBMITTING_PAGE_MIDDLE_PANEL'

    def __init__(self):
        super().__init__()

    def init_compo(self, parent, parent_widget):
        '''
        Initialise the component
        @param parent: QFrame
        @return: self
        '''
        self.parent = parent
        # layout
        self.layout_middle = QFrame(parent_widget)
        self.layout_middle.resize(parent_widget.geometry().width() - 40, parent_widget.geometry().height())
        self.layout_middle.move(30, 0)
        self.layout_middle.setStyleSheet(self.ctx.style_frame)
        # form_layout
        self.form_layout_middle = QFormLayout(self.layout_middle)
        self.form_layout_middle.setSpacing(20)
        self.form_layout_middle.setLabelAlignment(QtCore.Qt.AlignRight)
        self.form_layout_middle.setFormAlignment(QtCore.Qt.AlignLeft)
        hbox_layout_attr = QHBoxLayout()
        label_order_id_label = QLabel('Order ID:')
        label_order_id_label.setStyleSheet(self.ctx.style_label_key)
        label_order_id_label.setFixedHeight(30)
        label_order_id_data = QLabel(self.ctx.next_order_id)
        label_order_id_data.setStyleSheet(self.ctx.style_label_value)
        label_order_id_data.setFixedHeight(30)
        label_store_id_label = QLabel('Store ID:')
        label_store_id_label.setStyleSheet(self.ctx.style_label_key)
        label_store_id_label.setFixedHeight(30)
        if str(self.ctx.store_id).__len__() > 2:  # Thread problem fixed: owner store id is 1|2|3|4... Default is 1.
            store_id = str(self.ctx.store_id).split('|')[0]
        else:
            store_id = str(self.ctx.store_id)
        self.label_store_id_data = QLabel(store_id)
        self.label_store_id_data.setStyleSheet(self.ctx.style_label_value)
        self.label_store_id_data.setFixedHeight(30)
        label_staff_id_label = QLabel('Staff ID:')
        label_staff_id_label.setStyleSheet(self.ctx.style_label_key)
        label_staff_id_label.setFixedHeight(30)
        label_staff_id_data = QLabel(str(self.ctx.staff_id))
        label_staff_id_data.setStyleSheet(self.ctx.style_label_value)
        label_staff_id_data.setFixedHeight(30)
        label_datetime_label = QLabel('Date-time:')
        label_datetime_label.setStyleSheet(self.ctx.style_label_key)
        label_datetime_label.setFixedHeight(30)
        label_datetime_data = QLabel('not created yet')
        label_datetime_data.setStyleSheet(self.ctx.style_label_value)
        label_datetime_data.setFixedHeight(30)
        hbox_layout_attr.addWidget(label_order_id_label)
        hbox_layout_attr.addWidget(label_order_id_data)
        hbox_layout_attr.addWidget(label_store_id_label)
        hbox_layout_attr.addWidget(self.label_store_id_data)
        hbox_layout_attr.addWidget(label_staff_id_label)
        hbox_layout_attr.addWidget(label_staff_id_data)
        hbox_layout_attr.addWidget(label_datetime_label)
        hbox_layout_attr.addWidget(label_datetime_data)
        self.form_layout_middle.addRow(hbox_layout_attr)

        panel_item = Order_Submitting_Middle_Item()
        self.panel_item = panel_item.init_compo(self)
        return self