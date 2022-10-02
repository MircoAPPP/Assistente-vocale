from secrets import choice
import webbrowser
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
import webbrowser
from random import choice


engine = init()
engine.say("che cavolo vuoi")
engine.runAndWait()
r = Recognizer()

with Microphone () as source:
    print("pronto ad ascoltare...")
    audio = r.listen(source)
    testo = r.recognize_google(audio, language="it_IT").lower()
    risposta= "esprimiti meglio, che non si capisce niente"
    print(testo)

if "ricetta" in testo:
        with open("ricetta.txt", "w") as f:
            f.write("scemo chi legge")
            risposta = "ho creato per te, un testo con la ricetta"
elif any(parola in testo for parola in ["ore", "ora", "orario"]):
        webbrowser.open("www.amazon.it/s?k=orologio")
        risposta= "vai a comprarti un orologio"
elif testo.startswith(("cosa", "come", "quanto")):
        risposta = choice(["e che ne so", "chiedi ad Alexa", "ma che te frega"])
elif "mirko con la c" in testo:
        risposta= "mircoappp è il mio creatore"
elif "versione" in testo:
        risposta= "sono alla versione 0.0.1"
elif "rick roll" in testo:
        webbrowser.open("https://bit.ly/3y21yk1")
        risposta= "never gona give you up"
elif "ciao" in testo: 
        risposta= "Ciao sono ciruzzo che ti ruba l'orologio"
elif "cristiano ronaldo" in testo:
    risposta="suuuuuuuuuuuuuuuuuuuuuuuuuuuu"
elif "alexa" in testo:
    risposta= "sono meglio io non cambiarmi con quello schifo di alexa"
elif "siri" in testo:
    risposta= "ancora quello schifo ma non l'anno cambiato?"
elif "google" in testo:
    risposta= "google è accetabile ma non lo sopporto"
elif "ninna nanna ninna o" in testo:
    risposta="tre mitra sul comò ops ho sbagliato canzone"
elif "sorpresa" in testo:
    risposta="hai trovato una sorpresa ora sei capo della nasa haha stavo scherzando non lo sarai mai"
elif "battuta" in testo:
    risposta= "non mi stufare che stavo dormendo chiedi ad alexa o a google"
elif "corn" in testo:
    webbrowser.open("https://www.youtube.com/watch?v=_caMQpiwiaU&ab_channel=schmoyoho")
    risposta= "its corn"


engine.say (risposta)
engine.runAndWait()