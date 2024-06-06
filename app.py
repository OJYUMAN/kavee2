from flask import Flask, render_template, request, jsonify
import ssg
from dictionary import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/button_click', methods=['POST'])#หาคําคล้องจอง
def button_click():
    data = request.get_json()
    word = data['word']
    text2 = ssg.syllable_tokenize(word)#cut the word into syllables
    text44 = text2[-1]#get the last syllable
    #matchingword(text44)
    matchingsound(text44)
    
    return jsonify(message='Button was clicked!')

@app.route('/page2')
def next_page():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True)
