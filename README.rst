===========================
Template Project
===========================

A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.
This project structure is inspired from  `Cookiecutter Data Science <https://github.com/drivendata/cookiecutter-data-science>`_.


Project structure
===================

.. code-block:: bash

   <project_name>/
   ├── .gitignore                 Git configuration
   ├── README.rst                 The top-level README for developers using this project.
   ├── requirements.txt           The requirements file for reproducing the analysis environment,
   │                              e.g.  generated with `pip freeze > requirements.txt`
   ├── config.ini                 Project configurations
   ├── logging.ini                Logger configuration
   ├── LICENSE                    The license file
   ├── setup.py                   Make this project pip installable with `pip install -e`
   ├── Makefile                   Makefile with commands like `make data` or `make train`
   ├── MANIFEST.in                Definition files to be distribute
   ├── templateproject/           Python module
   │   ├── __init__.py            Makes src a Python module
   │   └── utils.py               Example of utility functions for the module
   ├── notebooks/                 Jupyter notebooks. Naming convention is a number (for ordering), the creator's initials,
   │                              and a short `-` delimited description, e.g.  `1.0-jqp-initial-data-exploration`.
   ├── bin/                       Executable python scripts
   │   └── main.py                Main Python script
   │   └── main.bat               Main executable (bash) script
   ├── data/                      Data folder including raw and processed data
   │   ├── interim/               Intermediate data that has been transformed.
   │   ├── processed/             The final, canonical data sets for modeling, visualisation
   │   └── raw/                   The original, immutable data dump.
   ├── resources/                 Data dictionaries, manuals, and all other explanatory materials.
   ├── docs/                      A default Sphinx project; see sphinx-doc.org for details
   ├── models/                    Trained and serialized models, model predictions, or model summaries
   └── reports/                   Generated analysis as HTML, PDF, LaTeX, etc.
   


Project Setup
==============

In order to setup your new project project, please follow the next instructions:


1. Clone the  project from git entreprise platform

.. code-block:: shell

        git clone https://gheprivate.intra.corp/hr-data-lab/TemplateProject.git
        cd TemplateProject

2. Configure the files and folders. At minimum, you'll need to create the following:

README.rst <./README.rst>`_: A description of your project and its goals.
`setup.py <./setup.py>`_: A definition of your package.
`requirements.txt <./requirements.txt>`_: the list of python requirements of your projects.
`config.ini <./config.ini>`_: the project configuration variables.
`logging.ini <./logging.ini>`_: the logging configuration including the path of output log.
`LICENSE <./LICENSE>`_: Your project's license, if it's open source. (See opensource.org for more information about selecting one.)
`.gitignore <./.gitignore>`_: A special file that tells Git what files and directories to ignore. (If you're using another VCS, this file has a different name. Look it up.)
A directory with the name of your project (e.g. `<templateproject>`_).
		
3. Install python requirements

.. code-block:: shell

        pip install -r requirements.txt

If you have limited access to internet, use the next option:

.. code-block:: shell

        pip install --proxy http://[YOUR NG]:[YOUR PASSWORD - URL ENCODED]@fr0-proxylan-vip.eu.airbus.corp:3128 -r requirements.txt


Using the project
=============================
1. Store your data files in `data/raw <./data/raw>`_  folder.

2. Edit the configuration file `config.ini <./config.ini>`_ to setup  paths, file names and project parameters.
Parameters to be edited. Example :

.. code-block:: Python

	# Path to different folders
	[path]
	raw = ../data/raw/
	interim = ../data/interim/
	processed = ../data/processed/


	resources = ../resources
	model = ../models
	reports = ../reports

	# Names of your raw data files to process
	[files]


	# Main script parameters
	[param]


3. Execute main Python script

.. code-block:: shell

        python bin/main.py

4. Merge the generated files in `data/interim <./data/interim>`_  with the Spotfire data file (hosted on SFS dedicated folder). Append new lines to the existing file.

Licenses
========

Copyright 2020, Airbus - All Rights Reserved

Issues
======

Please report any bugs or requests that you have using the  `issue tracker` of github.


Authors
============

* Elodie Bergonnier  `elodie.bergonnier@airbus.com <mailto:elodie.bergonnier@airbus.com>`_

