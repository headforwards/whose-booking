from config import setup
setup()
from flask import Flask, render_template, session, redirect, request, url_for
from auth_helper import get_token
from graph_helper import get_rooms


app = Flask(__name__)
app.secret_key='ajdhjkaghsdfhsdaf'

@app.route("/<room>")
def bookings(room):
    return render_template('room.html', name=room)

@app.route("/")
def home():
    #if session['token'] == '':
    get_token()
    token = get_rooms()
    return render_template('index.html', displaytoken=token)


if __name__ == '__main__':
    app.run(debug=True)