# Incase you want to customize for yourself and edit the trigger and exit calls. 
# edit nature from line 24 : <24 WAKE = 'nature'>  |  edit  Sayonara from line 119 : <119  if response == 'Sayonara':>  ****** The commands are caase sensative. some words might not be accepted
# eg : suppose we give  WAKE = 'frank', if you say frank while "Listening". the recived command will be Frank. see the F is caps here and the trigger will not work. so play around with the words
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import date
from datetime import datetime
from sys import exit

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))


# Speech Recognition Constants
recognizer =  sr.Recognizer()
microphone = sr.Microphone()

# Python Text-to-Speech (pyttsx3)  constants
engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

# Wake word
# Say this word to trigger your AI to recive commands
WAKE = "nature"

# Used to store user commands for analysis
CONVERSATION_LOG = "Conversation Log.txt"

# Initial analysis of words that would typically require a google search
SEARCH_WORDS = {"who": "who", "what": "what","when": "when","where": "where", "why": "why", "how": "how","search": "search"}
#

class Nature:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()



    # Used to hear the commands after the wake word has been said
    def hear(self, recognizer, microhphone, response):
        try:
            with microhphone as source:
                print("waiting for command..")
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dynamic_energy_threshold = 3000
                # May reduce the  time out in the future
                audio = recognizer.listen(source, timeout=5.0)
                command = recognizer.recognize_google(audio)
                print(command)
                s.remember(command)
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("network error")

    # Used to speak to the user
    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    # Used to track the date of the conversation, may need to add the time in the future
    def start_conversation_log(self):
        today = str(date.today())
        today = today
        with open('E:\VS Code\Python\AI Workshop\Conversation Log.txt', "a") as f:
            f.write("Conversation started on: " + today + " at "+ datetime.now().strftime("%H : %M : %S") + "\n")
        
    # Writes each command from the user to the conversation log
    def remember(self, command):
        with open('E:\VS Code\Python\AI Workshop\Conversation Log.txt', "a") as f:
            f.write("User: " + command + "\n")

    def find_search_words(self, command):
        # Checks the first word in the command to determine if its a search word
        if SEARCH_WORDS.get(command.split(' ')[0]) == command.split(' ')[0]:
            return True

    # Analysis the command
    def analyze(self, command):
        try:
            # if the command starts with a search word it will do a google search
            if self.find_search_words(command):
                s.speak("here is what i found")
                webbrowser.get('chrome').open("https://www.google.com/search?q={}".format(command))

            # Will need to expand on "open" commands
            elif command == "open youtube":
                s.speak("opening Youtube.")
                webbrowser.get('chrome').open("https://www.youtube.com/")
            elif command == "introduce yourself":
                s.speak("I am Frank Jarvis is my brother from another mother")
            else:
                s.speak("i dont know how to do that yet")
        except TypeError:
            pass
    
    # Used to listen for the wake word

    def listen(self, recognizer, microphone):
        while True:
            try:
                with microphone as source:
                    print("Listening.")
                    recognizer.adjust_for_ambient_noise(source)
                    recognizer.dynamic_energy_threshold = 100
                    audio = recognizer.listen(source, timeout=5.0)
                    
                    response = recognizer.recognize_google(audio)
                    print(response)
                    if response == WAKE:
                        s.speak("how can i help you?")
                        return response.lower()
                    else:
                        pass
                    if response == 'Sayonara': 
                        s.speak("Exiting the A I Adios")  
                        exit()
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Network Error")

s = Nature()
s.start_conversation_log()
while True:
    response = s.listen(recognizer, microphone)
    command = s.hear(recognizer, microphone, response)
    s.analyze(command)








# Currently have some errors and is limited to 
# 1) opening youtube
# 2) opening and searching for something in google search/chrome
# 3) introducing yourself

# The running program also takes time to respond in certain situation