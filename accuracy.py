import sys
import pandas as pd
from rmsd import calc_RMSD, create_structure, get_coordinates

def accuracy(coords):
    coords_gold = coords[0]
    accuracy = []
    for coord in coords[1:]:
        e = calc_RMSD(coord, coords_gold)
        accuracy.append(e)
    print(pd.DataFrame([accuracy], index = ["Accuracy"], columns = ["Model 1", "Model 2", "Model 3", "Model 4", "Model 5"]))

def main():
    # error handling, check if correct number of arguments passed in
    if len(sys.argv) != 7:
        raise TypeError("Wrong number of arguments, 7 expected, {} given".format(len(sys.argv)))

    # create structure objects
    structures = []
    for i in range(1,len(sys.argv)):
        struc = create_structure("MODEL" + str(i),sys.argv[i])
        structures.append(struc)

    # get coordinates
    coords = []
    for struc in structures:
        coord = pd.DataFrame(get_coordinates(struc), columns = ["c1", "c2", "c3"])
        coords.append(coord)

    accuracy(coords)

if __name__ == "__main__":
    main()