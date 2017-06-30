'''
Created on Jun 14, 2017

@author: mzehlike
'''
import unittest
import pandas as pd
from pandas.util import testing
import numpy as np
from data_structure.dataset import Dataset


class Test(unittest.TestCase):

    def test_dataframeCreation(self):
        dataset = Dataset('correctFile.csv')
        self.assertEqual((3, 4), dataset.data.shape, "dataset has wrong dimensions")

        with self.assertRaises(ValueError):
            dataset = Dataset('incorrectFileNoProtected.csv')
        with self.assertRaises(ValueError):
            dataset = Dataset('incorrectFileNoTarget.csv')


    def test_normalize_column(self):

        data = pd.DataFrame({'target1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                             'protected': [0, 1, 2, 3, 0, 1, 2, 3, 0]})
        dataset = Dataset(data)

        expected_result = pd.DataFrame({'target1': [-0.5, -0.375, -0.25, -0.125, 0, 0.125, 0.25, 0.375, 0.5],
                                        'protected': [0, 1, 2, 3, 0, 1, 2, 3, 0]})
        dataset.normalize_column('target1')
        testing.assert_frame_equal(expected_result, dataset.data, check_less_precise=True)


    def test_conditional_prob_of_acceptance(self):
        data = pd.DataFrame({'target': [1, 1, 1, 1, 1, 1, 1, 1],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:1.0, 1:1.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 1)
        self.assertDictEqual(expected_result, actual_result)

        #========================================================================

        data = pd.DataFrame({'target': [0, 0, 0, 0, 0, 0, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:0.0, 1:0.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 1)
        self.assertDictEqual(expected_result, actual_result)

        #=========================================================================

        data = pd.DataFrame({'target': [1, 1, 1, 1, 0, 0, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:0.5, 1:0.5}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 1)
        self.assertDictEqual(expected_result, actual_result)

        #=========================================================================

        data = pd.DataFrame({'target': [1, 0, 1, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:1.0, 1:0.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 1)
        self.assertDictEqual(expected_result, actual_result)

        #=========================================================================

        data = pd.DataFrame({'target': [0, 1, 0, 1, 0, 1, 0, 1],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:0.0, 1:1.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 1)
        self.assertDictEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
