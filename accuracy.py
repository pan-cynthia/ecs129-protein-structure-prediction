import sys
from Bio.PDB import PDBParser
import pandas as pd
import numpy as np
import rmsd_func


if len(sys.argv) != 3:
	raise TypeError(
        "Wrong number of arguments, 3 expected, {} given".format(len(sys.argv)))

#struct1 = sys.argv[2]
#struct2 = sys.argv[3]
#struct3 = sys.argv[4]
#struct4 = sys.argv[5]
#struct5 = sys.argv[6]

#goldSequence = sys.argv[1]

def accuracy():
	print("accuracy function")
	accuracyArray = []
	goldSequence = sys.argv[1]
	for row in range(len(sys.argv)-1):
		struct = sys.argv[row+1]
		rmsd = rmsd_func.main(struct, goldSequence)
		accuracyArray.append(subArray)
	print(accuracyArray)


def main():
	accuracy()

main()	
