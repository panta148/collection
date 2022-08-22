def speak(str):
    from win32com.client import Dispatch
    voice = Dispatch("SAPI.SPVOICE")
    voice.Speak(str)


if __name__ == '__main__':
    print("now some thing is going to speak")
    speak("Nepal is the beautiful country in the world ,"
          "and it the time to support the nepal and the Nepalies people")
    print("this is the ending sentence")



