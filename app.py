# save this as app.py
from flask import Flask, Response


app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, Patrick!</p>"

@app.route("/welcome")
def welcome():
    response_text = '{"message": "Hello, welcome to sdetAutomation flask-api" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response