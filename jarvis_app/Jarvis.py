import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import comtypes.client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)  # Speaking speed
engine.setProperty('volume', 2.0) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

speak("Hi sir, I am Jarvis. Please tell me how may I help you!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... JD")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in") 
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query == "None":
            continue
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=5)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play song' in query:
            music_dir = 'D:\songsfav'
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the music folder.")
            else:
                speak("Music directory not found.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

       