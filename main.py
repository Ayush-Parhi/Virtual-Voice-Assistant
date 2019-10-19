import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import signal


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 185)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir! how can i help you?")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon sir! how can i help you?")
    else :
        speak("Good Evening sir! how can i help you?")
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        speak("Sorry sir i didn't understand that. Please say that again. ")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open google' in query:
            webbrowser.open('google.co.in')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open gfg' in query:
            webbrowser.open('geeksforgeeks.org')
        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")
        elif 'facial recognition' in query:
            speak("Identifying the person")
            process = subprocess.Popen("python face_recognition.py", stdout=subprocess.PIPE, shell=True)
        elif 'movie' in query:
            mpath ="E:\\movies"
            movies = os.listdir(mpath)
            print(movies)
            speak("What would you like to watch sir?")
            query2 = take_command().lower()
            if 'endgame' in query2:
                speak("Enjoy sir!")
                os.startfile("E:\\movies\\MCU\\AVENGERS\\Avengers Endgame (2019) [Worldfree4u.Wiki] 720p BluRay x264 ESub [Dual Line Audio] [Hindi + English].mkv")
            if 'infinity war' in query2:
                speak("Enjoy sir!")
                os.startfile("E:\\movies\\MCU\\AVENGERS\\Avengers Infinity War (2018)\\Avengers Infinity War (2018) [Worldfree4u.club] 720p HDRip x264 [Dual Audio] [Hindi DD 2.0 + English DD 2.0].mkv")
            if 'civil war' in query2:
                speak("Enjoy sir!")
                os.startfile("E:\\movies\\MCU\\CAPTAIN AMERICA\\Captain America Civil War 2016 [Worldfree4u.Wiki] 720p BRRip x264 ESub [Dual Audio] [Hindi DD 5.1 + English DD 5.1].mkv")
            if 'far from home' in query2:
                speak("Enjoy sir!")
                os.startfile("E:\\movies\\MCU\\SPIDER-MAN\\Spider-Man Far From Home (2019) [Worldfree4u.Wiki] 720p HDRip x264 [Dual Audio] [Hindi + English].mkv")
        #elif 'music' or 'track' in query:
        #    speak("Enjoy sir!")
        #    os.startfile("E:\\06-Back In Black-mw.mp3")
        #elif 'who are you' or 'what are you' or 'tell me about yourself' in query:
        #    speak("I am JARVIS, a virtual voice assistant created by Ayush.")


