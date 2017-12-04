import wikipedia as wiki
import sys
import re

def respond(array):
    if "search" in array:
        return 1
    else:
        return 0

def handle_input(string):
    try:
        count = 1
        arr = string.split(" ")
        title = ""
        while count < len(arr):
            title = arr[count] + " "
            count = count + 1
        results = wiki.search(title, 2)
        summary = re.sub(r'\([^)]*\)|/[^/]*/', '', wiki.summary(results[0], 2))
        return summary

    except wiki.exceptions.DisambiguationError as e:
        return "Ambiguous search term. Please be more specific."

    except Exception as e:
        return "General wiki error"
