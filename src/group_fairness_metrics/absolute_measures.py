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
    @param target_column: name of the column that contains the prediction values
    @param protected_column: name of the column that contains the protection status
    @param non-protected: the value within protected_column that describes the non-protected category
                          zero on default

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


def normalized_difference(dataset, target_col, protected_col):
    """
    calculates the difference between the probability of being accepted given being a favored group
    member and the probability of being accepted given being a protected group member. This difference
    is normalized by the ratio of all accepted candidates by all favored candidates.
    Non-Discrimination is indicated when no difference in these probabilities exist. Maximum
    discrimination is indicated when the result is 1, i.e. the probability of being accepted as a
    favored is 1 whereas it is 0 for a protected group member.

    Only works for the binary case -> one protected group, one non-protected group, classification
    result is either positive or negative

    Assumes that in the dataset the favored group is labeled with protection status 0, protected group
    with 1
    Assumes that in the dataset the positive outcome is labeled as 1, negative as 0

    @param protected_col: name of the column that contains the protection status
    @param target_col: name of the column that contains the classifier results
    """

    unique, counts = np.unique(dataset.data[protected_col], return_counts=True)

    if len(unique) > 2:
        raise ValueError("This function is for binary problems only: There should be only one favored\
                          group and one protected group.")

    protected_group_counts = dict(zip(unique, counts))
    conditional_probs = dataset.conditional_prob_of_acceptance(target_col, protected_col)

    counts_pos = (dataset.data[target_col] == 1).sum()
    counts_neg = (dataset.data[target_col] == 0).sum()
    outcome_counts = {0:counts_neg, 1:counts_pos}

    prob_pos = outcome_counts[1] / len(dataset.data.index)
    prob_neg = outcome_counts[0] / len(dataset.data.index)
    prob_prot = protected_group_counts[1] / len(dataset.data.index)
    prob_fav = protected_group_counts[0] / len(dataset.data.index)

    d_max = min((prob_pos / prob_fav), (prob_neg / prob_prot))

    if d_max == 0:
        raise ZeroDivisionError

    delta = (conditional_probs[0] - conditional_probs[1]) / d_max
    return delta


def impact_ratio(dataset, target_col, protected_col):
    """
    calculates the ratio of positive outcomes for the protected group over the general group. Non-
    discrimination is indicated when the ratio is 1

    @param dataset:
    @param target_col:  name of the column that contains the classifier results
    @param protected_col: name of the column that contains the protection status

    """
    conditional_probs = dataset.conditional_prob_of_acceptance(target_col, protected_col)

    if conditional_probs[0] == 0:
        raise ZeroDivisionError

    return conditional_probs[1] / conditional_probs[0]






