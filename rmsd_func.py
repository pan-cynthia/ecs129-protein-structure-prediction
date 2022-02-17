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


def get_RMSD():
	parser = PDBParser()

	# structure 1
	structure1 = parser.get_structure("STRUCT-1", sys.argv[1])
	coord1 = pd.DataFrame(get_coordinates(structure1), columns=["c1", "c2", "c3"])

	# structure 2
	structure2 = parser.get_structure("STRUCT-2", sys.argv[2])
	coord2 = pd.DataFrame(get_coordinates(structure2), columns=["c1", "c2", "c3"])

	# shift the coordinates by barycenters
	coord1 = coord1 - coord1.mean()
	coord2 = coord2 - coord2.mean()

	# calculate R values
	R11, R12, R13, R21, R22, R23, R31, R32, R33 = [np.dot(coord1[x], coord2[y]) for x in coord1 for y in coord2]

	# generate 4 x 4 F matrix
	F_matrix = [[R11 + R22 + R33, R23 - R32, R31 - R13, R12 - R21],
            [R23 - R32, R11 - R22 - R33, R12 + R21, R13 + R31],
            [R31 - R13, R12 + R21, -R11 + R22 - R33, R23 + R32],
            [R12 - R21, R13 + R31, R23 + R32, -R11 - R22 + R33]]

	# calculate max eigenvalue of F matrix
	w, v = LA.eig(F_matrix)
	eigen_val = max(w)

	# calculate best fit RMSD "e"
	N = len(coord1)
	#sum = sum([np.dot(coord1[x], coord1[x]) + np.dot(coord2[x], coord2[x]) for x in coord1])
	sum_total = sum([np.dot(coord1[x], coord1[x]) + np.dot(coord2[x], coord2[x]) for x in coord1])
	numerator = sum_total - 2 * eigen_val
	if (abs(numerator) < 10**-2):
    		numerator = 0
	e = np.sqrt(numerator/N)
	#print(e)
	return e

def main():
	rmsd = get_RMSD()
	print(rmsd)

main()
