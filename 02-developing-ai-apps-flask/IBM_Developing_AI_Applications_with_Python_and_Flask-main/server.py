"""
Flask server for the Emotion Detection web application.
Serves the UI and exposes the emotionDetector endpoint.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Serve the main page with the emotion detection form.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the emotion in the text provided via textToAnalyze query parameter.
    Returns a formatted string or error message for blank/invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )
    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
