import sys
from Bio.PDB import PDBParser
import pandas as pd
import numpy as np
import rmsd_func


if len(sys.argv) != 3:
	raise TypeError(
        "Wrong number of arguments, 3 expected, {} given".format(len(sys.argv)))

#struct1 = sys.argv[1]
#struct2 = sys.argv[2]
#struct3 = sys.argv[3]
#struct4 = sys.argv[4]
#struct5 = sys.argv[5]

def precision():
	print("precision function")
	#rmsd = rmsd_func.main(struct1, struct2)
	#print("rmsd: ")	
	wholeArray = []
	for row in range(len(sys.argv)-1):
		subArray = []
		struct1 = sys.argv[row+1]
		print("row: " + str(row))
		for col in range(len(sys.argv)-1):
			struct2 = sys.argv[col+1]
			rmsd = rmsd_func.main(struct1, struct2)
			print("rmsd:")
			print(rmsd)
			subArray.append(rmsd)
			print("col: " + str(col))
		print("subArray: ")
		print(subArray)
		wholeArray.append(subArray)
	print("wholeArray")
	print(wholeArray)

#def accuracy():
	#print("accuracy function")
				

def main():
	precision()
	#accuracy()

main()	
