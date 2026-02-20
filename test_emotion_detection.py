from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result1 = emotion_detection("I am glad this happened.")
        self.assertEqual(result1['dominant_emotion'], "joy")

    def test_anger(self):
        result2 = emotion_detection("I am really mad about this.")
        self.assertEqual(result2['dominant_emotion'], "anger")

    def test_adisgust(self):
        result3 = emotion_detection("I feel disgusted just hearing about this.")
        self.assertEqual(result3['dominant_emotion'], "disgust")

    def test_sadness(self):
        result4 = emotion_detection("I am so sad about this.")
        self.assertEqual(result4['dominant_emotion'], "sadness")
        
    def test_fear(self):      
        result5 = emotion_detection("I am really afraid that this will happen.")
        self.assertEqual(result5['dominant_emotion'], "fear")

unittest.main()