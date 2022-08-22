import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and (hour<12):
        speak("Good Morning")
    elif hour>=12 and (hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello I am your Desktop assistant,please tell me, How can i help you")


def takeCommand():
    """
    it take the command through the micro phone and return in the form oof string


    with mic as source:
        print("Listening..")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    query=r.recognize_google(audio,language="en-US")
    print(f'User said:\n {query}')
    print("Thanks you man")
    """
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        print("Listening.....")
        r.pause_threshold = 1
        # print("helllo man")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        print("i am amrit panta")

    

    try:
        print("Recognizing....")
        # sentence=r.recognize_google(audio)
        query=r.recognize_google(audio,language="en-US")
        print(f'user said:\n {query}')
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"

    return query

def body():
        
    query=takeCommand().lower()
    if 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif "open google" in query:
        webbrowser.open('google.com')
    elif 'open Stack overflow' in query:
        webbrowser.open('Stack overflow.com')
    elif "play music" in query:
        music_dir="E:\\music"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[1]))
    elif 'open VsCode' in query:
        CodePath="C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(CodePath)
    elif "the time" in query:
        StrTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'The time is {StrTime}')
    elif "stop" in query:
        print("The system will be exit soon")
        sys.exit()
    else:
        print("Thanks for using")
    



if __name__ == '__main__':
    greet_me()
    while True:
        body()
    
    
    

    
    
    