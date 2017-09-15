'''
Created on Jun 13, 2017

@author: meike.zehlike
'''

import argparse
from data_structure.dataset import Dataset
from group_fairness_metrics.absolute_measures import *
import sys
from group_fairness_metrics.statistical_tests import *

def main():
    # check python version
    if sys.version_info[1] < 3.5:
        raise Exception("Please use Python 3.5 or above to run")

    # create the top-level parser
    parser = argparse.ArgumentParser(prog='fairness benchmarks',
                                     description='performs various discrimination group_fairness_metrics on a given dataset',
                                     epilog="=== === === end === === ===")
    parser.add_argument("-f", "--file", nargs='*', help="provide a dataset as csv-file to the algorithms")
    subparsers = parser.add_subparsers(help='sub-command help')

    # create the parser for the "file" command
    parser_file = subparsers.add_parser('file', help='provide a csv file containing a dataset')
    parser_file.add_argument(dest='file_to_read')

    # run demo
    parser.add_argument("-d", "--demo", dest='demo', action='store_true', help="run all algorithms with an example dataset")
    args = parser.parse_args()

    if (args.demo == True):
        run_demo('demo.csv')
        return

    # read file into dataframe
    if (args.file == None):
        raise ValueError("Please provide a csv-file")

    dataset = Dataset(args.file[0])
    # to be continued


def run_demo(filename):
    print('Running all measures with an example dataset and prints results to stdout. Please note, that this dataset was created artificially.')
    dataset = Dataset(filename)

    print('=========== difference of means test =============')
    print(t_test_ind(dataset, 'target_score', 'protected_sex'))

    print('\n=========== mean differences ==============')
    print(mean_difference(dataset, 'target_score', 'protected_sex').T)

    print('\n=========== normalized differences ============')
    print(normalized_difference(dataset, 'target_loan_approved', 'protected_sex'))

    print('\n=========== impact ratio ============')
    print(impact_ratio(dataset, 'target_loan_approved', 'protected_sex'))

    print('\n=========== odds ratio ============')
    print(fisher_exact(dataset, 'target_loan_approved', 'protected_sex'))





if __name__ == '__main__':
    main()
