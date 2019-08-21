# -*- coding: utf-8 -*-
#
"""setuptools-based setup.py template for Cython projects.

Main setup for the library.

Supports Python 3.7.

Usage as usual with setuptools:
    python setup.py build_ext # Build the extensions (as shared libraries)
    python setup.py build
    python setup.py install
    python setup.py sdist

For details, see
    http://setuptools.readthedocs.io/en/latest/setuptools.html#command-reference
or
    python setup.py --help
    python setup.py --help-commands
    python setup.py --help bdist_wheel  # or any command
"""

import os

from setuptools import setup, find_packages

#########################################################
# General config
#########################################################

# Name of the top-level package of your library.
#
# This is also the top level of its source tree,
# relative to the top-level project directory setup.py resides in.
libname = "Weisshorn"

# Short description for package list on PyPI
SHORTDESC = "A Python library for seismic wave modelling"

# Long description for package homepage on PyPI
DESC = """A Python library for seismic wave modelling.

The focus of Weisshorn is on numerical scientific projects,
where Dask, numba, and cupy can bring a large speedup.

Supports Python >= 3.7.
"""

# Set up data files for packaging.
#
# Directories (relative to the top-level directory where setup.py resides) in which to look for data files.
#datadirs = () #("test",)

# File extensions to be considered as data files. (Literal, no wildcards.)
#dataexts = (".py",  ".pyx", ".pxd",  ".c", ".cpp", ".h",  ".sh",  ".lyx", ".tex", ".txt", ".pdf")
#dataexts = (".py",)

# Standard documentation to detect (and package if it exists).
standard_docs     = ["README", "LICENSE", "TODO", "CHANGELOG", "AUTHORS"]  # just the basename without file extension
standard_doc_exts = [".md", ".rst", ".txt", ""]  # commonly .md for GitHub projects, but other projects may use .rst or .txt (or even blank).

#########################################################
# Init
#########################################################

# check for Python 3.7 or later
# http://stackoverflow.com/questions/19534896/enforcing-python-version-in-setup-py
import sys
if sys.version_info < (3,7):
    sys.exit('Sorry, Python < 3.7 is not supported')

# Extract __version__ from the package __init__.py
# (since it's not a good idea to actually run __init__.py during the build process).
#
# http://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package
import ast
init_py_path = os.path.join(libname, '__init__.py')
version = '0.0.unknown'
try:
    with open(init_py_path) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            print( "WARNING: Version information not found in '%s', using placeholder '%s'" % (init_py_path, version), file=sys.stderr )
except MyFileNotFoundError:
    print( "WARNING: Could not find file '%s', using placeholder version information '%s'" % (init_py_path, version), file=sys.stderr )

#########################################################
# Call setup()
#########################################################

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
	# https://packaging.python.org/specifications/core-metadata/#name
    name = "weisshorn",

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
	# https://packaging.python.org/en/latest/single_source_version.html
    version = version,

    author = "Filippo Broggini",

    author_email = "nathannever82@gmail.com",

    url = "https://github.com/serendipyty/weisshorn",

    description = SHORTDESC,
    long_description = DESC,

    # CHANGE THIS
    license = "Apache License 2.0",

    # free-form text field; http://stackoverflow.com/questions/34994130/what-platforms-argument-to-setup-in-setup-py-does
    platforms = ["OS Independent"],

    # See
    #    https://pypi.python.org/pypi?%3Aaction=list_classifiers
    #
    # for the standard classifiers.
    #
    # Remember to configure these appropriately for your project, especially license!
    #
    classifiers = [ "Development Status :: 1 - Planning",
                    "Intended Audience :: Developers",
                    "Intended Audience :: Science/Research",
                    "License :: OSI Approved :: Apache Software License",
                    "Operating System :: OS Independent",
                    "Programming Language :: Python",
                    "Programming Language :: Python :: 3.7",
                    "Topic :: Scientific/Engineering",
                    "Topic :: Scientific/Engineering :: Physics"
                  ],

    # See
    #    http://setuptools.readthedocs.io/en/latest/setuptools.html
    #
    install_requires = ["numpy", "sphinx"],

    python_requires = '>=3.7',

    # keywords for PyPI (in case you upload your project)
    #
    # e.g. the keywords your project uses as topics on GitHub, minus "python" (if there)
    #
    keywords = ["setuptools template example"],

    # All extension modules (list of Extension objects)
    #
    #ext_modules = my_ext_modules,

    # To automate compilation of cython files
    #
    #cmdclass={'build_ext': build_ext},

    # Declare packages so that  python -m setup build  will copy .py files (especially __init__.py).
    #
    # This **does not** automatically recurse into subpackages, so they must also be declared.
    #
    packages = find_packages(exclude=['contrib', 'docs', 'tests*']),

    # Install also Cython headers so that other Cython modules can cimport ours
    #
    # Fileglobs relative to each package, **does not** automatically recurse into subpackages.
    #
    # FIXME: force sdist, but sdist only, to keep the .pyx files (this puts them also in the bdist)
#    package_data = {'serendipyty': ['*.pxd', '*.pyx'],
#                    'serendipyty.seismic': ['*.pxd', '*.pyx'],
#                    'serendipyty.seismic.modelling': ['*.pxd', '*.pyx']},
    package_data = {},
    # Disable zip_safe, because:
    #   - Cython won't find .pxd files inside installed .egg, hard to compile libs depending on this one
    #   - dynamic loader may need to have the library unzipped to a temporary directory anyway (at import time)
    #
    zip_safe = False,

    # Custom data files not inside a Python package
#    data_files = datafiles
)

