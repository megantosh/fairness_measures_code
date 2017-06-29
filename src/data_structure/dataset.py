'''
Created on Jun 14, 2017

@author: meike.zehlike
'''
import pandas as pd
from numpy import integer


class Dataset(object):
    '''
    reads a dataset from a csv-file into a dataframe
    '''

    @property
    def data(self):
        """
        a data frame that contains the dataset to be analyzed
        """
        return self.__data


    @property
    def protected_cols(self):
        return self.__protected_cols


    @property
    def target_cols(self):
        return self.__target_cols


    def __init__(self, data):
        '''
        Constructor
        '''
        if isinstance(data, str):
            # expect data to be a filename
            self.__data = pd.read_csv(data, header=0)
        elif isinstance(data, pd.DataFrame):
            self.__data = data

        self.__protected_cols = [col for col in self.data.columns.values if col.startswith('protected')]
        self.__target_cols = [col for col in self.data.columns if col.startswith('target')]

        # check if dataset is well-formed
        if not self.__protected_cols:
            raise ValueError("The dataset should contain at least one column that describes a protection status")
        if not self.__target_cols:
            raise ValueError("The dataset should contain at least one column that describes a target variable")

        # check that protected attributes are indicated by integers
        for protected_column in self.__protected_cols:
            column_values = self.__data[protected_column]
            protection_categories = column_values.unique()
            if not all(isinstance(item, integer) for item in protection_categories):
                raise ValueError("Protection status should be indicated by integers only")


    def normalize_column(self, column_name):
        mean_col = self.data[column_name].dropna().mean()
        min_col = self.data[column_name].dropna().min()
        max_col = self.data[column_name].dropna().max()
        self.data[column_name] = self.data[column_name].apply(lambda x: (x - mean_col) / (max_col - min_col))






