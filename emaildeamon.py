from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import record, play_mp3

import httplib2
import os
from os.path import dirname, abspath, join, expanduser
import sys

from googleapiclient import discovery
from googleapiclient import errors
import oauth2client
from oauth2client import file
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow

import json
from json import JSONEncoder
from HTMLParser import HTMLParser
from datetime import datetime

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    print("checking for cached credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'mycroft-gmail-skill.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        credentials = tools.run_flow(OAuth2WebServerFlow(client_id=CID,client_secret=CIS,scope=SCOPES,user_agent=APPLICATION_NAME),store)
        print 'Storing credentials to ' + credential_dir
	print 'Your GMail Skill is now authenticated '
    else:
	print 'Loaded credentials for Gmail Skill from ' + credential_dir

    return credentials

def GetMessage(user_id, msg_id):
	try:
		message = service.users().messages().get(userId=user_id, id=msg_id).execute()
		return message

	except errors.HttpError, error:
		print 'An error occurred: %s' % error


def parse_datetime_string(string):
    if '+' in string:
	if "UTC" in string or "GMT" in string or "EST" in string or "PST" in string or "MEZ" in string:
		string = string[:-6]
	return datetime.strptime(string,"%a, %d %b %Y %H:%M:%S +%f")
    elif '-' in string:
	if "UTC" in string or "GMT" in string or "EST" in string or "PST" in string or "MEZ" in string:
		string = string[:-6]
	return datetime.strptime(string,"%a, %d %b %Y %H:%M:%S -%f")
    else:
	string = string[:-6]
	return datetime.strptime(string,"%a, %d %b %Y %H:%M:%S +%f")

def main()
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    global service
    service = discovery.build('gmail', 'v1', http=http)
    global messages

    try:
	user_id = "me"
	label_id = ["INBOX","IMPORTANT"]
        query = "is:unread"
	
	response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=1,q=query).execute()
	messages = []
    	if 'messages' in response:
    		messages.extend(response['messages'])

    	while 'nextPageToken' in response:
		page_token = response['nextPageToken']
		response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=max_results,q=query,pageToken=page_token).execute()
   except errors.HttpError, error:
	print 'An error occurred: %s' % error
 
    curMessage = messages[0]
    while true:
	user_id = "me"
	label_id = ["INBOX","IMPORTANT"]
	response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=1,q=query).execute()
	newMail = []
    	if 'newMail' in response:
    		newMail.extend(response['messages'])

    	while 'nextPageToken' in response:
		page_token = response['nextPageToken']
		response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=max_results,q=query,pageToken=page_token).execute()
	newestMail = newMail[0]
	if  curMessage is not newestMail:
		curMessage = newestMail
    		try:
			user_id = "me"
			label_id = ["INBOX","IMPORTANT"]
        		query = "is:unread"
	
			response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=10,q=query).execute()
			messages = []
		    	if 'messages' in response:
		    		messages.extend(response['messages'])

		    	while 'nextPageToken' in response:
				page_token = response['nextPageToken']
				response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=max_results,q=query,pageToken=page_token).execute()
	   	except errors.HttpError, error:
			print 'An error occurred: %s' % error
	    	
		msgs = messages[:10] 
		complete_phrase = ""
		for x in range(0,10):	
			msg_id = msgs[x]["id"] 
			msg = GetMessage(user_id, msg_id)
			msg_headers = msg["payload"]["headers"] 
			msg_headersT = {}
			for p in msg_headers: msg_headersT[p["name"]] = p["value"] 
			msg_from 	= msg_headersT["From"] 
			msg_from 	= msg_from.split("<")
			if (len(msg_from) > 1):
				if msg_from[0][:1] == '"':
					msg_from_sender = msg_from[0][1:-2]
				else:
					msg_from_sender = msg_from[0]
				msg_from_email	= msg_from[1][0:-1]	
			else:
				msg_from_email	= msg_from[0][0:-1]	
	
			msg_from_sender = msg_from_sender.replace('. ',', ')

			msg_received	= parse_datetime_string(msg_headersT["Date"])
			msg_received_24	= msg_received.strftime("%A, %B %d, %Y at %H:%M")
			msg_received_12 = msg_received.strftime("%A, %B %d, %Y at %I:%M %p")

			if int(time_format) == 12:
				msg_received = msg_received_12
			else:
				msg_received = msg_received_24

			msg_subject 	= HTMLParser().unescape(msg_headersT["Subject"])
			msg_txt		= HTMLParser().unescape(msg["snippet"])
	
			complete_phrase = "Email from "+msg_from_sender+" received "+msg_received+", with subject, "+msg_subject
			if detail is True:
				complete_phrase = complete_phrase + ", Message, " + msg_txt

			self.speak(complete_phrase)	
		
