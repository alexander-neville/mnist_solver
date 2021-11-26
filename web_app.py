from flask import Flask, session, json, render_template, request, redirect, url_for, abort, flash, get_flashed_messages, jsonify

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
    return jsonify({"status": 1})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
