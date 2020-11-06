#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Model_Order.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      06-09-2020
@LastModified   06-09-2020
@Function       Order model
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.Model import *


class Model_Order(Model):
    NAME = 'MODEL_ORDER'

    def __init__(self, file_name, sheet_name):
        super().__init__(file_name, sheet_name)
        self.format = self.ctx.load_data_label_json()

    def transform_for_system(self):
        '''
        Transform the dataframe to entity
        @return:
        '''
        self.table = self.table.astype('str')
        indices = []
        for index in range(len(self.table.columns)):
            for key in self.format['order']:
                if self.table.columns[index] == self.format['order'][key]:
                    indices.append(key)
        self.table.columns = indices
        self.table['order_id'] = self.table['order_id'].astype('int')
        self.table = self.table.sort_values('order_id', ascending=False)
        self.table = self.table.astype('str')
        self.table = self.table.reset_index()
        self.table['type'] = range(self.table.shape[0])
        for i in range(self.table.shape[0]):
            if self.table['cust_phone'][i] != 'nan':
                self.table.loc[i, 'type'] = 'Bean'
            else:
                self.table.loc[i, 'type'] = 'Common'

    def transform_to_excel_axis(self, new_data):
        '''
        Transform the entity to array(dict elements) with excel axis
        @return: data_formed
        '''
        data_formed = [{}]
        for k in self.format['order']:
            data_formed[0][self.format['order'][k]] = k
        for key in data_formed[0]:
            for kk in new_data[0]:
                if kk == data_formed[0][key]:
                    data_formed[0][key] = new_data[0][kk]
                    break
        return data_formed

    def prepare_to_write(self, new_data_transformed):
        '''
        Transform the array(dict elements) to dataframe
        @param new_data_transformed: list
        @return: new_table_to_write
        '''
        new_data_df = DataFrame(new_data_transformed)  # [{},{}]
        new_table_to_write = self.original_table.append(new_data_df, ignore_index=True)  # df including new data
        return new_table_to_write
