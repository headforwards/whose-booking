from config import setup
setup()
from flask import Flask, render_template, session, redirect, request, url_for
from auth_helper import get_token
from graph_helper import get_rooms, get_meetings

app = Flask(__name__)
app.secret_key='ajdhjkaghsdfhsdaf'

roomUrls = {
    "opie.thompson@headforwards.com": "https://outlook.office365.com/owa/calendar/db2bbb56063346f68c7416222c49f340@headforwards.com/8e1ba97c6a6749ddb20ceac13bfa01e11353762437929719530/calendar.html", #thompson
    "opie.liskov@headforwards.com": "http://outlook.office365.com/owa/calendar/4c9496f85f904f7286fc4fb2d2365a62@headforwards.com/5f4c4a8c13d64de68deee8fa642cba3517947868822812662980/calendar.html", #liskov
    "opie.newman@headforwards.com": "http://outlook.office365.com/owa/calendar/2e4e6143c7ff4de9ab6e5aeae3aea647@headforwards.com/274393823c1f4f5f98851bf2247f7e7c9740793119705658626/calendar.html", #newman
    "opie.hamilton@headforwards.com": "http://outlook.office365.com/owa/calendar/e49354d94fbf484f9b2c85e62ab925a2@headforwards.com/5a9a650be6304edd97e48833dfc556c713049660601462722245/calendar.html", #hamilton
    "pic.s18@headforwards.com": "http://outlook.office365.com/owa/calendar/cef28e595bae44e29c6f798c341c6923@headforwards.com/efc32ddb717c428580c88804431ae5ba6986522120498447319/calendar.html", #s18
    "pic.green@headforwards.com": "http://outlook.office365.com/owa/calendar/90a73bc735a24e1a80d8353ea2eb85c1@headforwards.com/98b70a3fc9b1443782a72ffc26ac53b56222321996911569098/calendar.html", #green
    "pic.meetingrooms@headforwards.com": "http://outlook.office365.com/owa/calendar/d1250939d2be405582a57a6e932d58e1@headforwards.com/eb2b759d0d5a42919aec15effe6ea2ea15405909583009543192/calendar.html", #charged
}


@app.route("/<room>/<name>")
def bookings(room, name):
    meetings = get_meetings(room)
    return render_template('room.html', meetings=meetings, name=name, link=roomUrls[room])

@app.route("/")
def home():
    rooms = get_rooms()
    return render_template('index.html', rooms=rooms)


if __name__ == '__main__':
    app.run(debug=True)