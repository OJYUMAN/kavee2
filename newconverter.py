import json
import pythainlp
from pythainlp.corpus.common import thai_words, thai_syllables, thai_negations, thai_stopwords, thai_family_names, thai_female_names, thai_male_names, countries, provinces
from ssg import syllable_tokenize
import re
from phonetic import *

# Generate a new json file with words as the key and the phonetic of the last syllable as the value
    # This is used to skip findword(), cutdictionaryword() entirely, improving the performance
with open('cleaned.json', 'r', encoding="utf8") as f: # Load the JSON file
     dic = json.load(f)
all_last_words = []

# get the last syllable and put them all in all_last_words
for x in dic:
   # print(x)
    
    # Remove ๑ ๒ ๓ ๔ ๕ ๖ ๗ and - from w
    w = x.replace("๑", "").replace("๒", "").replace("๓", "").replace("๔", "").replace("๕", "").replace("๖", "").replace("๗", "").replace("๘", "").replace("๙", "").replace("-", "").replace("ๆ", "")
    
    w = w.replace(' ', '')

    w = syllable_tokenize(w)
    w = str(w[-1])
    all_last_words.append(w)
    

all_last_phonetic = []
for x in all_last_words:
    all_last_phonetic.append(rhyme(x))


# Generate a new json file with words as the key and the phonetic of the last syllable as the value
the_actual_dict = dict()
for indexing, x in enumerate(dic.keys()):
    the_actual_dict[x] = all_last_phonetic[indexing]
#print(the_actual_dict)

with open('newconverter.json', 'w', encoding="utf8") as g:
    json.dump(the_actual_dict, g, ensure_ascii=False, indent=4)