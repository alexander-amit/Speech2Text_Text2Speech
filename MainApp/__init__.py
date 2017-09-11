import speech_recognition as sr
import pyttsx3
        
    
r = sr.Recognizer()
with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
try:
        saidbyme=r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + saidbyme)
        engine = pyttsx3.init()
        engine.say(saidbyme)
        engine.runAndWait()
except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    