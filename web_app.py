from flask import Flask, session, json, render_template, request, redirect, url_for, abort, flash, get_flashed_messages, jsonify
import random
import numpy as np
from dataset import display_one_character
from dataset import invert_numbers
from dataset import multiply_examples
import network
from scipy.ndimage.filters import gaussian_filter


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
    image = np.array(incoming["matrix"])
    blurred = gaussian_filter(image, sigma=0.5)
    # display_one_character(blurred)
    dataset = [[np.reshape(blurred, (784, 1)), None]]
    extended_dataset = multiply_examples(dataset)
    # invert_numbers(dataset)
    inputs = [x[0] for x in extended_dataset]
    predictions = nn.predict(inputs)
    prediction = max(predictions, key = predictions.count)
    print(prediction)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
