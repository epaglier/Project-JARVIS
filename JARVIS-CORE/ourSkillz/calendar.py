
intentWords = ["calendar","event","create", "get",]

def respond(arrayOfWords):
	numMatches = 0
	for word in intentWords:
		if word in arrayOfWords:
			numMatches = numMatches + 1
	return numMatches
	

def handle_input(string):
	#Do stuff on pi
	return "Sorry calendar is not functional right now."
