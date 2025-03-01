'''
This App sents test to a 3rd party API for emotion detection and returns the result
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    This function received the text from the JS code as argument
    and uses the Emotion detection library to send to the 3rd party API
    displays the result and text
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result = f"For the given statement, the system response is 'anger': {result['anger']}, \
    'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and \
    'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}"
    return result

@app.route("/")
def render_index_page():
    '''
    This function renders the main index.html page with text input, button and response field
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
