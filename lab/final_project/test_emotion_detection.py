import unittest
from EmotionDetection.emotion_detection import emotion_detector

class testEmotions(unittest.TestCase):
    def test_emotion(self):
        statement1=emotion_detector("I am glad this happened")
        self.assertEqual(statement1["dominant_emotion"],"joy")

        statement2=emotion_detector("I am really mad about this")
        self.assertEqual(statement2["dominant_emotion"],"anger")

        statement3=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(statement3["dominant_emotion"],"disgust")

        statement4=emotion_detector("I am so sad about this")
        self.assertEqual(statement4["dominant_emotion"],"sadness")

        statement5=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(statement5["dominant_emotion"],"fear")
unittest.main()