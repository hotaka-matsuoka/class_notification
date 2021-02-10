from __future__ import print_function
import datetime
import pickle
import os.path
import date
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def schedule_addtion(class_information_list):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    for dict in class_information_list:
        if dict['period'] == '1':
            start_time = '09:00:00'
            end_time = '10:30:00'
        elif dict['period'] == '2':
            start_time = '10:40:00'
            end_time = '12:10:00'
        elif dict['period'] == '3':
            start_time = '13:00:00'
            end_time = '14:30:00'
        elif dict['period'] == '4':
            start_time = '14:40:00'
            end_time = '16:10:30'
        else:
            start_time = '16:20:00'
            end_time = '17:50:30'

        event = {
        'summary': dict['subject'],
        'location': dict['classroom'],
        'description': dict['information'],
        'start': {
            'dateTime': f'{date.year}-{date.month}-{date.day}T{start_time}',
            'timeZone': 'Japan',
        },
        'end': {
            'dateTime': f'{date.year}-{date.month}-{date.day}T{end_time}',
            'timeZone': 'Japan',
        },
        }

        event = service.events().insert(calendarId='matsuhota108@gmail.com',
                                    body=event).execute()
    print (event['id'])
if __name__ == '__main__':
    schedule_addtion()
