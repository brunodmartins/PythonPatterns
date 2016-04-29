import unittest
import strategy
__author__ = 'Bruno'


class testStrategy(unittest.TestCase):
    def test_human_speak(self):
        human = strategy.Human()
        self.assertEqual(human.speak(), 'Hello!')

    def test_dog_speak(self):
        dog = strategy.Dog()
        self.assertEqual(dog.speak(), 'Bark!')

    def test_speak_speak(self):
        speak = strategy.Speak()
        try:
            speak.speak()
        except NotImplementedError:
            pass

if __name__ == '__main__':
    unittest.main()
