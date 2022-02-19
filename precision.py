import sys
import pandas as pd
from rmsd import calc_RMSD, create_structure, get_coordinates

def precision(coordinates):
    precision = []
    for row in coordinates:
        subarray = []
        for col in coordinates:
            rmsd = calc_RMSD(row, col)
            subarray.append(rmsd)
        precision.append(subarray)
    
    model_names = ["Model 1", "Model 2", "Model 3", "Model 4", "Model 5"]
    print(pd.DataFrame(precision, index = model_names, columns = model_names))

def main():
    # error handling, check if correct number of arguments passed in
    if len(sys.argv) != 6:
        raise TypeError("Wrong number of arguments, 6 expected, {} given".format(len(sys.argv)))

    # create structure objects
    structures = []
    for i in range(1, len(sys.argv)):
        struc = create_structure("MODEL" + str(i), sys.argv[i])
        structures.append(struc)

    # get coordinates
    coordinates = []
    for struc in structures:
        coord = pd.DataFrame(get_coordinates(struc), columns = ["c1", "c2", "c3"])
        coordinates.append(coord)
    
    precision(coordinates)

if __name__ == "__main__":
    main()