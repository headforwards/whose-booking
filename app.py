from flask import Flask, render_template, session, redirect, request, url_for
from auth_helper import get_sign_in_url, get_token_from_code

app = Flask(__name__)
app.secret_key='ajdhjkaghsdfhsdaf'

@app.route("/<room>")
def bookings(room):
    return render_template('room.html', name=room)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/sign-in")
def sign_in():
    # Get the sign-in URL
    sign_in_url, state = get_sign_in_url()
    # Save the expected state so we can validate in the callback
    session['auth_state'] = state
    # Redirect to the Azure sign-in page
    return redirect(sign_in_url)

@app.route("/callback")
def callback():
    # Get the state saved in session
    expected_state = session.pop('auth_state', '')
    # Make the token request
    token = get_token_from_code(request.url, expected_state)
    #Temporary! Save the response in an error so it's displayed
    session['flash_error'] = { 'message': 'Token retrieved', 'debug': format(token) }
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)