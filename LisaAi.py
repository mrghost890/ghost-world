import ctypes
import datetime as dt
import os
import random
import kit
import time
import pywhatkit
import requests
from utils import opening_text
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import subprocess
import pyjokes
import winshell
import urllib
import pyautogui as pg
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty("rate", 190)
engine.setProperty('volume', 1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")

    else:
        speak("Good Evening ")

    ansg = ['i am lisa, what can i do', 'hello my name is lisa', 'hi i am lisa']
    speak(random.choice(ansg))


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        ansD = ['i cant hear you', 'say again', 'there are to many voices', 'please say again', 'cant you just stop']
        ansD2 = ['so much noise shut up', 'please stop', 'tell me one by one', ]
        speak(random.choice(ansD or ansD2))

        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # lisa searching on wiki,jokes and also play music for you

        if 'search about ' in query:
            speak('okay Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to search result")
            speak(results)

        if 'who is' in query:
            speak('okay Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to search result")
            speak(results)

        elif 'can you tell me jokes' in query or 'tell me joke' in query:
            speak(pyjokes.get_joke())

        elif 'play music' in query:
            music_dir = 'D:\\FILES\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = dt.datetime.now().strftime("%H:%M")
            speak(f"time is{strTime}")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        # lisa can open website for you

        if 'open youtube' in query or 'youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google')

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak('opening fb')

        # about lisa. you can tell anything you want. lisa get you respond

        elif 'hello' in query:
            ansH = ['hello', 'how may help', 'what you need', 'yes i am hear']
            speak(random.choice(ansH))

        elif 'what the hell' in query or 'hell no' in query:
            ansW = "don't use abuse', don't say that,"
            speak(random.choice(ansW))

        elif 'who are you' in query:
            ansW = ['lisa', 'i am lisa', 'artificial intelligent', 'lisa ai']
            speak(random.choice(ansW))

        elif 'what can you do' in query:
            speak('i can open your files for you')
            speak('and your software')
            speak('i can tell you time')
            speak('many more things i can do')

        elif 'what is my ip' in query:
            speak('yor ipv4 is 49.34.168.1')
            print('IPv6:2409:4041:d16:4ca3:dc0e:6582:4ba2:9dbe')
            print('ISP:Jio\nCity:Ahmedabad\nRegion:Gujarat\nCountry:India')

        elif 'which system we use' in query:
            speak('its 64bit windows opreting system')

        elif 'can you speak hindi' in query:
            speak('i only learn three word')
            speak('jay shree krishna')

        if 'i am fine' in query:
            ans = ['okay', 'alright']
            speak(random.choice(ans))

        elif 'hay' in query:
            ans = ['hello how may help you', 'hay']
            speak(random.choice(ans))

        elif 'lisa' in query:
            ansL = ['yes', 'whats the matter', 'hello', ]
            speak(random.choice(ansL))

        elif 'ok good' in query:
            ansG = ['thanks', 'thank you', 'ofcoursh i am good']

        elif 'ok i got it' in query:
            speak('ok than')

        elif 'sorry' in query:
            speak('not a problem')

        elif 'thank you' in query:
            speak('welcome')

        elif 'come on' in query or 'why are you slow' in query:
            speak('i only have a 8gb ram')
            speak('upgrade to thirty tow gb than i go faster')

        elif 'are you there' in query:
            speak('yes, what can i do')

        # lisa can open software and files

        elif 'open telegram' in query:
            path = "C:\\Windows.old\\Users\\MrGHoST\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            speak('okay')
            os.startfile(path)

        elif 'open my file' in query or 'show file' in query:
            filePath = "D:\\FILES"
            os.startfile(filePath)

        elif 'open my movie' in query or 'can i watch movie' in query:
            speak('ok than i open movie list for you')
            moviePath = "D:\\MOVIE"
            os.startfile(moviePath)

        elif 'pirates of caribbean' in query or 'can i watch pirates of caribbean' in query:
            speak('ok than i open pirates of caribbean')
            piratesOfCaribbeanPath = "D:\\MOVIE\\Pirates of the Caribbean"
            os.startfile(piratesOfCaribbeanPath)

        elif 'harry potter' in query or 'i want to watch harry potter' in query:
            speak('ok than i open harry potter')
            harryPotterPath = "D:\\MOVIE\\Harry Potter"
            os.startfile(harryPotterPath)

        elif 'marvel' in query or 'i want to watch marvel movie' in query:
            speak('ok than i open marvel movie')
            marvelPath = "D:\\MARVEL"
            os.startfile(marvelPath)

        elif 'open vs code' in query:
            path = "C:\\Users\\MrGHoST\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('okay')
            os.startfile(path)

        elif 'open browser' in query:
            path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            speak('okay')
            os.startfile(path)

        elif 'open steam' in query:
            path = "D:\\FILES\\Steam\\Steam.exe"
            speak('okay')
            os.startfile(path)

        elif 'open photos' in query:
            path = "D:\\Pictures"
            speak('okay')
            os.startfile(path)

        elif 'open korean drama' in query or 'korean drama' in query:
            dramaPath = "D:\\KDRAMA&Movies"
            os.startfile(dramaPath)

        elif 'open web series' in query or 'web series' in query:
            webSeriesPath = "D:\\MOVIE\\Web Show"
            speak('ok hear you go')
            os.startfile(webSeriesPath)

        elif 'open lucifer' in query or 'lucifer' in query:
            luciferPath = "D:\\MOVIE\\Web Show\\Lucifer"
            ans = ['speak of the devil, there he is.', 'okay opening']
            speak(random.choice(ans))
            os.startfile(luciferPath)

        elif "don't hear" in query or "stop listening" in query:
            speak("for how much time you want to stop")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'lock the system' in query:
            speak("logging out")
            ctypes.windll.user32.LockWorkStation()

        elif 'system shutdown' in query:
            speak("shutting down, good bye")
            os.system("shutdown /s /t 1")

        elif 'restart the system' in query:
            speak('system restarting')
            os.system('restart /r /t 1')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycled")

        elif 'exit' in query:
            speak("okay bye ")
            exit()

        elif 'what should i watch' in query:
            anst = ['i open your movies if you want', 'may be you should watch webshow', 'i think you need a break']
            speak(random.choice(anst))

        elif "open whatsapp" in query:
            path = 'C:\\Users\\MrGHoST\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(path)

        elif 'send prank message' in query:
            path = 'C:\\Users\\MrGHoST\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(path)
            time.sleep(10)

            for i in range(1):
                pg.write('halo')
                pg.press('enter')
