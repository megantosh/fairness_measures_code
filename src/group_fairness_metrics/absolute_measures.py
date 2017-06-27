'''
Created on Jun 13, 2017

@author: meike.zehlike
'''
import numpy as np
import pandas as pd

def mean_difference(dataset, target_column, protected_column, non_protected=0):
    """
    takes a dataset with columns that contain target values (i.e. prediction scores of the model)
    as well as protection status variables and calculates the mean difference of the targets of each
    protected group to the non-protected group. For each target column, first the variables are
    ordered into a subset for each protected group and the mean is calculated. Then the values of
    the target column for the non-protected group are extracted and their mean is calculated.
    Each protected mean of predictions is subtracted from the non-protected mean.

    @param dataset: data that contains all target and protected variables
    @param target_column: column that contains the prediction values
    @param protected_column: the column that contains the protected variables
    @param non-protected: the value within protected_column that describes the non-protected category

    @return: a python dataframe that contains the target as column name and the protection
    categories from protected_column as indices. Note that the non-protected category is excluded as
    it would contain only zeros anyway. The cells contain the values of the mean differences
    between the non-protected group and the particular protected one for that particular target variables.
    If the difference is positive, the mean of the non-protected group was greater than the mean of the
    protected one, otherwise smaller.
    """

    if protected_column not in dataset.protected_cols:
        raise ValueError("given protected column name doesn't exist in dataset. Check spelling.")

    if target_column not in dataset.target_cols:
        raise ValueError("given target column name doesn't exist in dataset. Check spelling.")

    # normalize prediction scores


    result = pd.DataFrame()

    # get all protected attribute categories
    group_categories = dataset.data[protected_column].unique()

    # calculate mean of target values for the non-protected group
    target_values_nonprotected = dataset.data.loc[dataset.data[protected_column] == non_protected, target_column]
    mean_nonprotected = np.mean(target_values_nonprotected, dtype=np.float64)

    # calculate mean of target values for all protected categories
    for category in group_categories:
        if category == non_protected:
            # skip non_protected category, has been done above
            continue
        else:
            target_values_protected = dataset.data.loc[dataset.data[protected_column] == category, target_column]
            mean = np.mean(target_values_protected, dtype=np.float64)
            mean_diff = mean_nonprotected - mean
            df = pd.DataFrame({target_column: [mean_diff]}, index=[category])
            result = result.append(df)
    return result


def normalized_difference(dataset, target_col, protected_col, non_protected=0):
    result = pd.DataFrame()



    return result











