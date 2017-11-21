'''
Created on Jun 14, 2017

@author: mzehlike
'''
import unittest
import pandas as pd
import os
from pandas.util import testing
from data_structure.dataset import Dataset

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class Test(unittest.TestCase):

    def test_dataframeCreation(self):
        dataset = Dataset(THIS_DIR + '/correctFile.csv')
        self.assertEqual((3, 4), dataset.data.shape, "dataset has wrong dimensions")

        with self.assertRaises(ValueError):
            dataset = Dataset(THIS_DIR + '/incorrectFileNoProtected.csv')
        with self.assertRaises(ValueError):
            dataset = Dataset(THIS_DIR + '/incorrectFileNoTarget.csv')


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


    def test_conditional_prob_of_rejection(self):
        data = pd.DataFrame({'target': [1, 1, 1, 1, 1, 1, 1, 1],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:0.0, 1:0.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 0)
        self.assertDictEqual(expected_result, actual_result)

        #========================================================================

        data = pd.DataFrame({'target': [0, 0, 0, 0, 0, 0, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:1.0, 1:1.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 0)
        self.assertDictEqual(expected_result, actual_result)

        #=========================================================================

        data = pd.DataFrame({'target': [1, 1, 1, 1, 0, 0, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:0.5, 1:0.5}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 0)
        self.assertDictEqual(expected_result, actual_result)

        #=========================================================================

        data = pd.DataFrame({'target': [1, 0, 1, 0, 1, 0, 1, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:0.0, 1:1.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 0)
        self.assertDictEqual(expected_result, actual_result)

        #=========================================================================

        data = pd.DataFrame({'target': [0, 1, 0, 1, 0, 1, 0, 1],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected_result = {0:1.0, 1:0.0}
        actual_result = dataset.conditional_prob_for_group_category("target", "protected", 0)
        self.assertDictEqual(expected_result, actual_result)


    def test_get_all_targets_of_group(self):
        data = pd.DataFrame({'target': [1, 1, 1, 1, 0, 0, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        expected = [1, 1, 0, 0]
        actual = dataset.get_all_targets_of_group("target", "protected", 0)
        self.assertCountEqual(expected, actual)

        actual = dataset.get_all_targets_of_group("target", "protected", 1)
        self.assertCountEqual(expected, actual)

        #=============================================================================

        # if noone of the desired group is in the dataset, should return empty array
        data = pd.DataFrame({'target': [1, 1, 1, 1, 0, 0, 0, 0],
                             'protected': [1, 1, 1, 1, 1, 1, 1, 1]})
        dataset = Dataset(data)

        actual = dataset.get_all_targets_of_group("target", "protected", 0)
        self.assertFalse(actual)



    def test_count_classification_and_category(self):
        data = pd.DataFrame({'target': [1, 1, 1, 1, 1, 0, 0, 0],
                             'protected': [0, 1, 0, 1, 0, 1, 0, 1]})
        dataset = Dataset(data)

        self.assertEqual(1, dataset.count_classification_and_category("target", "protected", 0, 0))
        self.assertEqual(3, dataset.count_classification_and_category("target", "protected", 0, 1))
        self.assertEqual(2, dataset.count_classification_and_category("target", "protected", 1, 0))
        self.assertEqual(2, dataset.count_classification_and_category("target", "protected", 1, 1))


if __name__ == "__main__":
    unittest.main()
