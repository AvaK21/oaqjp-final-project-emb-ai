'''
This file is the main of the flask application workings. It starts here 
and calls the needed functions from here
'''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detection


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_det():
    ''' Takes the user input, runs it thro emotion_detection and ouputs the results
    '''
    text_to_analyze = request.args.get('textToAnalyze')


    response = emotion_detection(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"


    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, and "
        f"'sadness': {sadness_score}. The dominant emotion is "
        f"{dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    ''' Sets up the initial environment
    '''
    return render_template("index.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5004)
