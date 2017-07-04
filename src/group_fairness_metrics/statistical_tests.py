'''
Created on Jun 13, 2017

@author: meike.zehlike
'''
from scipy.stats import stats
from scipy.stats.stats import ttest_ind


def t_test_ind(dataset, target_col, protected_col, equal_var=False):
    """
    performs the independent two-sample t-Test, or Welch's test if equality of the variances is not
    given

    @param dataset:
    @param target_col:      name of the column that contains the classifier results
    @param protected_col:   name of the column that contains the protection status
    @param equal_var:       f True (default), perform a standard independent 2 sample test that
                            assumes equal population variances. If False, perform Welch’s t-test,
                            which does not assume equal population variance

    @return: calculated t-statistic and two-tailed p-value

    """
    protected_targets = dataset.get_all_targets_of_group(target_col, protected_col, 1)
    nonprotected_targets = dataset.get_all_targets_of_group(target_col, protected_col, 0)
    return ttest_ind(protected_targets, nonprotected_targets)


def fisher_exact(dataset, target_col, protected_col):
    """
    Performs a Fisher exact test on a 2x2 contingency table as in scipy.stats.fisher_exact()

    @param dataset:
    @param target_col:      name of the column that contains the classifier results
    @param protected_col:   name of the column that contains the protection status

    @return: odds ratio and related pvalue
    """
    positive_protected = dataset.count_classification_and_category(target_col, protected_col, protected=1, accepted=1)
    negative_protected = dataset.count_classification_and_category(target_col, protected_col, protected=1, accepted=0)
    positive_nonprotected = dataset.count_classification_and_category(target_col, protected_col, protected=0, accepted=1)
    negative_nonprotected = dataset.count_classification_and_category(target_col, protected_col, protected=0, accepted=0)

    contingency_table = [[positive_protected, negative_protected], [positive_nonprotected, negative_nonprotected]]

    return stats.fisher_exact(contingency_table)
