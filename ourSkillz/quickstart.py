
def respond(array):
    if "appointment" in array:
        return 20
    else:
        return 0

def handle_input(string):
    if "get" in string:
        print "got next event"
   
   if "create" in string:
        
       #hardcode for day of event fuck it
        arr = string.split(" ")
        atIndex = arr.index("at")
        summaryIndex = arr.index("summary")
        descIndex = arr.index("description")
        
        summary = ""
        i = summaryIndex + 1
        while i < descIndex:
            summary = summary + arr[i] + " "
            i = i + 1
        
        description = ""
        i = descIndex + 1
        while i < (len(arr)-1):
            description = description + arr[i] + " "

