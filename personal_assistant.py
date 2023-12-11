import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit 
import pyautogui 
import wikipedia
import os
import webbrowser

listener=sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command= listener.recognize_google(voice)
            command=command.lower()
            print(command)
            return(command)
    except:
        return ""

def greeting():
    current_time=datetime.datetime.now()
    hour=current_time.hour
    if 3<= hour <12:
        talk('Good Morning Mam!')
    elif 12 <= hour <18:
        talk('Good Afternoon Mam!')
    else:
        talk('Good Evening Mam!')

def run_assistant():
    command= take_command()
    if 'hello' in command:
        talk('Hii I Am Your Personal Assistant')
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    elif 'play' in command:
        song= command.replace('play', "")
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'stop' in command or 'start' in command:
        pyautogui.press('k')
        talk('Done Mam!')
    
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%H:%M %p")
        print(time)
        talk("Current time is" + time)
    
    elif 'open' in command:
        command=command.replace('open',"")
        pyautogui.press('super')
        pyautogui.typewrite(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        talk('Opening'+command)
    
    elif 'close' in command:
        talk("Closing Mam!")
        pyautogui.hotkey('alt','f4')
    
    elif 'who is' in command:
        person= command.replace('who is',"")
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    
    elif 'remember that' in command:
        rememberMessage=command.replace('remember that',"")
        talk('You told me to remember that'+ rememberMessage)
        remember=open('memory.txt',"a")
        remember.write(rememberMessage)
        remember.close()
    
    elif 'what do you remember' in command:
        remember=open('memory.txt',"r")
        talk('you told me to remember'+remember.read())
    
    elif 'clear remember file' in command:
        file=open('memory.txt','w')
        file.write("")
        talk('Done Mam! Everything i remember has been deleted.')
    
    elif 'shutdown' in command:
        talk('closing the pc in')
        talk('3. 2. 1')
        os.system("shutdown /s /t 1")

    elif 'restart' in command:
        talk('restarting the pc in')
        talk('3. 2. 1')
        os.system("shutdown /r /t 1")
    
    elif 'search' in command:
        usercm=command.replace('search',"")
        usercm=usercm.lower()
        webbrowser.open((usercm))
        talk('this is what i found on the internet.')

    elif 'exit' in command:
        talk('Goodbye!')
        exit()

    else:
        talk("I don't understand")

greeting()

while True:
    run_assistant()