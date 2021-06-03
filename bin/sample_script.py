#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This is a sample script.
"""

__author__ = "Lamjed Ben Jabeur"
__copyright__ = "Copyright 2019, Airbus"
__version__ = "0.9.0"
__maintainer__ = "Lamjed Ben Jabeur"
__email__ = "lamjed.la.ben-jabeur@airbus.com"
__status__ = "Prototype"

import argparse
import os
import sys
import time

from tqdm import tqdm

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from templateproject.utils import setup_logger, get_configuration


def get_arguments():
    """
    Parse command line arguments
    :return: arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="The input CSV file", type=str, required=True)
    parser.add_argument('-o', '--output', help="The output CSV file", type=str, required=True)
    parser.add_argument('-n', '--nrows', default=5, help="The number of rows", type=int, required=False)

    args = parser.parse_args()

    return args.input, args.output, args.nrows


if __name__ == '__main__':
    start = time.time()

    # SECTION: Setup logger
    logger = setup_logger()
    logger.info('START SCRIPT %s' % sys.argv[0])

    # SECTION:Config parameters

    raw_path = get_configuration('raw', 'path')
    processed_path = get_configuration('processed', 'path')

    logger.info('Configuration: row path=%s' % raw_path)
    logger.info('Configuration: processed path=%s' % processed_path)

    # SECTION: Argument parameters
    input_file, output_file, nrows = get_arguments()

    logger.info('Argument: input=%s' % input_file)
    logger.info('Argument: output=%s' % output_file)
    logger.info('Argument: nrows=%s' % nrows)
    logger.info('This is list of required packages')

    # SECTION: sample loop
    logger.info('Start processing')
    items = [i for i in range(0, 100)]
    with tqdm(total=len(items)) as pbar:
        for item in items:
            time.sleep(0.1)
            pbar.update(1)

    # End script
    end = time.time()
    logger.info('END SCRIPT')
    logger.info('EXECUTION TIME %0.3f' % (end - start))
