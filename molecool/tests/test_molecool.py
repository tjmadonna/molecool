"""
Unit testing for the molecute package.
"""

import sys
import numpy as np
import pytest

import molecool

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules

def test_calculate_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1, 1, 1], [2.4, 1, 1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    calculated_center = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1, 1, 1])

    assert np.array_equal(expected_center, calculated_center)

def test_calculate_molecular_mass(test_molecule):
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)
    
    expected_mass = molecool.data.atomic_weights['C'] + molecool.data.atomic_weights['H'] +\
        molecool.data.atomic_weights['H'] + molecool.data.atomic_weights['H']
    
    assert expected_mass == calculated_mass