
def respond(array):
    if "appointment" in array:
        return 20
    else:
        return 0

def handle_input(string):
    
    hours ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three"]

    if "get" in string:
        print "got next event"
   
    if "create" in string:
        #create appointment at thirteen summary hangout with friends description rage dick     
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
        while i < len(arr):
            description = description + arr[i] + " "
            i = i + 1
        print "Description: " + description
       
        return "created event"
