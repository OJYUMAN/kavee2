import json

text = "นัน";

# Load the JSON file
with open('dictionarycombined.json', 'r') as f:
    data = json.load(f)

# Find words that contain the input text
matching_words = [word for word in data if text in word and word != text]

# Print the matching words
for word in matching_words:
    print(word, data[word])

# # Check if the word exists in the JSON data
# if text in data:
#     #print(f"The word {text} exists in the JSON data.")
#     print(text, data[text])  # Fixed the issue by closing the opening parenthesis after "text"
# else:

#     print(f"The word {text} does not exist in the JSON data.")


# Print a specific word
#print(data[text])