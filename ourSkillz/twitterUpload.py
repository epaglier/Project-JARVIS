from TwitterAPI import TwitterAPI
import cv2

CONSUMER_KEY = 'K3A5A1dWbt9BKg41EBOc1Dnn4'
CONSUMER_SECRET = 'Eo2EqIN5m2iRor068OxV3NV5nwgRDQa5Z8hie2oeYf1BW3SCKP'
ACCESS_TOKEN_KEY = '886965171595472896-FndDWVETYvGQtlg7dWVxY6S3usoO2qG'
ACCESS_TOKEN_SECRET = 'kh24Fp13TzELdzi9MNwOQPxy4VlM6ByRrTBcAZC3pc7ff'

respond_to = ["tweet","post","twitter"]

def respond(array):
    count = 0
    for word in array:
        if word in respond_to:
            count = count + 1
    return count

def handle_input(string):
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    file = open('./ourSkillz/Image_folder/Demo.jpg', 'rb')
    cap = raw_input("Enter caption..\n")
    r = api.request('statuses/update_with_media', {'status':cap}, {'media[]':file})
    return "Posted to all of your adoring fan!"

