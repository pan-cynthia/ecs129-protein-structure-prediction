from Bio.PDB import *
import pandas as pd
import sys

# command to run the program: python3 rmsd.py structure1_file_path structure2_file_path

# command line arguments
# argv[0] = rmsd.py, argv[1] = structure1 file path, argv[2] = structure2 file path

# error handling, check if correct number of arguments passed in
if len(sys.argv) != 3:
    raise TypeError("Wrong number of arguments, 3 expected, {} given".format(len(sys.argv)))

# data preprocessing
def getCoordinates(structure):
    """
    Isolate lines that correspond to an alpha carbon (CA)
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
structure = parser.get_structure("STRUCT-1", sys.argv[1])
coord1 = pd.DataFrame(getCoordinates(structure), columns = ["x", "y", "z"])

# structure 2
structure = parser.get_structure("STRUCT-2", sys.argv[2])
coord2 = pd.DataFrame(getCoordinates(structure), columns = ["x", "y", "z"])