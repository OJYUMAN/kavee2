import json
import re

# Load the JSON file
file_path = 'dictionarycombined.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Function to strip HTML tags from a string
def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Apply the function to all strings in the dictionary
cleaned_data = {k: strip_html_tags(v) for k, v in data.items()}

# Save the cleaned data to a new JSON file
cleaned_file_path = 'cleaned.json'
with open(cleaned_file_path, 'w', encoding='utf-8') as cleaned_file:
    json.dump(cleaned_data, cleaned_file, ensure_ascii=False, indent=4)

print(f"Cleaned JSON file saved to {cleaned_file_path}")
