
import speech_recognition
from gtts import gTTS
import os
import pyttsx3
from time import ctime
import os
from playsound import playsound
import pywhatkit
import datetime
import wikipedia
import webbrowser
import requests
import time

# Function to speak using pyttsx3
def speak_pyttsx3(text):
    engine = pyttsx3.init(driverName='espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# Function to speak using gTTS
def speak_gtts(text):
    tts = gTTS(text=text, lang='en', slow=False)
    audio = "output.mp3"
    tts.save(audio)
    playsound(os.path.expanduser("~/Documents/Python_tasks/Alixa_project/output.mp3"))
    os.remove(audio)

listener = speech_recognition.Recognizer()

# Set this variable to choose the TTS library
use_pyttsx3 = False

if use_pyttsx3:
    speak_function = speak_pyttsx3
else:
    speak_function = speak_gtts

speak_function("Hi Muhammed")
speak_function("I am Alexa")
speak_function("how can i help you sir?")

# to catch command from user
def catch_command():
    try:
        with speech_recognition.Microphone(device_index=None) as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = ''
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')
                print(command)
    except speech_recognition.UnknownValueError:
        #speak_function("Sorry, I couldn't understand what you want.")
        pass
    except speech_recognition.RequestError as e:
        print(f"Speech recognition request failed: {e}")
    return command



def run_alexa():
    command = catch_command()
    print(command)

    if "play" in command:
        song = command.replace('play', '')
        speak_function("playing" + song)
        pywhatkit.playonyt(song)

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak_function("current time is" + time)

    if ("brief about" in command) or ("summary" in command):
        info = wikipedia.summary(command, 1)
        speak_function(info)
        print(info)

    if 'date today' in command:
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        speak_function(date)

    if "search" in command:
        search = command.replace("search", "")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak_function("done")

    if "location" in command:
        location = command.replace("location", "")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)

call_times = 0 # to make alexa remind me specific number of times
while True:
    # Set your location coordinates (latitude, longitude)
    latitude = 29.9
    longitude = 31.25

    # Set the date for which you want to get prayer times (today)
    today = datetime.datetime.today().date()

    # Get prayer times using Aladhan API
    url = f"https://api.aladhan.com/v1/timings/{today}?latitude={latitude}&longitude={longitude}&method=2"
    response = requests.get(url)
    data = response.json()

    # Extract prayer times
    times = data['data']['timings']

    
    # praying reminder
    if (datetime.datetime.now().strftime("%H:%M")) == times['Fajr']:
        if call_times < 2:
            speak_function("time of adahan el Fajr")
            call_times += 1
        elif call_times >= 2:
            time.sleep(50.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Dhuhr']:
        if call_times < 2:
            speak_function("time of adahan el Dhuhr")
            call_times += 1
        elif call_times >= 2:
            time.sleep(50.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Asr']:
        if call_times < 2:
            speak_function("time of adahan el Asr")
            call_times += 1
        elif call_times >= 2:
            time.sleep(50.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Maghrib']:
        if call_times < 2:
            speak_function("time of adahan el Maghrib")
            call_times += 1
        elif call_times >= 2:
            time.sleep(50.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Isha']:
        if call_times < 2:
            speak_function("time of adahan el Isha")
            call_times += 1
        elif call_times >= 2:
            time.sleep(50.0)
            call_times = 0

    run_alexa()
