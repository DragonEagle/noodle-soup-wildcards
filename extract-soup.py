#!/usr/bin/env python

import json
import os
import sys

# Create wildcard path if it doesn't exist
if not os.path.exists("noodle-soup"):
    os.makedirs("noodle-soup")

# Open json file and load contents into variable
with open("nsp_pantry.json") as json_file:
    json_data = json.load(json_file)

# Check if any text files with names matching json arrays exist
for array in json_data:
    if os.path.exists("noodle-soup/" + array + ".txt"):
       text_files_exist = True
       break
    else:
        text_files_exist = False

if text_files_exist:
    while True:
        overwrite = input("WARN: This script will overwrite any changes you may have made to your Noodle Soup wildcards. Would you like to continue? (Y/n) ")
        if overwrite == "Y" or overwrite == "y" or overwrite == "":
            break
        elif overwrite == "N" or overwrite == "n":
            sys.exit()
        else:
            print("Invalid input. Please try again.")

# Iterate through each array
for array in json_data:
    # Store contents of each array in its respective text file
    with open("noodle-soup/" + array + ".txt", "w") as text_file:
        for item in json_data[array]:
            text_file.write(item + "\n")
        print("Created " + array + ".txt")
        text_file.close()

print("NSP extraction complete; your text files are in noodle-soup/")
print("Note that it's not recommended to make any changes directly to these files, as they will be overwritten when updated – make a copy instead.")