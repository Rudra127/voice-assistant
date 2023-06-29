# pip install pyaudio

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import time
from tkinter import *
from tkinter import messagebox
from selenium import webdriver  # pip install selenium
import time
from selenium.webdriver.common.keys import Keys
import ecapture as ec
import subprocess
import ctypes
import win32com.client as wincl
import random
import requests

# import pygame
# import pygame.camera

# #    web driver as per you requirements ( you can use chrome, mozrila,edge etc..)
# SAPI5 is a voice which is provided by microsoft os.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):  # this function will help me to hear commands and output which i give
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # this function is for engage people
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am coco your personal assistant sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def timer():
    # creating Tk window
    box = Tk()

    # setting geometry of tk window
    box.geometry("300x250")

    # Using title() to display a message in
    # the dialogue box of the message in the
    # title bar.
    box.title("Time Counter")

    # Declaration of variables
    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    # Use of Entry class to take input from the user
    hourEntry = Entry(box, width=3, font=("Arial", 18, ""),
                      textvariable=hour)
    hourEntry.place(x=80, y=20)

    minuteEntry = Entry(box, width=3, font=("Arial", 18, ""),
                        textvariable=minute)
    minuteEntry.place(x=130, y=20)

    secondEntry = Entry(box, width=3, font=("Arial", 18, ""),
                        textvariable=second)
    secondEntry.place(x=180, y=20)

    def submit():
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get())*3600 + int(minute.get()) * \
                60 + int(second.get())
        except:
            print("Please input the right value")
        while temp > -1:

            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp, 60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours = 0
            if mins > 60:

                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            box.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")

            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1

    # button widget
    btn = Button(box, text='Set Time Countdown', bd='5',
                 command=submit)
    btn.place(x=70, y=120)

    # infinite loop which is required to
    # run tkinter program infinitely
    # until an interrupt occurs
    box.mainloop()

def sendEmail(to, content):
    # this will send mail to gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarvisxyz123@gmail.com', 'coco@2022')
    server.sendmail('jarvisxyz123@gmail.com', to, content)
    server.close()

def chatgpt_voice_assistant(api_key):
    # Set up the speech recognition API
    r = sr.Recognizer()

    # Set up the ChatGPT API
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Set up the text-to-speech engine
    engine = pyttsx3.init()

    # Record the user's speech
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Convert the speech to text
    text_input = r.recognize_google(audio, language='en-in')
  


    # Send the text to the ChatGPT API
    data = {
        "prompt": text_input,
        "max_tokens": 50,
        "temperature": 0.7,
    }

    response = requests.post(url, headers=headers, json=data)
    ai_response = response.json()["choices"][0]["text"]

    # Convert the AI response to speech
    engine.say(ai_response)
    engine.runAndWait()

def whatsapp():  # this is fun part of it and i complete your take call api and do things.
    # but i think so this is no what i am saying it's web scraping
    driver = webdriver.Chrome('C:\\Users\\praja\\OneDrive\\Documents\\python cwh\\chromedriver.exe')
    driver.get("https://web.whatsapp.com/")
    time.sleep(3)
    driver.maximize_window()
    driver.implicitly_wait(50)
    id = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
    id.send_keys('rudra_prajapati.007')
    time.sleep(3)

    passwd = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
    passwd.send_keys('jarvis1122')

    login = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]')
    login.click()

    time.sleep(10)

def instagram():  # this is fun part of it and i complete your take call api and do things.
    # but i think so this is no what i am saying it's web scraping
    driver = webdriver.Chrome('C:\\Users\\praja\\OneDrive\\Documents\\python cwh\\chromedriver.exe')
    driver.get("https://www.instagram.com/")
    time.sleep(3)
    driver.maximize_window()
    driver.implicitly_wait(50)
    id = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
    id.send_keys('jarvis.project')
    time.sleep(3)

    passwd = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
    passwd.send_keys('jarvis1122')

    login = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]')
    login.click()

    time.sleep(10)

def result():
    driver= webdriver.Chrome('C:\\Users\\praja\\OneDrive\\Documents\\python cwh\\chromedriver.exe')
    driver.get("https://www.gtu.ac.in/result.aspx")
    driver.maximize_window()
    driver.implicitly_wait(50)
    if driver.find_element("xpath",'//*[@id="result1"]/h6/li[1]/div/div[1]/div/div[2]/h3/a'):
        speak("ohh result is out. let's check it!!")
        result = driver.find_element("xpath",'//*[@id="result1"]/h6/li[1]/div/div[1]/div/div[2]/h3/a')
        result.click()
        # time.sleep(8)
        # enrollment = driver.find_elements("xpath",'//*[@id="txtenroll"]')
        # enrollment.send_keys[0]('216400307126')
        # time.sleep(5)
        # sub = driver.find_elements("xpath",'//*[@id="btnSearch"]')
        # sub.click()
        time.sleep(60)
    else:
       result()
def youtube():
    driver= webdriver.Chrome('C:\\Users\\praja\\OneDrive\\Documents\\python cwh\\chromedriver.exe')
    driver.get("https://youtube.com")
    driver.maximize_window()
    driver.implicitly_wait(100000)
    
    if driver.find_element("xpath",'//*[@id="skip-button:5"]/span/button/span'):
        ad=driver.find_element("xpath",'//*[@id="skip-button:5"]/span/button/span')
        time.sleep(5)
        ad.click()
        time.sleep(1200)
    else:
        youtube()


def takescreenshot():
   
    ec.capture(0, "coco ", "img.jpg")
    speak("Screenshot taken and saved as screenshot.jpg")


wishMe()
while True:
        # if 1:
    query = takeCommand().lower()

        # Logic for executing tasks based on query
    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
    elif 'open youtube' in query:
            speak("opening the youtube ")
            youtube()

    elif 'open google' in query:
            speak("opening the google")
            webbrowser.open("https://google.com")

    elif 'rick roll' in query:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif 'open stack overflow' in query:
            speak("opening the stackoverflow")
            webbrowser.open("https://stackoverflow.com")

    elif 'result' in query:
            speak("let's check it ")
            result()

    elif 'play music' in query:
            speak("playing the music")
            music_dir = 'C:\\Users\\praja\\Music\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
       
    elif 'play my playlist on spotify' in query:
            speak("opening the playlist")
            webbrowser.open("https://open.spotify.com/playlist/6FCr7M3yL0pM3v26OEZhrh")
    elif 'take screenshot' in query:
            speak("taking the screenshot")
            takescreenshot()
    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is money just kidding.")
            speak(f"Sir, the time is {strTime}")
    elif 'open instagram' in query:
            speak("opening the instagram")
            instagram()
    elif 'joke' in query:
            speak(pyjokes.get_joke())

    elif 'set timer' in query:
            speak("please enter the values")
            timer()
    elif 'thank you' in query:
            speak("Your welcome sir.")
    elif 'exit' in query:
            speak("Thank you sir for your time")
            exit()
    elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
    elif 'chat gpt' in query:
            speak ("what you want to saerch")
            api_key = "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"
            chatgpt_voice_assistant(api_key) 
    elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
    elif "who i am" in query:
            speak("If you talk then definitely your human.")
    elif 'ppt' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\praja\\OneDrive\\Documents\\python projects\\"
            os.startfile(power)
    elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

    elif "camera" in query or "take a photo" in query:
            speak("takeing the photos")
            ec.capture(0, "coco ", "img.jpg")
 
    elif 'email to rudra' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prajapatirudra127@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend rudra . I am not able to send this email")
    else:
            print("No query matched")
