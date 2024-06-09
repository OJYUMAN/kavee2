from flask import Flask, render_template, request, jsonify
import ssg
from dictionary import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', text=[])

@app.route('/api/button_click', methods=['POST'])#หาคําคล้องจอง
def button_click():
    
    data = request.get_json()
    word = data['word']
    text2 = ssg.syllable_tokenize(word)#cut the word into syllables
    text44 = text2[-1]#get the last syllable
    #print(text44)
    wordinfo = matchingsound(text44) # get the information of the words returned as the list of pairs
    #print(wordinfo)
    definitions = [x[0] for x in wordinfo] # loop through the list of pairs
    words = [x[1] for x in wordinfo]
    # words = getword(text44)#get the words that have the same sound as the input text
    
    return jsonify(definitions, words) #, words
   

@app.route('/api/button_click2', methods=['POST'])
def button_click2():
    data = request.get_json()
    word = data['word']
   
    wordinfo = matchingword(word) # get the information of the words returned as the list of pairs
    
    definitions = [x[0] for x in wordinfo] # loop through the list of pairs
    words = [x[1] for x in wordinfo]
   
   
    return jsonify(words, definitions) #, words #, words




@app.route('/page2')
def next_page():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True)
