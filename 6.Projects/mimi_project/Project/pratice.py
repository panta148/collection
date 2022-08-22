
import pyttsx3
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def speed():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.say("Hello World!")
    engine.say('My current speaking rate is ' + str(rate))
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()
    engine.stop()


if __name__ == '__main__':
    # mystr="Hello Nepal where are you."
    # speak(mystr)
    speed()
    