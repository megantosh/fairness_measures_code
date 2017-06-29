'''
Created on Jun 14, 2017

@author: meike.zehlike
'''
import pandas as pd
import numpy as np
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


    def conditional_prob_of_acceptance(self, target_col, protected_col):
        """
        calculates the conditional probability for each group (protected and favored to be classified
        as positive.
        Assumes that classification results are binary, either positive or negative

        @param target_col: name of the column in data that contains the classification results
        @param protected_col: name of the column in data that contains the protection status

        @return: a dictionary with protection status as key and conditional probability as value

        """
        if target_col not in self.target_cols:
            raise ValueError("given target column doesn't exist")

        if protected_col not in self.protected_cols:
            raise ValueError("given protected column doesn't exist")

        conditional_probs = {}
        unique, counts = np.unique(self.data[protected_col], return_counts=True)
        protected_group_counts = dict(zip(unique, counts))

        # calculate conditional probability of positive outcome given each group category
        all_positives = (self.data[target_col] == 1).sum()
        for group_category, xxx in protected_group_counts.items():
            values_of_category = self.data.loc[self.data[protected_col] == group_category, target_col]
            positive_and_category = (values_of_category == 1).sum()
            prob_pos_given_cat = positive_and_category / all_positives
            conditional_probs[group_category] = prob_pos_given_cat

        return conditional_probs



