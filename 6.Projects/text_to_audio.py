'''pip install gtts
pip install playsound'''
from gtts import gTTS
from playsound import playsound
audio='example.mp3'
language='en'
mytext="Nepal is a beautiful country where world's highest mountain Mt.Everest is lies"
print('Starting....')
clip=gTTS(text=mytext,lang=language,slow=False)
clip.save(audio) #save clip in audio format
playsound(audio) #playsound in audio format
print('Finished.......')