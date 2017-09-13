'''
Created on Jun 13, 2017

@author: meike.zehlike
'''

import argparse
from data_structure.dataset import Dataset
import sys

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

    args = parser.parse_args()

    # read file into dataframe
    if (args.file == None):
        raise ValueError("Please provide a csv-file")

    dataset = Dataset(args.file[0])


'''demo cmd on schufa'''


if __name__ == '__main__':
    main()
