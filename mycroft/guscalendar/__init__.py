from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'gvrousto'

LOGGER = getLogger(__name__)

class guscalendarSkill(MycroftSkill):
    def __init__(self):
        super(guscalendarSkill, self).__init__(name = "guscalendarSkill")
    
    def initialize(self):
        create_event_intent = IntentBuilder("CreateEventIntent").\
            require("CreateEventKeyword").build()
        self.register_intent(create_event_intent, self.handle_create_event_intent)
    
    def handle_create_event_intent(self, message):
        self.speak_dialog("created")
    
    def stop(self):
        pass

def create_skill():
    return guscalendarSkill()
