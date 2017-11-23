'''
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
    If the difference greater zero, the mean of the non-protected group was greater than the mean of the
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
    mean_nonprotected = np.mean(target_values_nonprotected)

    # calculate mean of target values for all protected categories
    for category in group_categories:
        if category == non_protected:
            # skip non_protected category, has been done above
            continue
        else:
            target_values_protected = dataset.data.loc[dataset.data[protected_column] == category, target_column]
            mean = np.mean(target_values_protected)
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
    discrimination is indicated when the result is 1 (or -1 respectively), i.e. the probability of being accepted as a
    favored is 1 whereas it is 0 for a protected group member.

    Only works for the binary case -> one protected group, one non-protected group, classification
    result is either positive or negative

    Assumes that in the dataset the favored group is labeled with protection status 0, protected group
    with 1
    Assumes that in the dataset the positive outcome is labeled as 1, negative as 0

    @param protected_col: name of the column that contains the protection status
    @param target_col: name of the column that contains the classifier results

    @return 0     if the probability of being accepted is equal for all groups
            > 0   if the probability of being accepted is higher for the non-protected group
            < 0   if the probability of being accepted is higher for the protected group
    """

    unique_prot, counts_prot = np.unique(dataset.data[protected_col], return_counts=True)
    unique_targ, counts = np.unique(dataset.data[target_col], return_counts=True)

    if len(unique_prot) > 2 or len(unique_targ) > 2:
        print("This function is only applicable for binary problems. See function docs for details.")
        return np.nan

    protected_group_counts = dict(zip(unique_prot, counts_prot))
    conditional_probs = dataset.conditional_prob_for_group_category(target_col, protected_col, 1)

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
    calculates the ratio of positive outcomes for the protected group over the entire group. Non-
    discrimination is indicated when the ratio is close to 1

    @param dataset:
    @param target_col:      name of the column that contains the classifier results
    @param protected_col:   name of the column that contains the protection status

    @return:    > 1 if the probability to be classified positive as protected is greater than as
                    for the whole group
                < 1 if the probability to be classified positive as protected is less than as for
                    the whole group
                = 1 if probabilities are equal

                If the probability to be positively classified is zero, using this measure doesn't
                make sense and we throw a ValueError
    """
    prob_pos_prot = dataset.conditional_prob_for_group_category(target_col, protected_col, accepted=1)
    prob_pos = dataset.prob_positive_classification(target_col)

    if prob_pos == 0:
        raise ValueError

    return prob_pos_prot[1] / prob_pos


def odds_ratio(dataset, target_col, protected_col):
    """
    a statistical measure that describes the dependency of two features.

    @return:    > 1 if the probability to be classified positive as non-protected is greater than as
                    as protected
                < 1 if the probability to be classified positive as protected is greater than as
                    non-protected
                = 1 if probabilities are equal

                If the probability to be positively classified as a protected group member is zero,
                we catch the FloatingPointError and return positive infinity instead
    """
    conditional_probs_pos = dataset.conditional_prob_for_group_category(target_col, protected_col, accepted=1)
    conditional_probs_neg = dataset.conditional_prob_for_group_category(target_col, protected_col, accepted=0)

    try :
        return (conditional_probs_pos[0] * conditional_probs_neg[1]) / (conditional_probs_pos[1] * conditional_probs_neg[0])
    except FloatingPointError: return np.inf







