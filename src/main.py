'''
Created on Jun 13, 2017

@author: mzehlike
'''

import argparse
from dataStructure.dataset import Dataset

def main():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='fairness benchmarks',
                                     description='performs various discrimination measures on a given dataset',
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

    dataset = Dataset(args.file)



if __name__ == '__main__':
    main()
