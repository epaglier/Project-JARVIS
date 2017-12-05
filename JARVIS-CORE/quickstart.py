from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from datetime import datetime
import time

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def todayDateEnd():
    todayEnd = datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)
    todayEnd += datetime.timedelta(days=1)	# Add extrea dat to rango for GTM deltaset new event at 8:30 am
    todayEnd = todayEnd.isoformat() + 'Z'
    return todayEnd

def tomorrowDateStart():
    tomorrowStart = datetime.datetime.utcnow().replace(hour=00, minute=00, second=01)
    tomorrowStart += datetime.timedelta(days=1)
    tomorrowStart = tomorrowStart.isoformat() + 'Z'
    return tomorrowStart

def tomorrowDateEnd():
    tomorrowEnd = datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)
    tomorrowEnd += datetime.timedelta(days=2)	# Add extrea dat to rango for GTM delta
    tomorrowEnd = tomorrowEnd.isoformat() + 'Z'
    return tomorrowEnd

def otherDateStart(until):
    otherDayStart = datetime.datetime.utcnow().replace(hour=00, minute=00, second=01)
    otherDayStart += datetime.timedelta(days=until)
    otherDayStart = otherDayStart.isoformat() + 'Z'
    return otherDayStart
          
def otherDateEnd(until):
    otherDayEnd = datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)
    otherDayEnd += datetime.timedelta(days=until)
    otherDayEnd = otherDayEnd.isoformat() + 'Z'
    return otherDayEnd

def newDate(day,hours,minutes):
    newDate = datetime.datetime.utcnow().replace(hour=hours, minute=minutes, second=01)
    newDate += datetime.timedelta(days=day)
    newDate = newDate.isoformat() + gmt
    newDate = parse_datetime_string(str(newDate))
    return newDate

def parse_datetime_string(string):
    if '+' in string:
	return datetime.datetime.strptime(string,"%Y-%m-%dT%H:%M:%S+%f")
    else:
	return datetime.datetime.strptime(string,"%Y-%m-%dT%H:%M:%S-%f")

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getNextEvent():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=1, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def createEvent():
    	credentials = get_credentials()
    	http = credentials.authorize(httplib2.Http())
    	service = discovery.build('calendar', 'v3', http=http)
	
	event = {
		'summary': 'summary',
		'description': 'description',
		'start': {
			'dateTime': '2017-12-05T23:00:00-05:00',
			'timeZone': 'America/Indianapolis',
		},
  		'end': {
    			'dateTime': '2017-12-05T23:30:00-05:00',
    			'timeZone': 'America/Indianapolis',
  		},
	}
	created_event = service.events().insert(calendarId='primary', body=event).execute()

def main():
	getNextEvent()
	createEvent()	

if __name__ == '__main__':
    main()
