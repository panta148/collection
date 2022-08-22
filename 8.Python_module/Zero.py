>>> import speech_recognition as sr
>>> r = sr.Recognizer()
>>> harvard = sr.AudioFile('audio_files/harvard.wav')
>>> with harvard as source:
...     audio = r.record(source)
... 
>>> type(audio)
<class 'speech_recognition.AudioData'>
>>> r.recognize_google(audio)
u'the stale smell of old beer lingers it takes heat to bring out the odor a cold dip restores health and zest a salt pickle taste fine with ham tacos al Pastore are my favorite a zestful food is the hot cross bun'
>>> 

######################################################################################
#Ambient Noise
>>> jackhammer = sr.AudioFile('audio_files/jackhammer.wav')
>>> with jackhammer as source:
...     audio = r.record(source)
... 
>>> r.recognize_google(audio)
u'the snail smell of old beer drinkers'
>>> with jackhammer as source:
...     r.adjust_for_ambient_noise(source)
...     audio = r.record(source)
... 
>>> r.recognize_google(audio)
u'still smell old gear vendors'
>>> 
########################################################################################
Speech testing
Using the speech recognition module:

$ python -m speech_recognition
A moment of silence, please...
Set minimum energy threshold to 259.109953712
Say something!
Got it! Now to recognize it...
You said hello hello
Got it! Now to recognize it...
You said the rain in Spain
Say something!
^C$