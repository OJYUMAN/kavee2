import json
import pythainlp
from pythainlp.corpus.common import thai_words, thai_syllables, thai_negations, thai_stopwords, thai_family_names, thai_female_names, thai_male_names, countries, provinces
from ssg import syllable_tokenize
import re
from phonetic import *

def matchingword(text):
    
    with open('cleaned.json', 'r', encoding="utf8") as f: # Load the JSON file
        data = json.load(f)

    # check if the word exists in the JSON data
    matching_words = [word for word in data if word == text]

    thai_numbers = {1: '๑', 2: '๒', 3: '๓', 4: '๔', 5: '๕', 6: '๖', 7: '๗', 8: '๘', 9: '๙', 10: '๑๐'}

    if(len(matching_words) == 0):#if the word does not exist in the JSON data
        for i in range(1, 11):#loop for adding thai numbers to the input text

            #add thai numbers to the input text and keep it in newword
            newword = text + ' ' + thai_numbers[i]

            #check if the new word exists in the JSON data and keep it in matchw
            matchw = [word for word in data if word == newword]
            print(matchw)
            if matchw != []:#if the new word exists in the JSON data
                matching_words.extend(matchw)
 
    print(matching_words)

    datas = []

    for word in matching_words: # Print the matching words
        datas.append([word, data[word]])
       # print(word, data[word])
    
    return datas







def matchingsound(text):
    
    with open('cleaned.json', 'r', encoding="utf8") as f:# Load the JSON file
        dic = json.load(f)
    
    phonetic_form = rhyme(text)#change the input text to phonetic form
    #print(phonetic_form)

    with open('newconverter.json', 'r', encoding="utf8") as g: # Load the converter JSON file
        conv = json.load(g)
    all_of_the_phonetics = conv.values()

    index = []
    for ind, x in enumerate(all_of_the_phonetics):
        if x == phonetic_form:
            index.append(ind)

    print("index:",index)


    wordsinfo = []
     # Get the information of the words
    list_of_keys = list(dic.keys())
    for i in index:
        the_word = list_of_keys[i]
        # print(the_word)
        worddara = dic[the_word]
        wordsinfo.append([worddara, the_word])
        
    #print(wordsinfo)
    return wordsinfo


"""
if __name__ ==  "__main__":
    # Generate a new json file with words as the key and the phonetic of the last syllable as the value
    # This is used to skip findword(), cutdictionaryword() entirely, improving the performance
    with open('cleaned.json', 'r', encoding="utf8") as f: # Load the JSON file
        dic = json.load(f)
    all_last_words = []

    # get the last syllable and put them all in all_last_words
    for x in dic:
        w = syllable_tokenize(x)
        w = str(w[-1])
        # print(w)
        all_last_words.append(w)

    all_last_phonetic = []
    for x in all_last_words:
        all_last_phonetic.append(rhyme(x))

    # Generate a new json file with words as the key and the phonetic of the last syllable as the value
    the_actual_dict = dict()
    for indexing, x in enumerate(dic.keys()):
        the_actual_dict[x] = all_last_phonetic[indexing]
    print(the_actual_dict)

    with open('converter.json', 'w', encoding="utf8") as g:
        json.dump(the_actual_dict, g, ensure_ascii=False, indent=4)"""