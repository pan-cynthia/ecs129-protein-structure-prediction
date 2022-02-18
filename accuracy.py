import sys
import pandas as pd
import numpy as np
from rmsd import calc_RMSD, create_structure, get_coordinates

def accuracy(coords):
	print("accuracy function")
	coords_gold = coords[0]
	accuracy_array = []
	for coord in coords[1:]:
		e = calc_RMSD(coord, coords_gold)
		accuracy_array.append(e)
	print(accuracy_array)

def main():
	# error handling, check if correct number of arguments passed in
	if len(sys.argv) < 3:
		raise TypeError("Wrong number of arguments, at least 3 expected, {} given".format(len(sys.argv)))

	# create structure objects
	structures = []
	for i in range(1,len(sys.argv)):
		structures.append(create_structure("MODEL" + str(i),sys.argv[i]))

	# get coordinates
	coords = []
	for struc in structures:
		coord = pd.DataFrame(get_coordinates(struc), columns=["c1", "c2", "c3"])
		coords.append(coord)

	accuracy(coords)

if __name__ == "__main__":
	main()