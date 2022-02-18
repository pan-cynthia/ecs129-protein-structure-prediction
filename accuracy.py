import sys
import pandas as pd
import numpy as np
from rmsd import calc_RMSD, create_structure, get_coordinates

def accuracy(coord_gold, coord1, coord2, coord3, coord4, coord5):
	print("accuracy function")
	# accuracy_array = []
	# for row in range(len(sys.argv)-1):
	# 	struct = sys.argv[row+1]
	# 	rmsd = rmsd_func.main(struct, goldSequence)
	# 	accuracyArray.append(subArray)
	# 	print(accuracyArray)

def main():
	# error handling, check if correct number of arguments passed in
	if len(sys.argv) != 7:
		raise TypeError("Wrong number of arguments, 7 expected, {} given".format(len(sys.argv)))

	# create structure objects
	gold_standard = create_structure("GOLD", sys.argv[1])
	model1 = create_structure("MODEL-1", sys.argv[2])
	model2 = create_structure("MODEL-2", sys.argv[3])
	model3 = create_structure("MODEL-3", sys.argv[4])
	model4 = create_structure("MODEL-4", sys.argv[5])
	model5 = create_structure("MODEL-5", sys.argv[6])

	# get coordinates
	coord_gold = pd.DataFrame(get_coordinates(gold_standard), columns=["c1", "c2", "c3"])
	coord1 = pd.DataFrame(get_coordinates(model1), columns=["c1", "c2", "c3"])
	coord2 = pd.DataFrame(get_coordinates(model2), columns=["c1", "c2", "c3"])
	coord3 = pd.DataFrame(get_coordinates(model3), columns=["c1", "c2", "c3"])
	coord4 = pd.DataFrame(get_coordinates(model4), columns=["c1", "c2", "c3"])
	coord5 = pd.DataFrame(get_coordinates(model5), columns=["c1", "c2", "c3"])

	accuracy(coord_gold, coord1, coord2, coord3, coord4, coord5)

if __name__ == "__main__":
	main()
