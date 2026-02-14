"""
Flask server for Emotion Detection application.
"""

from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route("/")
def show_template():
    """
    Renders the main index page.
    """
    return render_template("index.html")
@app.route("/emotionDetector")
def emotion_detecting():
    """
    Handles emotion detection requests and returns formatted response.
    """
    text = request.args.get("textToAnalyze")
    emotions = emotion_detector(text)
    if emotions["anger"] is None :
        return "Invalid text! Please try again!"
    response = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
