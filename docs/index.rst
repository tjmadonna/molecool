.. molecool documentation master file, created by
   sphinx-quickstart on Thu Mar 15 13:55:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to molecool's documentation!
=========================================================
molecool is a Python package designed to read in, perform analysis, and visualize molecular coordinates. The file format `xyz` and `pdb` are currently supported.

molecool is currently under development and can not yet be installed from PyPI or conda.

Installation
------------
**These instructions assume you have the python package manager conda installed.**

To install molecool, navigation to the GitHub repository and clone it.

To do a developmental install, type

``pip install -e .``

Dependencies
^^^^^^^^^^^^
You need to install numpy and matplotlib

Usage
-----
Once installed, you can use the package. This example draws a benzene molecule from an xyz file.::

    import molecool

    benzene_symbols, benzene_coors = molecool.open_xyz('benzene.xyz')

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   about
   getting_started
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
