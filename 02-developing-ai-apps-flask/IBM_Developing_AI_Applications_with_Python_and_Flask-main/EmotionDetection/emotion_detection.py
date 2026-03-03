"""Module for detecting emotions in text using Watson NLP API."""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the given text and return emotion scores with the dominant emotion.

    Returns a dict with anger, disgust, fear, joy, sadness scores
    and dominant_emotion. Returns all None values on invalid input.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers, timeout=10)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }
    dominant_emotion = max(scores, key=scores.get)

    scores["dominant_emotion"] = dominant_emotion
    return scores
