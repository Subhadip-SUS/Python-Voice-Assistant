import tkinter
from tkinter import *
from why import *
import customtkinter
import os
from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import pyautogui 
from time import sleep 
import screen_brightness_control as sbc 
import pyscreenshot
from tkinter import messagebox
import time
from bs4 import BeautifulSoup
import requests
import subprocess
from ecapture import ecapture as ec
import sys
import platform
import bs4                                         # pip install beautifulsoup4
import clipboard
import wolframalpha                                # pip install wolframalpha
from quote import quote                            # pip install quote
import winshell as winshell                        # pip install winshell
from geopy.geocoders import Nominatim              # pip install geopy  and pip install geocoder
from geopy import distance
import poetpy                                      # pip install poetpy
import MyAlarm      
from pywikihow import search_wikihow               # pip install pywikihow
import json

# poems
# currency exchange
# minigames
# chatgpt
# 




root = customtkinter.CTk()
root.title("My Jarvis")

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")




def textField():

    system = platform.system()

    if system == "Windows":
        print("System: Windows")
        print("Loading Sapi5 engine")
        engine_to_use = "sapi5"
    elif system == "Darwin":
        print("System: MacOS")
        print("Loading nsss engine")
        engine_to_use = "nsss"
    else:
        # Linux, Posix, BSD, etc.
        print("System: %s" % system)
        print("Loading espeak engine")
        engine_to_use = "espeak"
    try:
        engine = pyttsx3.init(engine_to_use)
    except Exception as err:
        print("Could not load the TTS engine. Do you have it properly installed?")
        print("Error:")
        print(err)
        sys.exit("Critical Error")

    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'voices[0].id')

    list_of_jokes = ["The three most well known languages in India are English, Hindi, and... JavaScript","Interviewer... Where were you born?Me in India... Interviewer:.. oh, which part?... Me: What ‘which part’ ..? Whole body was born in India","how many Indians does it take to fix a lightbulb?Two. One to do the task and other to explain how lightbulbs were actually invented in ancient India","What do you call bread from India? It's Naan of your business","Britain: Drive on the left side... Europe and America: Drive on the right side...India: lol what's a 'traffic law'?"]
    jokes = len(list_of_jokes)-1
    ran_joke=random.randint(0,jokes)
    root.update()


    
    def speak(audio): #speak audio
        root.update()
        engine.say(audio)
        root.update()
        engine.runAndWait()
        root.update()
    def wishMe(): #wishes me
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<=3:
            speak("It's Late Night Sir!, You should sleep right now")
        elif hour>=4 and hour<12:
            speak("Good Moring Master!")
        elif hour>=12 and hour<17:
            speak("Good Afternoon Sir !")
        elif hour>=17 and hour<19:
            speak("Good Evening !")
        elif hour>=19 and hour<24:
            speak("Good Night Sir!")
        if hour>=0 and hour<=4:
            pass
        else:
            speak("I am Your Personal assistant, Jarvis! version 1.0!")
    def takeCommand(): #takes microphone inout and returns output
        global meaw
        root.update()
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            meaw = "Listening..."
            global output
            output = customtkinter.CTkLabel(master=root, text=meaw)
            output.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            root.update()
            r.pause_threshold=1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            meaw = "Recognizing..."
            output = customtkinter.CTkLabel(master=root, text=meaw)
            output.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            root.update()
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition
            print(f"User said: {query}\n")  #User query will be printed
            root.update()
        except Exception as e:   
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            meaw = "Say that again please..."
            output = customtkinter.CTkLabel(master=root, text=meaw)
            output.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            root.update()
            print(f"User said: {query}\n")  #User query will be printed
            return "None" #None string will be returned
        return query

    if __name__ == "__main__":
        wishMe()
        speak("How May I Help You Sir ?")
        while True:
                    # Check the internet connection
            try:
                requests.get('https://www.google.com/').status_code
                query = takeCommand().lower()
            except:
                speak('Internet is not connected, Sir')

            
            if 'wikipedia' in query:
                speak('Searching in Wikipedia')
                query = query.replace("according to wikipedia","")
                results=wikipedia.summary(query, sentences=2)
                speak("Accoring to Wikipedia")
                print(results)
                speak(results)
                speak("anything else for which i may assist you")

            # Take screenshot
            elif 'screenshot' in query:
                speak("screenshot taking ,sir")
                times = time.time()
                name_img = r"{}.png".format(str(times))
                img = pyautogui.screenshot(name_img)
                speak("screenshot is taken, sir")
                img.show()

            # It can read the selected text
            elif 'read' in query:
                text = clipboard.paste()
                try:
                    speak(text)
                except Exception as e:
                    speak("Cannot read the text ,sir")

            # elif 'covid' in query:
            #     r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
            #     json = r.json()
            #     speak("Total Cases are {}, Total death are {}, Total recovered are {}".format(json['cases'], json['deaths'],
            #                                                                             json['recovered']))

            elif 'covid 19' in query or 'corona' in query:
                speak('For which region u want to see the Covid-19 cases. '
                            'Overall cases in the world or any specific country?')
                c_query = takeCommand()
                if 'overall' in c_query or 'over all' in c_query or 'world' in c_query or 'total' in c_query or 'worldwide' in c_query:
                    def world_cases():
                        try:
                            url = 'https://www.worldometers.info/coronavirus/'
                            info_html = requests.get(url)
                            info = bs4.BeautifulSoup(info_html.text, 'lxml')
                            info2 = info.find('div', class_='content-inner')
                            new_info = info2.findAll('div', id='maincounter-wrap')
                            # print(new_info)
                            print('Worldwide Covid-19 information--')
                            speak('Worldwide Covid-19 information--')

                            for i in new_info:
                                head = i.find('h1', class_=None).get_text()
                                counting = i.find('span', class_=None).get_text()
                                print(head, "", counting)
                                speak(f'{head}: {counting}')

                        except Exception as e:
                            pass


                    world_cases()
            elif "initiate" in query or "chat" in query or "Veronica" in query or "gpt" in query:
                def GPT():
                    speak("Connecting to Veronica")
    
                    #Enter API KEY or Leave blank if you don't want to use this function
                    API_KEY = ""
                    openai.api_key = API_KEY
                    if API_KEY == "":
                        print("Please Enter the API Key!")
                        speak("Please Enter the API Key!")
                    while API_KEY != "":
                        engine1 = pyttsx3.init()
                        voices = engine1.getProperty('voices')
                        engine1.setProperty('voice', voices[1].id)
                        r = sr.Recognizer()
                        mic = sr.Microphone(device_index=1)
                        
                    
    
                        conversation = ""
                        
                        user_name = str(input("Enter your name: "))
                        bot_name = "Veronica"
                        print("Hey,"+user_name)
                        
                        while True:
                            with mic as source:
                                print("\nlistening...")
                                r.adjust_for_ambient_noise(source, duration=0.2)
                                audio = r.listen(source)
                            print("no longer listening.\n")
    
                            try:
                                user_input = r.recognize_google(audio)
                            except:
                                continue
    
    
                            prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "
                                
                            conversation += prompt  # allows for context
                                # fetch response from open AI api
                            response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=50)
                            response_str = response["choices"][0]["text"].replace("\n", "")
                            response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
                            
                            conversation += response_str + "\n"
                            print(response_str)
                            engine1.say(response_str)
    
                            prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
    
                            conversation += prompt  # allows for context
                            # fetch response from open AI api
                            response = openai.Completion.create(
                                engine='text-davinci-003', prompt=conversation, max_tokens=50)
                            response_str = response["choices"][0]["text"].replace(
                                "\n", "")
                            response_str = response_str.split(
                                user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
    
                            conversation += response_str + "\n"
                            print(response_str)
                            engine1.say(response_str)
                            engine1.runAndWait()
                GPT()

                elif 'country' in c_query or 'specific country' in c_query:
                    def country_cases():
                        try:
                            speak('Tell me the country name.')
                            c_name = takeCommand()
                            c_url = f'https://www.worldometers.info/coronavirus/country/{c_name}/'
                            data_html = requests.get(c_url)
                            c_data = bs4.BeautifulSoup(data_html.text, 'lxml')
                            new_data = c_data.find('div', class_='content-inner').findAll('div', id='maincounter-wrap')
                            # print(new_data)
                            print(f'Covid-19 information for {c_name}--')
                            speak(f'Covid-19 information for {c_name}')

                            for j in new_data:
                                c_head = j.find('h1', class_=None).get_text()
                                c_counting = j.find('span', class_=None).get_text()
                                print(c_head, "", c_counting)
                                speak(f'{c_head}: {c_counting}')

                        except Exception as e:
                            pass


                    country_cases()

            elif 'what you want to do' in query:
                speak("I want to help people to do certain tasks on their single voice commands.")

            elif 'alexa' in query:
                speak("I don't know Alexa, but I've heard of Alexa. If you have Alexa, "
                            "I may have just triggered Alexa. If so, sorry Alexa.")

            elif 'google assistant' in query:
                speak("He was my classmate, too intelligent guy. We both are best friends.")

            elif 'siri' in query:
                speak("Siri, She's a competing virtual assistant on   a competitor's phone. "
                            "Not that I'm competitive or anything.")

            elif 'cortana' in query:
                speak("I thought you'd never ask. So I've never thought about it.")

            elif 'python assistant' in query:
                speak("Are you joking. You're coming in loud and clear.")

            elif 'what language you use' in query:
                speak("I am written in Python and I generally speak english.")

            elif 'what can you do' in query:
                speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
                speak("Just give me commands Master!")

            elif 'show me' in query and 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            elif 'open youtube' in query:
                speak("Here We Go")
                webbrowser.open("youtube.com")
                speak("anything else for which i may assist you")

            elif 'youtube' in query and 'search' in query:
                speak("What Should I Search Sir ?")
                search_yt=takeCommand()
                search_yt=search_yt.replace(" ","+")
                speak("Here We Go")
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_yt}")
                speak("anything else for which i may assist you")

            elif 'ask' in query:
                question = takeCommand()
                app_id = "R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif 'open google' in query:
                speak("Here We Go")
                webbrowser.open("google.com")
                speak("anything else for which i may assist you")

            elif 'search' in query:
                query=query.replace("search","")
                query=query.replace(" ","+")
                speak("Here We Go")
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak("anything else for which i may assist you")

            elif 'open instagram' in query:
                speak("Here We Go")
                webbrowser.open("instagram.com")
                speak("anything else for which i may assist you")

            elif 'open facebook' in query:
                speak("Here We Go")
                webbrowser.open("facebook.com")
                speak("anything else for which i may assist you")

            elif 'open twitter' in query:
                speak("Here We Go")
                webbrowser.open("twitter.com")
                speak("anything else for which i may assist you")

            elif 'download youtube videos' in query:
                speak("Here We Go")
                webbrowser.open("en.onlinevideoconverter.pro")
                speak("anything else for which i may assist you")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(strTime)
                speak("anything else for which i may assist you")

            elif 'the date' in query:
                today=datetime.date.today()
                speak(today)
                speak("anything else for which i may assist you")

            elif 'set alarm' in query:
                speak("Tell me the time to set an Alarm. For example, set an alarm for 11:21 AM")
                a_info = takeCommand()
                a_info = a_info.replace('set an alarm for', '')
                a_info = a_info.replace('.', '')
                a_info = a_info.upper()
                MyAlarm.alarm(a_info)

            elif query == 'jarvis':
                speak("At Your Service Sir, How can I help you")

            elif 'joke' in query:
                speak(list_of_jokes[ran_joke])
                speak("anything else for which i may assist you")

            elif "volume" in query and 'up' in query:
                pyautogui.press("volumeup", presses=5)
                speak("volume upped")
                sleep(1)
                speak("anything else for which i may assist you")

            elif "volume" in query and 'down' in query:
                pyautogui.press("volumedown", presses=5)
                speak("volume lowered")
                sleep(1)
                speak("anything else for which i may assist you")
                
            elif "mute" in query:
                pyautogui.press("volumemute")
                speak("volume muted")
                sleep(1)
                speak("anything else for which i may assist you")

            elif "brightness" in query:
                try:
                    speak("Which brighness level do you want ?")
                    current=sbc.get_brightness()
                    bright=int(takeCommand())
                    set=sbc.set_brightness(bright)
                    speak(f"brightness set to {bright} percent")
                    sleep(1)
                    speak("anything else for which i may assist you")
                except Exception as e:
                    print(e)
                    speak("error")




            elif 'todo' in query or 'to do' in query:
                if 'add' in query or 'create' in query:
                    with open('todo.txt','a') as f:
                        todo_w=takeCommand()
                        f.write(f"{todo_w}\n")
                    speak("To Do is updated successfully !")                    
                elif 'read' in query or 'tell' in query:
                    with open('todo.txt','r') as f:
                        todo_r=f.read()
                        if todo_r =="":
                            todo_r="No Pendning Tasks Sir"
                        speak(todo_r)
                elif 'erase' in query or 'remove all' in query or 'clear' in query:
                    with open("todo.txt","w") as f:
                        f.write("")
                    speak("All Tasks has been cleared, Sir !")

            elif 'pause' in query or 'stop' in query and 'song' in query:
                pyautogui.press("playpause")
                speak("vMusic Paused")
                sleep(1)
                speak("anything else for which i may assist you")

            elif 'change' in query and 'song' in query:
                pyautogui.press("nexttrack", presses=1)
                sleep(1)
                speak("anything else for which i may assist you")

            elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
                speak("Thank you for using Jarvis Sir")
                exit()

            elif 'note' in query or 'notes' in query:
                speak("What to write on that note?")
                notes=takeCommand()
                with open(f"note.txt",'a') as f:
                        f.write(f"{notes}\n")
    
                speak("We updated your notes successfully !")
                speak("anything else for which i may assist you")

            elif "log off" in query or "sign out" in query:
                speak(
                    "Ok , your pc will log off in 10 seconds! make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
            
            elif "camera" in query or "take a photo" in query:
                ec.capture(0, "Jarvis camera", "img.jpg")
            

            elif "weather" in query or 'temperature' in query:
                speak("which city should I search in")
                try:
                    cty = takeCommand()
                    try:
                        cty=cty.replace(" ","+")
                        search = "temperature in" + cty 
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    except:
                        speak("City Not Found ")
                except:
                    speak("error")

            elif "who made you" in query or "who created you" in query or "who discovered you" in query:
                speak("I was built by a Human")
                print("I was built by a Human")

            elif 'distance' in query:
                geocoder = Nominatim(user_agent="Singh")
                speak("Tell me the first city name??")
                location1 = takeCommand()
                speak("Tell me the second city name??")
                location2 = takeCommand()

                coordinates1 = geocoder.geocode(location1)
                coordinates2 = geocoder.geocode(location2)

                lat1, long1 = coordinates1.latitude, coordinates1.longitude
                lat2, long2 = coordinates2.latitude, coordinates2.longitude

                place1 = (lat1, long1)
                place2 = (lat2, long2)

                distance_places = distance.distance(place1, place2)

                print(f"The distance between {location1} and {location2} is {distance_places}.")
                speak(f"The distance between {location1} and {location2} is {distance_places}")

            elif 'how to' in query:
                try:
                    # query = query.replace('how to', '')
                    max_results = 1
                    data = search_wikihow(query, max_results)
                    # assert len(data) == 1
                    data[0].print()
                    speak(data[0].summary)
                except Exception as e:
                    speak('Sorry, I am unable to find the answer for your query.')

            # elif 'news' in query or 'news headlines' in query:
            #     url = "https://news.google.com/news/rss"
            #     client = webbrowser(url)
            #     xml_page = client.read()
            #     client.close()
            #     page = bs4.BeautifulSoup(xml_page, 'xml')
            #     news_list = page.findAll("item")
            #     speak("Today's top headlines are--")
            #     try:
            #         for news in news_list:
            #             print(news.title.text)
            #             speak(f"{news.title.text}")
            #             print()

            #     except Exception as e:
            #         pass



            else:
                speak("sorry I can't help, Please give another command")




def buttonpressed():
    button.destroy()
    textField()
    
root.geometry('300x300')
button = customtkinter.CTkButton(master=root, text="Tap to Start", command=buttonpressed)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
root.mainloop()
