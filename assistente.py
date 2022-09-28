from secrets import choice
import webbrowser
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
import webbrowser
from random import choice

engine = init()
engine.say("non mi stufare che ho il covid")
engine.runAndWait()
r = Recognizer()

with Microphone() as source:
    print("pronto ad ascoltare...................")
    audio = r.listen(source)
    testo = r.recognize_google(audio, language="it-IT").lower()
    risposta = "esprimiti meglio che non capisco niente"
    print(testo)

    if "ricetta " in testo:
        with open("ricetta.txt", "w") as f:
            f.write("scemo chi legge")
            risposta = "ho creato per te, un testo con la ricetta"
    elif any(parola in testo for parola in ["ore", "ora", "orario"]):
        webbrowser.open("www.amazon.it/s?k=orologio")
        risposta= "vai a comprarti un orologio"
    elif testo.startswith(("cosa", "come", "quanto")):
        risposta = choice(["e che ne so", "chiedi ad Alexa", "ma che te frega"])
    engine.say (risposta)
    engine.runAndWait()