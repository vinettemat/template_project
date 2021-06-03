#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This script describes  module distribution to the Distutils<
    More information about the scturcture of scrip can be found oin the next resoources
    - https://docs.python.org/2/distutils/setupscript.html
    -  https://github.com/kennethreitz/setup.py
"""

__author__ = "Lamjed Ben Jabeur"
__copyright__ = "Copyright 2019, Airbus"
__version__ = "0.9.0"
__maintainer__ = "Lamjed Ben Jabeur"
__email__ = "lamjed.la.ben-jabeur@airbus.com"
__status__ = "Prototype"

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='TemplateProject', # The name of your module
    version='0.9.0',
    description='A standard structure for data science project',
    long_description=readme,
    author='Elodie Bergonnier',
    author_email='elodie.bergonnier@airbus.com',
    url='https://gheprivate.intra.corp/hr-data-lab/covid19-absence',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    scripts=['bin/sample_script.py'] # executable scripts
)

