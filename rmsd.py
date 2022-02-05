import sys
from Bio.PDB import PDBParser
import pandas as pd
import numpy as np
from numpy import linalg as LA

# command to run the program: python3 rmsd.py structure1_file_path structure2_file_path

# command line arguments
# argv[0] = rmsd.py, argv[1] = structure1 file path, argv[2] = structure2 file path

# error handling, check if correct number of arguments passed in
if len(sys.argv) != 3:
    raise TypeError(
        "Wrong number of arguments, 3 expected, {} given".format(len(sys.argv)))

# data preprocessing
def get_coordinates(structure):
    """Isolate lines that correspond to an alpha carbon (CA)
    and extract the coordinates

    Args:
        structure : Structure object created by Biopython library using PDB file

    Returns:
        data (list) : List of coordinates
    """
    data = []
    atoms = structure.get_atoms()
    for atom in atoms:
        if atom.get_name() == "CA":
            data.append(atom.get_coord())
    return data


parser = PDBParser()

# structure 1
structure1 = parser.get_structure("STRUCT-1", sys.argv[1])
coord1 = pd.DataFrame(get_coordinates(structure1), columns=["c1", "c2", "c3"])

# structure 2
structure2 = parser.get_structure("STRUCT-2", sys.argv[2])
coord2 = pd.DataFrame(get_coordinates(structure2), columns=["c1", "c2", "c3"])

# get barycenters
coord1_means = coord1.mean(axis=1)
coord2_means = coord2.mean(axis=1)

# shift the coordinates to the barycenters
def shift_coordinates(coord, means):
    return coord - means

coord1[["c1", "c2", "c3"]] = coord1[["c1", "c2", "c3"]].apply(
    shift_coordinates, means=coord1_means)
coord2[["c1", "c2", "c3"]] = coord2[["c1", "c2", "c3"]].apply(
    shift_coordinates, means=coord2_means)
