import os
import yaml
import requests
from flask import session

# Load the oauth_settings.yml file
stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
login_url = 'https://login.microsoftonline.com/{0}/oauth2/v2.0/token'.format(settings['tenant_id'])

def get_token():
    data = {
        'client_id' : settings['app_id'],
        'scope' : 'https://graph.microsoft.com/.default',
        'client_secret' : settings['app_secret'],
        'grant_type' : 'client_credentials'
    }

    token = requests.post(login_url, data).text
    session['token'] = token
