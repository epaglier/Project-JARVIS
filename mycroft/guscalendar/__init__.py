from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message

from mycroft.configuration import ConfigurationManager
from mycroft.util import record, play_mp3
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client import file
import datetime
import calendar
import time

from os.path import dirname, abspath, join, expanduser
import sys

import json
from json import JSONEncoder
import subprocess
import tzlocal
from astral import Astral

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

    

#google funciton to get credentials
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
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')
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

class Calendar_Mutator:
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    
    def setEvent(self,event, location, description, ):
        event = {
            'summary': event,
            'location': location,
            'description': description,
            'start': {
                    'dateTime': '2017-10-05T09:00:00-07:00',
                    'timeZone': 'America/Los_Angeles',
            },
            'end': {
                    'dateTime': '2017-10-06T17:00:00-07:00',
                    'timeZone': 'America/Los_Angeles',
            },
            'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 24 * 60},
                        {'method': 'popup', 'minutes': 10},
                    ],
            },
        }
        
        event = Calendar_Mutator.service.events().insert(calendarId='primary', body=event).execute()
        print('Event = ', (event.get('htmlLink')))        
    
    def getXEvents(self, numEvents):
        print('Getting the upcoming ', numEvents)
         
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        
        eventsResult = Calendar_Mutator.service.events().list(
          calendarId='primary', timeMin = now, maxResults=numEvents, singleEvents=True,
          orderBy='startTime').execute()
        events = eventsResult.get('items', [])
        
        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
    
    def getEventsForDay():
        print('get the events for the whole day!')


__author__ = 'gvrousto'

LOGGER = getLogger(__name__)

def todayEnd():
    today = datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)
    today = += datetime.timedelta(days=1)
    today = today.isoformat() + 'Z'
    return today

def tomorrowStart():
    tomorrow = datetime.datetime.utcnow().replace(hour=00, minute=00, second=01)
    tomorrow += datetime.timedelta(days=1)
    tomorrow = tomorrow.isoformat() + 'Z'
    return tomrrow
def tomorrowEnd():
    tomorrow = datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)
    tomorrow += datetime.timedelta(days=2)
    tomorrow = tomorrow.isoformat() + 'Z'
    return tomrrow
def parseDateTime(string):
    if '+' in string
        return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%S+%f")
    else
        return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%S-%f")


class guscalendarSkill(MycroftSkill):
    def __init__(self):
        super(guscalendarSkill, self).__init__(name = "guscalendarSkill")
    
    def initialize(self):
        create_event_intent = IntentBuilder("CreateEventIntent").\
            require("CreateEventKeyword").build()
        self.register_intent(create_event_intent, self.handle_create_event_intent)
        
       get_nextEvent_intent = IntentBuilder("NextEventIntent")\
            .require("NextKeyword")\
            .require("EventKeyword")\
            .build()
        self.register_intent(get_nextEvent_intent, self.handle_next_event);


    def handle_create_event_intent(self, message):
        self.speak_dialog("created")

    def handle_next_event
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        eventsResult = Calendar_Mutator.service.events().list(
          calendarId='primary', timeMin = now, maxResults=1, singleEvents=True,
          orderBy='startTime').execute()
        events = eventsResult.get('items', [])
        
        if not events
            self.speak_dialog("NoEvents")
        else
            next = events[0]
            place = ''
            description = ''
            start = event['start'].get('dateTime', event['start'].get('date'))
            start = start[:22]+start[(22+1):]
            start = parse_datetime_string(start)
                                    
            today = datetime.datetime.strptime(time.strftime("%x"),"%m/%d/%y") 
            tomorrow = today + datetime.timedelta(days=1)
            date_compare = datetime.datetime.strptime(start.strftime("%x"),"%m/%d/%y")credentials = get_credentials()
            
            rangeDate = "today"
            if (date_compare == today):
                rangeDate = "today"
            elif (date_compare == tomorrow):
                rangeDate = "tomorrow"
            else:
                month_name = (calendar.month_name[start.month])
                day_name = (calendar.day_name[start.weekday()])
                day = str(start.day)
                rangeDate = day_name + ", " + month_name + " " + day
            
            startHour = ("{:d}:{:02d}".format(start.hour, start.minute))
            startHour = time.strptime(startHour,"%H:%M")
            startHour = time.strftime("%I:%M %p",startHour)
            if (startHour[0]=='0'): startHour = startHour.replace('0','',1)
            end = event['end'].get('dateTime', event['end'].get('date'))
            end = end[:22]+end[(22+1):]
            end = parse_datetime_string(end)
            endHour = ("{:d}:{:02d}".format(end.hour, end.minute))
            endHour = time.strptime(endHour,"%H:%M")
            endHour = time.strftime("%I:%M %p",endHour)
            if (endHour[0]=='0'): endHour = endHour.replace('0','',1)

            complete_phrase = ""
           
            if(checkLocation(event)):
                location = event['location']
                location = location.splitlines()
                place_city = ','.join(location[:1])
                place =  " on " + place_city 
            else:
                place =  ""
           
            status = event['status']
            summary = event['summary']

            if(checkDescription(event))
                description = event['description']
            else
               description = ''

            if (len(organizer)) == 2:
                organizer = organizer['displayName']
                if (where.upper() == "WHERE"):
                    if (len(place) > 3):
                        complete_phrase = "Your next appointment will be" + place + " organized by " + organizer + " "
                        place = ""
                    else:
                        complete_phrase = "There is not detailed place, but " + organizer + " has scheduled a appointment for "
                else:
                    complete_phrase = organizer + " has scheduled a appointment for "

                complete_phrase = complete_phrase + rangeDate  + " begining at " + startHour + " and ending at " + endHour + place
                complete_phrase = complete_phrase + ". About " + summary + ". " + description
            
            elif (len(organizer)) == 3:
                if (where.upper() == "WHERE"):
                    if (len(place) > 3):
                        complete_phrase = "Your next appointment will be" + place + " "
                        place = ""
                    else:
                        complete_phrase = "There is not detailed place, but you have a appointment "
                else:
                    complete_phrase = "You have a appointment "

                complete_phrase = complete_phrase + rangeDate  + " from " + startHour + " at " + endHour + place 
                complete_phrase = complete_phrase + ". About " + summary + ". " + description

        self.speak(complete_phrase)


def create_skill():
    return guscalendarSkill()
