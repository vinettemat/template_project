#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This script include basic unit test.
"""

__author__ = "Lamjed Ben Jabeur"
__copyright__ = "Copyright 2019, Airbus"
__version__ = "0.9.0"
__maintainer__ = "Lamjed Ben Jabeur"
__email__ = "lamjed.la.ben-jabeur@airbus.com"
__status__ = "Prototype"

from .context import templateproject

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()