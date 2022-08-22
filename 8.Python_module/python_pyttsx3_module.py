"""
Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay.
 Supports multiple TTS engines, including Sapi5, nsss, and espeak.

 Installation
pip install pyttsx3

If you recieve errors such as No module named win32com.client, No module named win32,
 or No module named win32api, you will need to additionally install pypiwin32.

 Changing Voice , Rate and Volume :

import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
"""
"""
single fiinction to speal the text
import pyttsx3
pyttsx3.speak("I will speak this text")
"""
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
    mystr="Hello Nepal where are you."
    speak(mystr)
    speed()
