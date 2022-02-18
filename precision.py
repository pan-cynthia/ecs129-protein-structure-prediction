import sys
from Bio.PDB import PDBParser
import pandas as pd
import numpy as np
from rmsd import calc_RMSD, create_structure, get_coordinates

def precision(coord1, coord2, coord3, coord4, coord5):
	print("precision function")
	rmsd = calc_RMSD(coord1, coord2)
	print("rmsd: ", rmsd)	
	# wholeArray = []
	# for row in range(len(sys.argv)-1):
	# 	subArray = []
	# 	struct1 = sys.argv[row+1]
	# 	print("row: " + str(row))
	# 	for col in range(len(sys.argv)-1):
	# 		struct2 = sys.argv[col+1]
	# 		rmsd = rmsd_func.main(struct1, struct2)
	# 		print("rmsd:", rmsd)
	# 		subArray.append(rmsd)
	# 		print("col: " + str(col))
	# 	print("subArray: ")
	# 	print(subArray)
	# 	wholeArray.append(subArray)
	# print("wholeArray")
	# print(wholeArray)			

def main():
	# error handling, check if correct number of arguments passed in
	if len(sys.argv) != 6:
		raise TypeError("Wrong number of arguments, 6 expected, {} given".format(len(sys.argv)))

	# create structure objects
	model1 = create_structure("MODEL-1", sys.argv[1])
	model2 = create_structure("MODEL-2", sys.argv[2])
	model3 = create_structure("MODEL-3", sys.argv[3])
	model4 = create_structure("MODEL-4", sys.argv[4])
	model5 = create_structure("MODEL-5", sys.argv[5])

	# get coordinates
	coord1 = pd.DataFrame(get_coordinates(model1), columns=["c1", "c2", "c3"])
	coord2 = pd.DataFrame(get_coordinates(model2), columns=["c1", "c2", "c3"])
	coord3 = pd.DataFrame(get_coordinates(model3), columns=["c1", "c2", "c3"])
	coord4 = pd.DataFrame(get_coordinates(model4), columns=["c1", "c2", "c3"])
	coord5 = pd.DataFrame(get_coordinates(model5), columns=["c1", "c2", "c3"])
	
	precision(coord1, coord2, coord3, coord4, coord5)

if __name__ == "__main__":
	main()
