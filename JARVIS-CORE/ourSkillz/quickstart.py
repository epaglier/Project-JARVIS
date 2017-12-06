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
        startArr = start.split("T")
        hourOfE = startArr[1]
        hourOfEArr = hourOfE.split(":")
        resHour = hourOfEArr[0]
        return ("Next Appointment is at " + resHour + " hundred hours. The appointment is " + event['summary'] + "  .Description " + event['description'])

def createEvent(summary, description, time):
    	credentials = get_credentials()
    	http = credentials.authorize(httplib2.Http())
    	service = discovery.build('calendar', 'v3', http=http)
	timeEnd = time + 1
	event = {
		'summary': summary,
		'description': description,
		'start': {
			'dateTime': '2017-12-06T' + str(time) + ':00:00-05:00',
			'timeZone': 'America/Indianapolis',
		},
  		'end': {
    			'dateTime': '2017-12-06T' + str(timeEnd) + ':00:00-05:00',
    			'timeZone': 'America/Indianapolis',
  		},
	}
	created_event = service.events().insert(calendarId='primary', body=event).execute()

def respond(array):
    if "appointment" in array:
        return 20
    else:
        return 0

def handle_input(string):
    
    if "retrieve" in string:
        print("recognized retrieve")
        return getNextEvent()
   
    if "create" in string:
        #create appointment at thirteen summary shoot pool description pool with martin daneil and evan     
        #2017-12-05T23:00:00-05:00 summary

        arr = string.split(" ")
        atIndex = arr.index("at")
        summaryIndex = arr.index("summary")
        descIndex = arr.index("description")
        
        at = ""
        i = atIndex + 1
        while i < summaryIndex:
            at = at + arr[i] + " "
            i = i + 1
        
        at = at[:-1] 
        time = int(at)


        summary = ""
        i = summaryIndex + 1
        while i < descIndex:
            summary = summary + arr[i] + " "
            i = i + 1
        
        description = ""
        i = descIndex + 1
        while i < len(arr):
            description = description + arr[i] + " "
            i = i + 1
         
        createEvent(summary, description, time)
        return "created event"
    return "specify retrieve or get for your appointment"
