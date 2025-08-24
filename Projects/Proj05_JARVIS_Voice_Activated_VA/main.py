# main.py

import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
from client import send_and_save

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = '#ADD YOUR NewsApi key#' # Do not Redeem(any one else)!!!!!

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open('https://www.google.com')
    elif 'open youtube' in c.lower():
        webbrowser.open('https://www.youtube.com')
    elif 'open linkedin' in c.lower():
        webbrowser.open('https://www.linkedin.com')
    elif 'open facebook' in c.lower():
        webbrowser.open('https://www.facebook.com')
    elif 'open pinterest' in c.lower():
        webbrowser.open('https://www.pinterest.com')
    elif c.lower().startswith('play song'):
        song_name = c.lower().replace('play song', '').strip()
        if song_name in musicLibrary.music_:
            webbrowser.open(musicLibrary.music_[song_name])
            speak(f'Playing {song_name}')
        else:
            speak('Sorry, I could not find that song in the library.')
    elif 'news' in c.lower():
        r = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}')
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            pass
    else:
        response_text = send_and_save(c)
        speak(response_text)

if __name__ == '__main__':
    speak("Iniatializing JARVIS")

    while True:
        r = sr.Recognizer()
        print('recognising....')
        try:
            with sr.Microphone() as source:
                print("Listening....")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=7)
            word = r.recognize_google(audio)

            if (word.lower() == 'jarvis'):
                speak('Yes sir, how can I help you?')
           
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=5, phrase_time_limit=7)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
