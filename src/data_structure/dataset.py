'''
Created on Jun 14, 2017

@author: meike.zehlike
'''
import pandas as pd


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

    def __init__(self, filename):
        '''
        Constructor
        '''
        self.__data = pd.read_csv(filename, header=0)

        protected_cols = [col for col in self.data.columns.values if col.startswith('protected')]
        target_cols = [col for col in self.data.columns if col.startswith('target')]

        # check if dataset is well-formed
        if not protected_cols:
            raise ValueError("The dataset should contain at least one column that describes a protection status")
        if not target_cols:
            raise ValueError("The dataset should contain at least one column that describes a target variable")


