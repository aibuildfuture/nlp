from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getResult',methods=['POST'])
def get_result():
    input = request.form['input']
    output = extract(input)
    return input

def extract(input):
    return input
