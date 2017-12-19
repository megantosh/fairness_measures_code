'''
Created on Jun 13, 2017

@author: meike.zehlike
'''

import measures.statistical_tests as statest
from data_structure.dataset import Dataset
import unittest
import numpy as np
import pandas as pd


class Test(unittest.TestCase):
    '''
    Variance between the groups / variance within groups
    not related / not paired
    '''
    np.seterr(all='raise')

    def test_t_test_ind(self):

        data = pd.DataFrame({'target': [935, 955, 967, 1002, 1000, 964, 952, 933],
                             'protected': [978, 982, 1017, 973, 1006, 1017, 995, 1048]})

        dataset = Dataset(data)

        expected_p_val = pd.DataFrame({'target': [0.01672]},
                                         dtype=np.float64)

        actual_p_val = statest(dataset, 'target', 'protected', non_protected=0)

        self.assertTrue(expected_p_val.equals(actual_p_val))


        # ==========================================================================
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html