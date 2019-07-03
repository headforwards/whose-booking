import os
import yaml
import requests
from flask import session

# Load the oauth_settings.yml file
login_url = 'https://login.microsoftonline.com/{0}/oauth2/v2.0/token'.format(os.environ['tenant_id'])

def get_token():
    data = {
        'client_id' : os.environ['app_id'],
        'scope' : 'https://graph.microsoft.com/.default',
        'client_secret' : os.environ['app_secret'],
        'grant_type' : 'client_credentials'
    }
    try:
        token = requests.post(login_url, data).json()
        session['token'] = token['access_token']
    except Exception as e:
        print(e)
        pass
