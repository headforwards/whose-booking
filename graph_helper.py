from flask import session
import requests
import os
import datetime
import dateutil.parser
from auth_helper import get_token

graph_url = 'https://graph.microsoft.com/beta'
user_id = os.environ['user_id']

def get_rooms():
    token = get_token()
    url = '{0}/users/{1}/{2}'.format(graph_url, user_id, 'findrooms')
    headers = {"Authorization": "Bearer {0}".format(token)}
    response = requests.get(url, headers=headers).json()
    if 'value' in response:
        return response['value']
    else:
        print(response)
        return []


def get_meetings(room):
    token = get_token()
    today = datetime.date.today().strftime("%Y-%m-%d")
    data = {
        "schedules": [room],
        "startTime": {
            "dateTime": "{0}T08:00:00".format(today),
            "timeZone": "UTC"
        },
        "endTime": {
            "dateTime": "{0}T17:00:00".format(today),
            "timeZone": "UTC"
        },
        "availabilityViewInterval": "60"
    }
    url = '{0}/users/{1}/{2}'.format(graph_url, user_id, 'calendar/getSchedule')
    headers = {
        "Authorization": "Bearer {0}".format(token),
        "Prefer": 'outlook.timezone="Europe/London"'
    }
    schedules = requests.post(url, json=data, headers=headers).json()['value'][0]
    for event in schedules['scheduleItems']:
        event['start']['dateTime'] = dateutil.parser.parse(event['start']['dateTime']).strftime('%H:%M')
        event['end']['dateTime'] = dateutil.parser.parse(event['end']['dateTime']).strftime('%H:%M')
    return schedules
