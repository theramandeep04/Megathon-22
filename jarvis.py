from asyncio import DatagramProtocol
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pywhatkit as kit

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("start audio.mp3")

def recordAudio():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")
        
        data = ""
        
        try:
            data = r.recognize_google(audio)
            print("You have said \n" + data)
            print("Audio Recorded Successfully \n ")

    
        
        except Exception as e:
            print("Error :  " + str(e))
            
        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
            
        return data
    
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())
    if "play Alan Walker" in data:
        kit.playonyt("https://youtu.be/HhjHYkPQ8F0")

# initialization
time.sleep(2)
speak("Hi Ramandeep, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
