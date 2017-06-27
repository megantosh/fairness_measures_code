'''
Created on Jun 13, 2017

@author: meike.zehlike
'''
import unittest
import group_fairness_metrics.absolute_measures as am
import pandas as pd
from data_structure.dataset import Dataset
import numpy as np


class Test(unittest.TestCase):

    def test_mean_difference(self):
        data = pd.DataFrame({'target1': [1, 2, 3, 4, 5, 6, 7, 8],
                             'protected': [0, 1, 2, 3, 0, 1, 2, 3]})

        dataset = Dataset(data)

        expected_result_0 = pd.DataFrame({'target1': [-1, -2, -3]},
                                          index=[1, 2, 3], dtype=np.float64)

        actual_result_0 = am.mean_difference(dataset, 'target1', 'protected', non_protected=0)
        self.assertTrue(expected_result_0.equals(actual_result_0))

        #==========================================================================

        expected_result_1 = pd.DataFrame({'target1': [1, -1, -2]},
                                          index=[0, 2, 3], dtype=np.float64)

        actual_result_1 = am.mean_difference(dataset, 'target1', 'protected', non_protected=1)
        self.assertTrue(expected_result_1.equals(actual_result_1))



if __name__ == "__main__":
    unittest.main()
