from flask import Flask, jsonify, send_file
import random

app = Flask(__name__)
quotes = [
    "No one can make you feel inferior without your consent.",
    "Always aim high, work hard, and care deeply about what you believe in. And, when you stumble, keep faith. And, when you're knocked down, get right back up and never listen to anyone who says you can't or shouldn't go on.",
    "Don't let anyone speak for you, and don't rely on others to fight for you.",
    "If you don't like the road you're walking, start paving another one.",
    "Be the change you wish to see in the world.",
    "Believe in yourself!",
    "Stay positive, work hard, make it happen.",
    "Every day is a second chance.",
    "Dream big and dare to fail.",
    "Push yourself, because no one else is going to do it for you.",
    "Never be limited by other people's limited imaginations.",
    "The only impossible journey is the one you never begin.",
    "All our dreams can come true, if we have the courage to pursue them.",
    "Take the first step in faith. You don't have to see the whole staircase, just take the first step.",
    "Don't wait. The time will never be just right.",
    "The greater the obstacle, the more glory in overcoming it.",
    "The man who moves a mountain begins by carrying away small stones.",
    "Great things are not done by impulse, but by a series of small things brought together."
]
@app.route('/')
def home():
    return send_file("index.html")

@app.route('/style.css')
def css():
    return send_file("style.css")

@app.route('/quote')
def quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True)