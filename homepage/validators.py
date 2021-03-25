from django.core.exceptions import ValidationError
import fleep
import json
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import re

def validateSoundAssets(value)->bool:
    with open('temp.wav', 'wb+') as destination:
        destination.write(value.read())
    if (checkType() and checkAudio()):
        return True
    else :
        return False


def checkAudio():
    authenticator = IAMAuthenticator('KTAC__c-sREYsNJlxDV82U5VQgGdWkgwwGOpWa3N5tdD')
    service = SpeechToTextV1(authenticator=authenticator)
    service.set_service_url("https://api.kr-seo.speech-to-text.watson.cloud.ibm.com/instances/8c376c7c-efef-4888-a376-f57fdae6b66a")    
    with open("temp.wav",'rb') as audio_file:  
        dic = json.loads(json.dumps(service.recognize(
                                audio=audio_file,
                                content_type='audio/wav',   
                                timestamps=True,
                                word_confidence=True,
                                model='en-US_NarrowbandModel').get_result(), indent=2))
    str = ""    
    while bool(dic.get('results')):
        str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:]        
    if(re.search("\*+",str)):
        return False
    else:
        return True

def checkType():
    with open("temp.wav", "rb") as file:
        info = fleep.get(file.read(128))
        if info.extension[0] == 'wav':
            return True
        else: 
            return False
