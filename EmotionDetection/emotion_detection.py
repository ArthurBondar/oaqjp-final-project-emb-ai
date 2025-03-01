import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        highest_score = 0
        output = {}
        for emotion, score in formatted_response['emotionPredictions'][0]['emotion'].items():
            output[emotion] = score
            if score > highest_score:
                highest_score = score
                output['dominant_emotion'] = emotion

    elif response.status_code == 400:
        output = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
        
    return output