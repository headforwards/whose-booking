from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<room>")
def bookings(room):
    return render_template('room.html', name=room)

@app.route("/")
def home():
    return render_template('index.html')