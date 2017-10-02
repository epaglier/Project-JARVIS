{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red46\green95\blue225;\red245\green245\blue245;\red42\green55\blue62;
\red136\green0\blue160;\red204\green0\blue78;\red21\green129\blue62;\red182\green37\blue31;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl400\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  __future__ \cf2 \strokec2 import\cf4 \strokec4  print_function\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  httplib2\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  os\cb1 \
\
\cf2 \cb3 \strokec2 from\cf4 \strokec4  apiclient \cf2 \strokec2 import\cf4 \strokec4  discovery\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  oauth2client \cf2 \strokec2 import\cf4 \strokec4  client\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  oauth2client \cf2 \strokec2 import\cf4 \strokec4  tools\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  oauth2client.file \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 Storage\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 import\cf4 \strokec4  datetime\cb1 \
\
\cf2 \cb3 \strokec2 try\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 \'a0 \'a0 \cf2 \strokec2 import\cf4 \strokec4  argparse\cb1 \
\cb3 \'a0 \'a0 flags = argparse.\cf5 \strokec5 ArgumentParser\cf4 \strokec4 (parents=[tools.argparser]).parse_args()\cb1 \
\pard\pardeftab720\sl400\partightenfactor0
\cf2 \cb3 \strokec2 except\cf4 \strokec4  \cf5 \strokec5 ImportError\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 \'a0 \'a0 flags = \cf2 \strokec2 None\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl400\partightenfactor0
\cf6 \cb3 \strokec6 # If modifying these scopes, delete your previously saved credentials\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 # at ~/.credentials/calendar-python-quickstart.json\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 SCOPES = \cf7 \strokec7 'https://www.googleapis.com/auth/calendar.readonly'\cf4 \cb1 \strokec4 \
\cb3 CLIENT_SECRET_FILE = \cf7 \strokec7 'client_secret.json'\cf4 \cb1 \strokec4 \
\cb3 APPLICATION_NAME = \cf7 \strokec7 'Google Calendar API Python Quickstart'\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\sl400\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  get_credentials():\cb1 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 \'a0 \'a0 \cf7 \strokec7 """Gets valid user credentials from storage.\cb1 \
\
\pard\pardeftab720\sl400\partightenfactor0
\cf7 \cb3 \'a0 \'a0 If nothing has been stored, or if the stored credentials are invalid,\cb1 \
\cb3 \'a0 \'a0 the OAuth2 flow is completed to obtain the new credentials.\cb1 \
\
\cb3 \'a0 \'a0 Returns:\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 Credentials, the obtained credential.\cb1 \
\cb3 \'a0 \'a0 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 \'a0 \'a0 home_dir = os.path.expanduser(\cf7 \strokec7 '~'\cf4 \strokec4 )\cb1 \
\cb3 \'a0 \'a0 credential_dir = os.path.join(home_dir, \cf7 \strokec7 '.credentials'\cf4 \strokec4 )\cb1 \
\cb3 \'a0 \'a0 \cf2 \strokec2 if\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  os.path.exists(credential_dir):\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 os.makedirs(credential_dir)\cb1 \
\cb3 \'a0 \'a0 credential_path = os.path.join(credential_dir,\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0\cf7 \strokec7 'calendar-python-quickstart.json'\cf4 \strokec4 )\cb1 \
\
\cb3 \'a0 \'a0 store = \cf5 \strokec5 Storage\cf4 \strokec4 (credential_path)\cb1 \
\cb3 \'a0 \'a0 credentials = store.\cf2 \strokec2 get\cf4 \strokec4 ()\cb1 \
\cb3 \'a0 \'a0 \cf2 \strokec2 if\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  credentials \cf2 \strokec2 or\cf4 \strokec4  credentials.invalid:\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 flow.user_agent = APPLICATION_NAME\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 \cf2 \strokec2 if\cf4 \strokec4  flags:\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 credentials = tools.run_flow(flow, store, flags)\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 \cf2 \strokec2 else\cf4 \strokec4 : \cf6 \strokec6 # Needed only for compatibility with Python 2.6\cf4 \cb1 \strokec4 \
\cb3 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 credentials = tools.run(flow, store)\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 \cf2 \strokec2 print\cf4 \strokec4 (\cf7 \strokec7 'Storing credentials to '\cf4 \strokec4  + credential_path)\cb1 \
\cb3 \'a0 \'a0 \cf2 \strokec2 return\cf4 \strokec4  credentials\cb1 \
\
\pard\pardeftab720\sl400\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  main():\cb1 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 \'a0 \'a0 \cf7 \strokec7 """Shows basic usage of the Google Calendar API.\cb1 \
\
\pard\pardeftab720\sl400\partightenfactor0
\cf7 \cb3 \'a0 \'a0 Creates a Google Calendar API service object and outputs a list of the next\cb1 \
\cb3 \'a0 \'a0 10 events on the user's calendar.\cb1 \
\cb3 \'a0 \'a0 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 \'a0 \'a0 credentials = get_credentials()\cb1 \
\cb3 \'a0 \'a0 http = credentials.authorize(httplib2.\cf5 \strokec5 Http\cf4 \strokec4 ())\cb1 \
\cb3 \'a0 \'a0 service = discovery.build(\cf7 \strokec7 'calendar'\cf4 \strokec4 , \cf7 \strokec7 'v3'\cf4 \strokec4 , http=http)\cb1 \
\
\cb3 \'a0 \'a0 now = datetime.datetime.utcnow().isoformat() + \cf7 \strokec7 'Z'\cf4 \strokec4  \cf6 \strokec6 # 'Z' indicates UTC time\cf4 \cb1 \strokec4 \
\cb3 \'a0 \'a0 \cf2 \strokec2 print\cf4 \strokec4 (\cf7 \strokec7 'Getting the upcoming 10 events'\cf4 \strokec4 )\cb1 \
\cb3 \'a0 \'a0 eventsResult = service.events().list(\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 calendarId=\cf7 \strokec7 'primary'\cf4 \strokec4 , timeMin=now, maxResults=\cf8 \strokec8 10\cf4 \strokec4 , singleEvents=\cf2 \strokec2 True\cf4 \strokec4 ,\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 orderBy=\cf7 \strokec7 'startTime'\cf4 \strokec4 ).execute()\cb1 \
\cb3 \'a0 \'a0 events = eventsResult.\cf2 \strokec2 get\cf4 \strokec4 (\cf7 \strokec7 'items'\cf4 \strokec4 , [])\cb1 \
\
\cb3 \'a0 \'a0 \cf2 \strokec2 if\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  events:\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 \cf2 \strokec2 print\cf4 \strokec4 (\cf7 \strokec7 'No upcoming events found.'\cf4 \strokec4 )\cb1 \
\cb3 \'a0 \'a0 \cf2 \strokec2 for\cf4 \strokec4  \cf2 \strokec2 event\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  events:\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 start = \cf2 \strokec2 event\cf4 \strokec4 [\cf7 \strokec7 'start'\cf4 \strokec4 ].\cf2 \strokec2 get\cf4 \strokec4 (\cf7 \strokec7 'dateTime'\cf4 \strokec4 , \cf2 \strokec2 event\cf4 \strokec4 [\cf7 \strokec7 'start'\cf4 \strokec4 ].\cf2 \strokec2 get\cf4 \strokec4 (\cf7 \strokec7 'date'\cf4 \strokec4 ))\cb1 \
\cb3 \'a0 \'a0 \'a0 \'a0 \cf2 \strokec2 print\cf4 \strokec4 (start, \cf2 \strokec2 event\cf4 \strokec4 [\cf7 \strokec7 'summary'\cf4 \strokec4 ])\cb1 \
\
\
\pard\pardeftab720\sl400\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  __name__ == \cf7 \strokec7 '__main__'\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl400\partightenfactor0
\cf4 \cb3 \'a0 \'a0 main()\
}