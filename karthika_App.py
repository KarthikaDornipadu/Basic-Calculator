import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import Wikipedia
import pyjokes
import sys
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices)>1:
    engine.setProperty('voice',voices[1].id)
else:
    engine.setProperty('voicec',voices[0].id)
def engine_talk(text):
    print(f"Karthika is saying: {text}")
    engine.say(text)
    engine.runAndWait()
def user-command():
    try:
        with sr.Microphone() as source:
             listener.adjust_for_ambient_noise(source)
             print("Start Speaking ! !")
             voice = listener.listen(source)
             command = listener.recognise_google(voice)
             command =command.lower()
             if 'karthika' in command:
                 command = command.replace('karthika',' ')
                 print(f"User said: {command}")
                 return command
except Exception as e:
       print(f"Error: {e}")
       return " "
def run_karthika():
    command =user_commands()
    if command:
        if 'play' in command:
            song=command.replace('Play', '')
            engine_talk('Playing ' + song)
            pywhatkit.playonyt(song)
       elif 'Who is' in command:
           name=command.replace('Who is', '')
           info=Wikipedia.summary(name,1)
           print(info)
       elif 'joke' in command:
           engine_talk(pyjokes.get_joke()
       elif 'stop' in command:
           sys.exit()
       else:
           engine_talk('I could not hear you properly')
else:     
    engine_talk('I did not catch that. please speak again.')
while True:
     run_karthika()