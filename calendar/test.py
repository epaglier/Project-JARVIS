import calendar_api

CM = calendar_api.Calendar_Mutator()
numEvents = 7
CM.getXEvents(numEvents)
location = 'test the calendar insert'
description = 'asdf'
event = 'test'
CM.setEvent(event, description,event)
