import sys
import os

respond_to = ["where", "am", "I", "how", "far", "away", "current", "location"]

def respond(array):
    count = 0
    for e in array:
        if e in respond_to:
            count += 1
    return count

def handle_input(string):
    return "You are at [loc_coords], [loc_address]" 
