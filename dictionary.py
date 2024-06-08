import json
import pythainlp
from pythainlp.corpus.common import thai_words, thai_syllables, thai_negations, thai_stopwords, thai_family_names, thai_female_names, thai_male_names, countries, provinces
from ssg import syllable_tokenize
import re
from phonetic import *

def matchingword(text):
    
    with open('cleaned.json', 'r', encoding="utf8") as f: # Load the JSON file
        data = json.load(f)
    
    # Find words that contain the input text
    matching_words = [word for word in data if text in word and word != text]

    for word in matching_words: # Print the matching words
        print(word, data[word])


def matchingsound(text):
    
    with open('cleaned.json', 'r', encoding="utf8") as f:# Load the JSON file
        dic = json.load(f)
    
    phonetic_form = rhyme(text)#change the input text to phonetic form
    print(phonetic_form)

    # to only use the last syllable of the word cutting all syllables before then keep it in "data"
    # data = cutdictionaryword(dic)
    #print(len(data))

    # Find words from datas that have the same sound as the input text then return the index of the words
    # index = findword(data, phonetic_form)

    with open('converter.json', 'r', encoding="utf8") as g: # Load the converter JSON file
        conv = json.load(g)
    all_of_the_phonetics = conv.values()

    index = []
    for ind, x in enumerate(all_of_the_phonetics):
        if x == phonetic_form:
            index.append(ind)

    print(index)
    print(len(index))


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
def getword(text):
    with open('cleaned.json', 'r', encoding="utf8") as f:# Load the JSON file
        dic = json.load(f)

    phonetic_form = rhyme(text)  # change the input text to phonetic form
    print(phonetic_form)

    # to only use the last syllable of the word cutting all syllables before then keep it in "data"
    # data = cutdictionaryword(dic)
    # print(len(data))

    # Find words from datas that have the same sound as the input text then return the index of the words
    # index = findword(data, phonetic_form)

    with open('converter.json', 'r', encoding="utf8") as g:  # Load the converter JSON file
        conv = json.load(g)
    all_of_the_phonetics = conv.values()

    index = []
    for ind, x in enumerate(all_of_the_phonetics):
        if x == phonetic_form:
            index.append(ind)

    print(index)
    print(len(index))

    words = []
    for i in index:
        words.append(list(dic.keys())[i])

    return words



    


########

def cutdictionaryword(data0):
    # to only use the last syllable of the word cutting all syllables before
    # ปฏิบัติ -> บัติ, ตำรวจ -> รวจ (ไม่ได้เช็คว่าถูกหมดไหม)
    datas = []
    for x in data0:
        w = syllable_tokenize(x)
        w = str(w[-1])
        #print(w)
        datas.append(w)
    # then the last syllables are kept in "data"
    # open("CutDict.txt", "w", encoding="utf8").write("\n".join(datas))
    return datas



# def dicphonetic(data):
#     # change "data" to phonetic form then keep it in "datas"
#     datas = []
#     for x in data:
#         y = rhyme(x)
#         datas.append(y)

#     return datas



def findword(datas, phonetic_form):
    newwords = []
    index = []
    # this loops through the list "datas" and find every entry that rhymes (returns as a list of index
    # of the matched entry)
    for index_of_word, x in enumerate(datas): # Find words that have the same sound as the input text
        y = rhyme(x)
        if phonetic_form == y:
            newwords.append(x)
            index.append(index_of_word)

    return index
"""

"""

def getwordinfo(index, dic):
    # Get the information of the words
    for i in index:
        print(list(dic.keys())[i], dic[list(dic.keys())[i]])
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
        json.dump(the_actual_dict, g, ensure_ascii=False, indent=4)