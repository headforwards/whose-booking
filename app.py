from config import setup
setup()
from flask import Flask, render_template, session, redirect, request, url_for
from auth_helper import get_token
from graph_helper import get_rooms, get_meetings

app = Flask(__name__)
app.secret_key='ajdhjkaghsdfhsdaf'


@app.route("/<room>/<name>")
def bookings(room, name):
    get_token()
    meetings = get_meetings(room)
    return render_template('room.html', meetings=meetings, name=name)

@app.route("/")
def home():
    get_token()
    rooms = get_rooms()
    return render_template('index.html', rooms=rooms)


if __name__ == '__main__':
    app.run(debug=True)