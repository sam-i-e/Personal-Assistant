import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import os
import time
import subprocess
import wolframalpha
import json
import requests
import take_pic
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def timer():
    speak("Enter the time in seconds")
    print("Enter the time in seconds")
    statement = takeCommand().lower()
    sec = int(statement)
    while sec >= 0:
        timer = datetime.timedelta(seconds=sec)
        print(timer, end="\r")
        time.sleep(1)
        sec -= 1


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=8, phrase_time_limit=8)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


print("Loading your AI personal assistant Lilo")
speak("Loading your AI personal assistant Lilo")
wishMe()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye bye" in statement or "bye" in statement:
            speak('your personal assistant Lilo is shutting down,Good bye')
            print('your personal assistant Lilo is shutting down,Good bye.')
            break
        elif "wikipedia" in statement:
            speak("Searching wikipedia......")
            print("Searching wikipedia......")
            statement = statement.replace("wikipedia ", "")
            result = wikipedia.summary(statement, sentences=3)
            print(result)
            speak(f'According to wikipedia\n {result}')
        elif "weather" in statement:
            api_key = "19ff20b253ed011c87da50a4aef58e9d"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            print("what is the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            time.sleep(3)
        elif "joke" in statement:
            speak(pyjokes.get_joke())
            time.sleep(3)
        elif "youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(3)
        elif "google" in statement:
            webbrowser.open_new_tab("https://www.google.co.in")
            speak("google is open now")
            time.sleep(3)
        elif "open gmail" in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            speak("gmail is open now")
            time.sleep(3)
        elif "open timer" in statement:
            timer()
            speak("Time's up")
            print("Time's up")
            time.sleep(3)
        elif "what is the time" in statement:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'The time is {t}')
            speak(f'The time is {t}')
        elif "news" in statement:
            webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from Times of India, Happy Reading!")
            time.sleep(3)
            speak('your personal assistant Lilo is shutting down,Good bye')
            print('your personal assistant Lilo is shutting down,Good bye')
            break
        elif "take a photo" in statement or "click a picture" in statement:
            speak("Say Cheese!")
            take_pic.click()
        elif "who are you" in statement or "what can you do" in statement:
            print('''I am your sweet and intelligent Assistant Lilo version 1.0 . I am programmed to minor tasks like
                  opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather
                  In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!''')
            speak('''I am your sweet and intelligent Assistant Lilo version 1 point 0.  I am programmed to minor tasks like
                  opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather
                  In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!''')
        elif "who created you" in statement or "who discovered you" in statement:
            print("I was built by Samow")
            speak("I was built by Samow")
        elif "where do you live" in statement or "what is your location" in statement:
            print("My Love, In your heart.")
            speak("My Love, In your heart.")