from main import name
from main import tts
import datetime
import time
import os
# The Input

def speak(msg):
    return tts(msg)

def ip(msg):
    return inputmsg.strip().lower() == msg

def get_time():
    return time.strftime('%l:%M')

def get_date():
    today = datetime.date.today()
    return today.strftime("%b %d %Y")

def get_day():
    today = datetime.date.today()
    return today.strftime("%A")

# The loop to infinity
while 1 == 1:
    inputmsg = input(f"{name} > ")
    # Commands Start from here... 
    if ip("!help"):
        tts("Did you call help?")
    elif ip("hey how are you doing?"):
        tts("I'm good! What about you")
    elif ip("im fine"):
        tts("nice!")
    elif ip("!time"):
        tts(get_time())
    elif ip("!date"):
        tts(get_date())
    elif ip("what is your name"):
        tts("My name is Gimme your liver. For more info type !gyl")
    elif ip("!gyl"):
        print("https://suspicous.link")
    elif ip("!day"):
        tts(get_day())
    elif inputmsg.split(' ')[0] == "!speak":
        speak(inputmsg.split(' ')[1])
        print(" Message spoken. ")
    elif ip("exit()"):
        os.system('exit')
    else:
        print("Sorry, I did not understand what you typed.")