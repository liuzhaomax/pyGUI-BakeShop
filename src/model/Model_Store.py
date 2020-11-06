#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Model_Store.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      23-09-2020
@LastModified   23-09-2020
@Function       Store model
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.Model import *


class Model_Store(Model):
    NAME = 'MODEL_STORE'

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
            for key in self.format['store']:
                if self.table.columns[index] == self.format['store'][key]:
                    indices.append(key)
        self.table.columns = indices
        # strip
        for i in range(self.table.shape[0]):
            for k in self.format['store']:
                self.table[k][i] = self.table[k][i].strip()
        self.table['store_id'] = self.table['store_id'].astype('int')
        self.table = self.table.sort_values('store_id', ascending=True)
        self.table = self.table.astype('str')
        self.table = self.table.reset_index()