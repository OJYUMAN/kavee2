import json

# Initialize an empty dictionary to store the combined data
combined_data = {}

# Loop over the 13 JSON files
for i in range(1, 14):
    # Define the file path
    json_file_path = f'new/charset{i:02}.json'
    
    # Open and load the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Merge the data into the combined_data dictionary
    combined_data.update(data)

# Save the combined data to a new JSON file
with open('combined.json', 'w', encoding='utf-8') as json_file:
    json.dump(combined_data, json_file, ensure_ascii=False, indent=4)