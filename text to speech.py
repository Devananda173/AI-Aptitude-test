import pyttsx3
from gtts import gTTS

engine=pyttsx3.init()
engine.say("I am Devananda")
engine.runAndWait()

rate=engine.getProperty('rate')
print(rate)
engine.setProperty('rate',150)
engine.say("It is a cat")
engine.runAndWait()

voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
engine.say("It is a flower")
engine.runAndWait()

volume=engine.getProperty('volume')
print(volume)
engine.setProperty('volume',0.6)
engine.say("It is a flower")

engine.save_to_file("There are many flowers in my garden",'audio/AI.mp3')
engine.runAndWait()

ab=gTTS(text='I love reading books',lang='fr',tld='co.uk')
ab.save('audio/AB.mp3')




