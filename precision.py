import sys
from Bio.PDB import PDBParser
import pandas as pd
import numpy as np
from rmsd import calc_RMSD, create_structure, get_coordinates

def precision(coord1, coord2, coord3, coord4, coord5):
	print("precision function")
	# rmsd = calc_RMSD(coord1, coord2)
	# print("rmsd: ", rmsd)	
	wholeArray = []
	"""for row in range(len(sys.argv)-1):
		subArray = []
		struct1 = sys.argv[row+1]
		print("row: " + str(row))
		for col in range(len(sys.argv)-1):
	 		struct2 = sys.argv[col+1]
	 		rmsd = calc_RMSD(struct1, struct2)
	 		print("rmsd:", rmsd)
	 		subArray.append(rmsd)
	 		print("col: " + str(col))
		print("subArray: ")
		print(subArray)
		wholeArray.append(subArray)
	"""
	
	# print(calc_RMSD(coord1, coord2))
#	for row in range(len(sys.argv)-1):
#		for col in range(len(sys.argv)-1):
#			print(calc_RMSD("coord"+str(row), "coord"+str(col)))

	subArray1 = []
	pre1_1 = calc_RMSD(coord1, coord1)
	subArray1.append(pre1_1)
	pre1_2 = calc_RMSD(coord1, coord2)
	subArray1.append(pre1_2)
	pre1_3 = calc_RMSD(coord1, coord3)
	subArray1.append(pre1_3)
	pre1_4 = calc_RMSD(coord1, coord4)
	subArray1.append(pre1_4)
	pre1_5 = calc_RMSD(coord1, coord5)
	subArray1.append(pre1_5)
	print(subArray1)	
	wholeArray.append(subArray1)


	subArray2 = []
	pre2_1 = calc_RMSD(coord2, coord1)
	subArray2.append(pre2_1)
	pre2_2 = calc_RMSD(coord2, coord2)
	subArray2.append(pre2_2)
	pre2_3 = calc_RMSD(coord2, coord3)
	subArray2.append(pre2_3)
	pre2_4 = calc_RMSD(coord2, coord4)
	subArray2.append(pre2_4)
	pre2_5 = calc_RMSD(coord2, coord5)
	subArray2.append(pre2_5)      
	# print(subArray2)
	wholeArray.append(subArray2)

	subArray3 = []
	pre3_1 = calc_RMSD(coord3, coord1)
	subArray3.append(pre3_1)
	pre3_2 = calc_RMSD(coord3, coord2)
	subArray3.append(pre3_2)
	pre3_3 = calc_RMSD(coord3, coord3)
	subArray3.append(pre3_3)
	pre3_4 = calc_RMSD(coord3, coord4)
	subArray3.append(pre3_4)
	pre3_5 = calc_RMSD(coord3, coord5)
	subArray3.append(pre3_5)
	# print(subArray3)
	wholeArray.append(subArray3)

	subArray4 = []
	pre4_1 = calc_RMSD(coord4, coord1)
	subArray4.append(pre4_1)
	pre4_2 = calc_RMSD(coord4, coord2)
	subArray4.append(pre4_2)
	pre4_3 = calc_RMSD(coord4, coord3)
	subArray4.append(pre4_3)
	pre4_4 = calc_RMSD(coord4, coord4)
	subArray4.append(pre4_4)
	pre4_5 = calc_RMSD(coord4, coord5)
	subArray4.append(pre4_5)
	# print(subArray4)
	wholeArray.append(subArray4)

	subArray5 = []
	pre5_1 = calc_RMSD(coord5, coord1)
	subArray5.append(pre5_1)
	pre5_2 = calc_RMSD(coord5, coord2)
	subArray5.append(pre5_2)
	pre5_3 = calc_RMSD(coord5, coord3)
	subArray5.append(pre5_3)
	pre5_4 = calc_RMSD(coord5, coord4)
	subArray5.append(pre5_4)
	pre5_5 = calc_RMSD(coord5, coord5)
	subArray5.append(pre5_5)
	# print(subArray5)
	wholeArray.append(subArray5)

	print(wholeArray)			

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
