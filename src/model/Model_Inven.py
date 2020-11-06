#!/usr/bin/python3
# coding=utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''
@FileName       Model_Inven.py
@Author         Zhao Liu
@StudId         30822750
@StartDate      06-09-2020
@LastModified   06-09-2020
@Function       Inven model
'''''''''''''''''''''''''''''''''''''''''''''''''''
from src.model.Model import *


class Model_Inven(Model):
    NAME = 'MODEL_INVEN'

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
            for key in self.format['inven']:
                if self.table.columns[index] == self.format['inven'][key]:
                    indices.append(key)
        self.table.columns = indices
        # strip
        for i in range(self.table.shape[0]):
            for k in self.format['inven']:
                self.table[k][i] = self.table[k][i].strip()
        self.table = self.table.sort_values('item_id', ascending=True)
        self.table = self.table.reset_index()

    def transform_to_excel_axis_for_update(self, new_quantities_remaining):
        '''
        Transform the entity to dataframe
        @param new_quantities_remaining:
        @return: self.table
        '''
        for key in range(new_quantities_remaining.__len__()):
            for i in range(self.table.shape[0]):
                if self.table['item_id'][i] == key:
                    self.table.loc[i, 'quantity'] = new_quantities_remaining[key]
                    break
        return self.table

    def prepare_to_update(self, table_calculated):
        '''
        Change the index of dataframe for writing
        @param table_calculated: Dataframe
        @return: new_table_to_write
        '''
        indices = []
        table = table_calculated.drop(columns=['index'])
        for index in range(len(table.columns)):
            for key in self.format['inven']:
                if table.columns[index] == key:
                    indices.append(self.format['inven'][key])
        table.columns = indices
        new_table_to_write = table  # df including new data
        return new_table_to_write
