from fbrecog import FBRecog
from math import trunc

invoke_words = ["who","was","that","recognize","picture"]

def respond(array):
    count = 0
    for word in invoke_words:
        if word in array:
            count = count + 1
    return count

def recognize():
    #if token fails refresh with https://developers.facebook.com/tools/explorer
    access_token = 'EAACEdEose0cBAEo8IOuvhrN6qnmZCV5LX2Dg1LzQNuQKWhy42jc0Rs0dviEhqbFsfjOSULA2Fa6WbCtW28PQm7TVA8s15X2vhvboY9xnXQnvxRwGKMKqqINcUeaQ8odCiba9KQOdaHdavSldDFtwpAHZAqGoZBYJDqmGGbKiDvlOtBUe3Eyyszw9W2TX71YxGbSy35QxwZDZD'

    cookies = ':authority:www.facebook.com:method:POST:path:/photos/tagging/recognition/?dpr=2:scheme:httpsaccept:*/*accept-encoding:gzip, deflate, braccept-language:en-US,en;q=0.9content-length:780content-type:application/x-www-form-urlencodedcookie:datr=RQD_VTToj-1jR-KtNHnkD5z0; sb=okQMV3S6FMXJUYoPXpGyf9Qz; pl=n; dpr=2; c_user=100000817532103; xs=83%3ARAscKWCwE-q2gw%3A2%3A1503639870%3A10210%3A2689; fr=0GAYWIzMJiEPQs44I.AWWOTqNOqEzDRgssWVke6LNEiPU.BV_wBJ.So.Fn2.0.0.BZ_N8L.AWXbQaGQ; presence=EDvF3EtimeF1509744742EuserFA21B00817532103A2EstateFDutF1509744742588CEchFDp_5f1B00817532103F4CC; act=1509744809019%2F27; wd=725x703origin:https://www.facebook.comreferer:https://www.facebook.com/user-agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36x_fb_background_state:1'
    
    fb_dtsg = 'AQEYoBOWHQEQ:AQFonwFL5ZkC'

    recog = FBRecog(access_token, cookies, fb_dtsg)
    temp = recog.recognize("/home/evan/Project-JARVIS/JARVIS-CORE/ourSkillz/Image_folder/Demo.jpg")#'simplecv' + str(num) + ".png")
    return temp[0]

def handle_input(string):
    arr = recognize()
    return "I am " + str(trunc(float(arr['certainity']*100))) + " percent sure that was " + arr['name']

