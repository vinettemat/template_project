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

import configparser
import logging
import logging.config
import multiprocessing
import os
import re
import warnings


# Logging utilities

def filter_warnings():
    warnings.filterwarnings('ignore')


def setup_logger():
    """
    Configure the logger
    :return:
    """

    filter_warnings()
    logging_file = 'logging.ini' if os.path.isfile('logging.ini') else (
        '../logging.ini' if os.path.isfile('../logging.ini') else 'logging.ini')
    logging.config.fileConfig(logging_file, disable_existing_loggers=True)
    return get_logger()


def get_logger():
    """
    Gets the logger
    :return: the logger
    """
    return logging.getLogger(__name__)


# Configuration utilities

def get_configuration(key, group=None, is_list=False):
    '''
    Gets a configuration paramter
    :param key:  the parameter key
    :param group: the parameter group
    :return:  the parameter value
    '''
    config = configparser.ConfigParser()
    config.read('config.ini' if os.path.isfile('config.ini') else '../config.ini')
    value = config[group][key] if group else config[key]
    if is_list:
        value = re.split('\s*,+\*', value)
    return value


# Pandas mulithreading

def thread_apply(args):
    '''
    Warper for Pandas pd.apply in  multithreading mode
    :param args: arguments to be passed to pd.apply with the two arguments corresspend to dataframe and the function.
    :return: processed pandas Series
    '''
    df, func, kwargs = args
    return df.apply(func, **kwargs)


def parallel_apply(df, func, k=1000, **kwargs):
    '''

    :param df: the  pandas dataframe
    :param func: the function to be applied on the dataframe
    :param k: the minimal number of row to use multithreading
    :param kwargs: addition arguments
    :return: transformed dataframe
    '''

    logger = get_logger()
    if df.shape[0] >= k:
        logger.info("PARALEL APPLY", func.__name__, df.shape[0])
        workers = multiprocessing.cpu_count()
        size = int(len(df) / workers)
        pool = multiprocessing.Pool(processes=workers)
        dataframes = [(df.iloc[i:min(i + size, len(df)), :], func, kwargs) for i in range(0, len(df), size)]
        result = pool.map(thread_apply, dataframes)
        pool.close()
        return pd.concat(result)
    else:
        logger.info("INLINE APPLY", func.__name__, df.shape[0])
        return df.apply(func, **kwargs)
