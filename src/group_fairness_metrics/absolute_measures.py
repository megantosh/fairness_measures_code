'''
Created on Jun 13, 2017

@author: meike.zehlike
'''
import numpy as np
import pandas as pd

def mean_difference(dataset, protected_column, non_protected=0, targets='all'):
    """
    takes a dataset with columns that contain target variables as well as protection status variables
    and calculates the mean difference of the targets of each protected group to the non-protected
    group. For each target column, first the variables are ordered into a subset for each protected
    group and the mean is calculated. Then the values of the target column for the non-protected
    group are extracted and their mean is calculated.
    Each protected mean is subtracted from the non-protected mean.

    @param dataset: data that contains all target and protected variables
    @param protected_column: the column that contains the protected variables
    @param non-protected: the value within protected_column that describes the non-protected category
    @param targets: set of column names of which the mean differences shall be calculated

    @return: a python dataframe that contains the target columns as column names and the protection
    categories from protected_column as indices. Note that the non-protected category is excluded as
    it would contain only zeros anyway. The cells contain the values of the mean differences
    between the non-protected group and the particular protected one for that particular target variables.
    If the difference is positive, the mean of the non-protected group was greater than the mean of the
    protected one, otherwise smaller.
    """

    if protected_column not in dataset.protected_cols:
        raise ValueError("given protected_column column name doesn't exist in dataset. Check spelling.")


    if targets == 'all':
        targets = dataset.target_cols

    result = pd.DataFrame()

    # get all protected attribute categories
    group_categories = dataset.data[protected_column].unique()

    for column_name in targets:
        if column_name not in dataset.target_cols:
            raise ValueError("given target column name doesn't exist in dataset. Check spelling.")
        else:
            result_col = pd.DataFrame()

            # calculate mean of target values for the non-protected group
            target_values_nonprotected = dataset.data.loc[dataset.data[protected_column] == non_protected, column_name]
            mean_nonprotected = np.mean(target_values_nonprotected, dtype=np.float64)

            # calculate mean of target values for all protected categories
            for category in group_categories:
                if category == non_protected:
                    # skip non_protected category, has been done above
                    continue
                else:
                    target_values_protected = dataset.data.loc[dataset.data[protected_column] == category, column_name]
                    mean = np.mean(target_values_protected, dtype=np.float64)
                    mean_diff = mean_nonprotected - mean
                    df = pd.DataFrame({column_name: [mean_diff]}, index=[category])
                    result_col = result_col.append(df)
        result = pd.concat([result, result_col], axis=1)
    return result
