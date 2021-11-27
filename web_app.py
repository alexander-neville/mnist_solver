from flask import Flask, session, json, render_template, request, redirect, url_for, abort, flash, get_flashed_messages, jsonify
import random
import numpy as np
from handle_data import display_one_character

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def process_drawing():
    incoming = request.get_json()
    print(incoming)
    display_one_character(np.array(incoming["matrix"]))
    return jsonify({"prediction": random.randint(0,9)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
