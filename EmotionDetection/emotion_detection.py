import requests
import json
def emotion_detection(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json = Myobj, headers = Headers)

    data = response.json()

    scores = data['emotionPredictions'][0]['emotion']

    max_emotion = max(scores, key=scores.get)

    anger_score = data['emotionPredictions'][0]['emotion']['anger']

    disgust_score = data['emotionPredictions'][0]['emotion']['disgust']
    
    fear_score = data['emotionPredictions'][0]['emotion']['fear']
    
    joy_score = data['emotionPredictions'][0]['emotion']['joy']
    
    sadness_score = data['emotionPredictions'][0]['emotion']['sadness']

    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': max_emotion
}