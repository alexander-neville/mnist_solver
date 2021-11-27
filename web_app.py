from flask import Flask, session, json, render_template, request, redirect, url_for, abort, flash, get_flashed_messages, jsonify
import random
import numpy as np
from dataset import display_one_character
from main import invert_numbers
import network

app = Flask(__name__)
app.config.from_object(__name__)
nn = network.load("./data/config.json")

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def process_drawing():
    incoming = request.get_json()
    print(incoming)
    dataset = [[np.reshape(np.array(incoming["matrix"]), (784, 1)), None]]
    print(dataset)
    invert_numbers(dataset)
    inputs = [x[0] for x in dataset]
    prediction = int(nn.predict(inputs)[0])
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
