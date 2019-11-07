import numpy as np

def open_pdb(file_location):
    """
    Open and read coordinates from a PDB file

    The PDB file must specify the atom elements in the last column and follow
    the conventions outlined in the PDB format specification.

    Parameters
    ----------
    file_location : str
        Location of the PDB file to read
    
    Returns
    -------
    symbols : list
        Atomic symbols of the PDB file
    np_coordinates : np.ndarray
        Atomic coordinates of the PDB file
    """

    with open(file_location) as file:
        data = file.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)
    np_coordinates = np.array(coordinates)

    return symbols, np_coordinates