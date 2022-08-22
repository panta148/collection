import pyttsx3
from pygame import mixer
from datetime import datetime
from time import time
def speak(audio):
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def musiconloop(file,stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input(" ->")
        if a==stop:
            mixer.music.stop()
            break

def log_now(msz):
    with open("Document.txt","a") as f:
        f.write(f'{msz}\t\t{datetime.now()}\n')




if __name__ == '__main__':
    # musiconloop("Two_Face.mp3","stop")
    speak("WelCome to the Remainder APP")
    init_water=time()
    init_eye=time()
    init_exe=time()
    water=5*60
    eye=20*60
    exe=30*60
    choice=True
    while choice:
        if time()-init_water>water:
            speak("hello bro its water drinking time ..please drank water\n type stop to stop ")
            # print("hello bro its water drinking time ..please drank water\n type stop to stop ->")
            musiconloop("Two_Face.mp3","stop")
            init_water=time()
            log_now("Drinking water at  ")
        if time()-init_eye>eye:
            speak("hello bro its eyes exercise time ..please do thee exercise\n type stop to stop ")
            # print("hello bro its eyes exercise time ..please do thee exercise\n type stop to stop ->")
            musiconloop("Luxery.mp3","stop")
            init_eye=time()
            log_now("Eye Exercise  at  ")
        if time()-init_exe>exe:
            speak("hello bro its Exercise time ..please do the exercise\n type stop to stop ")
            # print("hello bro its Exercise time ..please do the exercise\n type stop to stop ->")
            musiconloop("Lost_Found.mp3","stop")
            init_exe=time()
            log_now("Exercise done  at  ")   
 
        

                