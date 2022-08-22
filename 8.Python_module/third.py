"""
f we have an audio file that we want to translate to text, we simply have to replace the source with the audio file instead of a microphone.
Place the audio file and the program in the same folder for convenience. This works for WAV, AIFF, of FLAC files.
An implementation has been shown below
"""
"""
edit
play_arrow

brightness_4
"""
#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr 
  
AUDIO_FILE = ("example.wav") 
  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 
    #reads the audio file. Here we use record instead of 
    #listen 
    audio = r.record(source)   
  
try: 
    print("The audio file contains: " + r.recognize_google(audio)) 
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech  
              Recognition service; {0}".format(e)) 