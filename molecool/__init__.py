"""
molecool
A python package for analyzing and visualizing molecules for the MolSSI Best Practices workshop.
"""

# Add imports here
from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list, calculate_center_of_mass, calculate_molecular_mass
from .visualize import draw_molecule, bond_histogram

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
