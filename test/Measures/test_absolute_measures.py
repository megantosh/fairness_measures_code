'''
Created on Jun 13, 2017

@author: meike.zehlike
'''
import unittest
import measures.absolute_measures as am
import pandas as pd
from data_structure.dataset import Dataset
import numpy as np


class Test(unittest.TestCase):

    np.seterr(all='raise')

    def test_mean_difference(self):
        data = pd.DataFrame({'target': [1, 2, 3, 4, 5, 6, 7, 8],
                             'protected': [0, 1, 2, 3, 0, 1, 2, 3]})

        dataset = Dataset(data)

        expected_result_0 = pd.DataFrame({'target': [-1, -2, -3]},
                                          index=[1, 2, 3], dtype=np.float64)

        actual_result_0 = am.mean_difference(dataset, 'target', 'protected', non_protected=0)
        self.assertTrue(expected_result_0.equals(actual_result_0))

        #==========================================================================

        expected_result_1 = pd.DataFrame({'target': [1, -1, -2]},
                                          index=[0, 2, 3], dtype=np.float64)

        actual_result_1 = am.mean_difference(dataset, 'target', 'protected', non_protected=1)
        self.assertTrue(expected_result_1.equals(actual_result_1))


    def test_normalized_difference(self):
        # no discrimination
        data = pd.DataFrame({'target': [1, 1, 0, 0, 1, 1, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(0, am.normalized_difference(dataset, "target", "protected"))

        #===========================================================================

        # maximal discrimination
        data = pd.DataFrame({'target': [1, 0, 1, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(1, am.normalized_difference(dataset, "target", "protected"))

        #===========================================================================

        # bit of discrimination
        data = pd.DataFrame({'target': [1, 1, 0, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(0.5, am.normalized_difference(dataset, "target", "protected"))

        #===========================================================================

        # if no-one is selected function would raise zero division error
        data = pd.DataFrame({'target': [0, 0, 0, 0, 0, 0, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertRaises(ZeroDivisionError, am.normalized_difference, dataset, "target", "protected")

        #===========================================================================

        # if everybody is selected function would raise zero division error
        data = pd.DataFrame({'target': [1, 1, 1, 1, 1, 1, 1, 1],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertRaises(ZeroDivisionError, am.normalized_difference, dataset, "target", "protected")


    def test_impact_ratio(self):
        # no discrimination
        data = pd.DataFrame({'target': [1, 1, 0, 0, 1, 1, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(1, am.impact_ratio(dataset, "target", "protected"))

        #===========================================================================

        # maximal discrimination
        data = pd.DataFrame({'target': [1, 0, 1, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(0, am.impact_ratio(dataset, "target", "protected"))

        #===========================================================================

        # discrimination against protected
        data = pd.DataFrame({'target':    [1, 1, 0, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(0.5, am.impact_ratio(dataset, "target", "protected"))

        #===========================================================================

        # inverse discrimination
        data = pd.DataFrame({'target': [0, 1, 0, 1, 0, 1, 0, 1],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(2, am.impact_ratio(dataset, "target", "protected"))


    def test_odds_ratio(self):
        # no discrimination
        data = pd.DataFrame({'target': [1, 1, 0, 0, 1, 1, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(1, am.odds_ratio(dataset, "target", "protected"))

        #===========================================================================

        # the probability of being accepted as a protected group member is in this case zero
        # hence should return infinity
        data = pd.DataFrame({'target': [1, 0, 1, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(np.inf, am.odds_ratio(dataset, "target", "protected"))

        #===========================================================================

        # inverse discrimination
        data = pd.DataFrame({'target': [0, 1, 0, 1, 0, 1, 0, 1],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertEqual(0, am.odds_ratio(dataset, "target", "protected"))

        #===========================================================================

        # bit of discrimination, value should be greater than one
        data = pd.DataFrame({'target': [1, 1, 0, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})

        dataset = Dataset(data)
        self.assertGreater(am.odds_ratio(dataset, "target", "protected"), 1)

if __name__ == "__main__":
    unittest.main()








