
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
        
        at = ""
        i = atIndex + 1
        while i < summaryIndex:
            at = at + arr[i] + " "
            i = i + 1
    
        print "At: " + at
        
        summary = ""
        i = summaryIndex + 1
        while i < descIndex:
            summary = summary + arr[i] + " "
            i = i + 1
        
        print "Summary: " + summary
        
        description = ""
        i = descIndex + 1
        while i < (len(arr)-1):
            description = description + arr[i] + " "
            
        print "Description: " + description
        
