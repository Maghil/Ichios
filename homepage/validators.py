from django.core.exceptions import ValidationError
import fleep
import json
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import re
import time
import os
import environ

# root = environ.Path(    )  # get root of the project
env = environ.Env()
environ.Env.read_env() 

def validateSoundAssets(value)->bool:
    filename = str(time.time())+".wav"
    with open(filename, 'wb+') as destination:
        destination.write(value.read())
    if (checkType(filename) and checkAudio(filename)):
        os.remove(filename)
        return True
    else :
        os.remove(filename)
        return False


def checkAudio(filename):
    authenticator = IAMAuthenticator(env.str('IBM_KEY'))
    service = SpeechToTextV1(authenticator=authenticator)
    service.set_service_url(env.str('IBM_URL'))    
    try:
        with open(filename,'rb') as audio_file:  
            dic = json.loads(json.dumps(service.recognize(
                                    audio=audio_file,
                                    content_type='audio/wav',   
                                    timestamps=True,
                                    word_confidence=True,
                                    model='en-US_NarrowbandModel').get_result(), indent=2))
    except:
        return(False)
    str = ""    
    while bool(dic.get('results')):
        str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:]  
    if(re.search("\*+",str)):
        return False
    else:
        return True

def checkType(filename):
    with open(filename, "rb") as file:
        info = fleep.get(file.read(128))
        if info.extension[0] == 'wav':
            return True
        else: 
            return False
