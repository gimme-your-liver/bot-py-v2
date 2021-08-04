# Created by breadA#3012

# Imports
from audioplayer import AudioPlayer
from gtts import gTTS
import random
import os
import chats.display
import chats.commands
import inquirer

def tts(msg, language='en'):
    myobj = gTTS(text=msg, lang=language, slow=False)
    myobj.save("audio.mp3")
    AudioPlayer("audio.mp3").play(block=True)


# For Linux



questions = [
  inquirer.Text('name', message="What's your name"),
  inquirer.Confirm('student', message="Are you a student?"),
]

answers = inquirer.prompt(questions)
# { 'name': 'breadA', 'student': True }
name = answers['name']
if answers['name']:
    tts(f"Hello {name}")

if answers['student'] == True:
    tts("Okay, so you are a student? nice!")


