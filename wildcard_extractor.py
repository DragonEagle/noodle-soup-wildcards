#!/usr/bin/env python

import json
import os

# Open the json file
with open('nsp_pantry.json') as json_file:
    data = json.load(json_file)

# Create the output directory if it does not exist
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# Iterate through each array in the json file
for key in data:
    # Create a file for each array
    with open('outputs/' + key + '.txt', 'w') as output_file:
        # Iterate through each item in the array
        for item in data[key]:
            # Write each item to the file
            output_file.write(item + '\n')
        print('Created file: ' + key + '.txt')
        output_file.close()

json_file.close()