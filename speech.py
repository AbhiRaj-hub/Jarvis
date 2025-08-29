import pyttsx3
from decouple import config
import speech_recognition as sr
USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

from datetime import datetime

def greet_user():
    hour = datetime.now().hour
    if hour>=0 and hour<12:
        speak(f"Good Morning {USERNAME}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon {USERNAME}")
    elif hour>=18 and hour<24:
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}, How may I assist you?")



from random import choice
from utils import opening_text


def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text()))
        else:
            hour = datetime.now().hour
            if 21 <= hour:
                speak(f"Good Night Sir, take care!")
            else:
                speak(f"Good Day Sir!")
            exit()
    except Exception:
        speak("Sorry, I didn't catch that could you repeat?")
        query = 'None'
    return query


