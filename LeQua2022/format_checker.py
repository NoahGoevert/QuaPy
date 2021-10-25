import argparse
import quapy as qp
from data import ResultSubmission, evaluate_submission
import constants
import os

"""
LeQua2022 Official format-checker script 
"""

def main(args):
    try:
        ResultSubmission.check_file_format(args.prevalence_file)
    except Exception as e:
        print(e)
        print('Format check: not passed')
    else:
        print('Format check: passed')


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='LeQua2022 official format-checker script')
    parser.add_argument('prevalence_file', metavar='PREV-PATH', type=str,
                        help='Path of the file containing prevalence values to check')
    args = parser.parse_args()

    main(args)
