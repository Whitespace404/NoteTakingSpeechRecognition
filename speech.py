import os
import time
import speech_recognition as sr
import pyttsx3
import subprocess
import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    reco = sr.Recognizer()
    with sr.Microphone() as source:
        audio = reco.listen(source)
        reco.adjust_for_ambient_noise(source, duration=5)
        said = ""
        try: 
            said = reco.recognize_google(audio)
            return said
        except Exception as e:
            print(e)


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


speak("I am listening")

text = get_audio()
NOTE_STRS = ["make a note", "remember this", 'write this down', 'take a note']
for phrase in NOTE_STRS:
    if len(text) != 0:
        if phrase in text:
            speak("What do you want me to write down?")
            note_text = get_audio()
            note(note_text)
            speak("I've made a note of that")
    elif len(text) == 0:
        speak("You did not say anything")
    
