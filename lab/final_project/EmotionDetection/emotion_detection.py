import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    obj = {
        "raw_document": {"text": text_to_analyse}
    }
    response = requests.post(url, json=obj, headers=header)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        
    formatted = json.loads(response.text)
    emotions = formatted["emotionPredictions"][0]["emotion"]
    maxim = 0
    dominant_emotion = ""

    for emotion, value in emotions.items():
        if value > maxim:
            maxim = value
            dominant_emotion = emotion

    emotions["dominant_emotion"] = dominant_emotion

    return emotions