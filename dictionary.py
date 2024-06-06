import json
import pythainlp
from pythainlp.corpus.common import thai_words, thai_syllables, thai_negations, thai_stopwords, thai_family_names, thai_female_names, thai_male_names, countries, provinces
from ssg import syllable_tokenize
import re
from phonetic import *

def matchingword(text):
    
    with open('dictionarycombined.json', 'r') as f:# Load the JSON file
        data = json.load(f)
    
    # Find words that contain the input text
    matching_words = [word for word in data if text in word and word != text]

    for word in matching_words:# Print the matching words
        print(word, data[word])


def matchingsound(text):
    
    with open('dictionarycombined.json', 'r') as f:# Load the JSON file
        dic = json.load(f)
    
    phonetic_form = rhyme(text)#change the input text to phonetic form
    print(phonetic_form)

    # to only use the last syllable of the word cutting all syllables before then keep it in "data"
    data = cutdictionaryword(dic)
    #print(len(data))

    #datas = dicphonetic(data)# change "data" to phonetic form then keep it in "datas"
    #print(len(datas))

    newwords = findword(data, phonetic_form)# Find words from datas that have the same sound as the input text
    print(newwords)
    print(len(newwords))
    


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
    return datas



def dicphonetic(data):
    # change "data" to phonetic form then keep it in "datas"
    datas = []
    for x in data:
        y = rhyme(x)
        datas.append(y)

    return datas



def findword(datas, phonetic_form):
    newwords = []
    for x in datas:# Find words that have the same sound as the input text
        y = rhyme(x)
        if phonetic_form == y:
            newwords.append(x)

    return newwords
    



