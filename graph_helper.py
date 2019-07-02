from flask import session
import requests
import os

graph_url = 'https://graph.microsoft.com/beta'
user_id = os.environ['user_id']

def get_rooms():
    url = '{0}/users/{1}/{2}'.format(graph_url, user_id, 'findrooms')
    headers = {"Authorization": "Bearer {0}".format(session['token'])}
    response = requests.get(url, headers=headers).json()
    return response





