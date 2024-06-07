#this script is used to convert the charset.js files to json files for easier access

import json
import re

for i in range(1,14):
    # Read the entire file content
    file_path = f'Data/charset{i:02}.js'
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    # Use regex to extract data from the arrays
    pattern = re.compile(r'K_W\[(\d+)\]="(.*?)";M_W\[\d+\]="(.*?)";D_T\[\d+\]="(.*?)";')
    matches = pattern.findall(file_contents)

    # Create a dictionary to store the JSON data
    data = {}
    for match in matches:
        index, k_w, m_w, d_t = match
        data[m_w] = d_t

    # Convert the dictionary to a JSON formatted string
    json_data = json.dumps(data, ensure_ascii=False, indent=4)

    # Save the JSON data to a file
    json_file_path = f'new/charset{i:02}.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

