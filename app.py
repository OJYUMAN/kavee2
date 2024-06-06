from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/button_click', methods=['POST'])
def button_click():
    data = request.get_json()
    word = data['word']
    print(word)
    # Process the email...
    return jsonify(message='Button was clicked!')

@app.route('/page2')
def next_page():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True)
