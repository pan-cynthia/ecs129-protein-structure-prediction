# ECS 129 Project - Protein Structure Prediction  

## Before Running

Install the Biopython library using the following command:
```
pip install biopython
```

## Running
Remember to replace the file path placeholders in the commands below with the file paths on your machine to the structures you want to compare. 

### rmsd.py
To run rmsd.py, use the following command:

```
python3 src/rmsd.py struct1_file_path struct2_file_path
```

### accuracy.py
This program expects 6 different structures as input, with the first being the gold standard.  
To run accuracy.py, use the following command:
```
python3 src/accuracy.py gold_standard_file_path struct1_file_path struct2_file_path struct3_file_path struct4_file_path struct5_file_path
```

### precision.py
This program expects 5 different structures as input, specifically the 5 structures that AlphaFold2 outputs.  
To run precision.py, run the following command:
```
python3 src/precision.py struct1_file_path struct2_file_path struct3_file_path struct4_file_path struct5_file_path
```