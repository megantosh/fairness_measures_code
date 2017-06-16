'''
Created on Jun 14, 2017

@author: mzehlike
'''
import unittest
from dataStructure.dataset import Dataset


class Test(unittest.TestCase):

    def test_dataframeCreation(self):
        dataset = Dataset('correctFile.csv')
        self.assertEqual((3, 4), dataset.data.shape, "dataset has wrong dimensions")

        with self.assertRaises(ValueError):
            dataset = Dataset('incorrectFileNoProtected.csv')
        with self.assertRaises(ValueError):
            dataset = Dataset('incorrectFileNoTarget.csv')



if __name__ == "__main__":
    unittest.main()
