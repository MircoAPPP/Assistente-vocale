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
        risposta= "sono alla versione beta della beta della beta"
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
    risposta= "tre mitra sul comò ops ho sbagliato canzone"
elif "sorpresa" in testo:
    risposta="hai trovato una sorpresa ora sei capo della nasa haha stavo scherzando non lo sarai mai"
elif "battuta" in testo:
    risposta= "non mi stufare che stavo dormendo chiedi ad alexa o a google"
elif "corna" in testo:
    webbrowser.open("https://www.youtube.com/watch?v=_caMQpiwiaU&ab_channel=schmoyoho")
    risposta= "its corn"
elif "voglio studiare" in testo:
    risposta= "ha ha ha ha ha ha ha ha  ha ha troppo divertente, inizia a studiare davvero"
elif "leggimi qualcosa" in testo:
     risposta="non cio sbatti, leggiti manga e taci"
elif "+" in testo:
    risposta= "non fare operazzioni di matematica se non le sai fare neache te, lasciami in pace"
elif "meno" in testo:
    risposta= "non fare operazzioni di matematica se non le sai fare neache te, lasciami in pace"
elif "per" in testo:
    risposta= "non fare operazzioni di matematica se non le sai fare neache te, lasciami in pace"
elif "diviso" in testo:
    risposta= "non fare operazzioni di matematica se non le sai fare neache te, lasciami in pace"
elif "deruba un razzo della nasa" in testo:
    risposta= "aspetta          ok arriverà martedì"
elif "non trovo il libro" in testo:
    risposta= "intendi quello che ho lanciato dal tetto?"
elif "lunghezza" in testo:
    risposta= "ciao come stai non me ne frega niente comunque si chiama così perchè è il comando più lungo di tutti e basta, monnalisa non so cosa dire ma il comando deve essere lungo come detto dal titolo del comando e la pizza con l'ananas è molto buona aiutooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo non si piu cosa dire davvero 695384362623 carbonara e panna gnam gnam addio lol scherzavo a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a ciao non ho ancora finito di parlare bhawtbsergurdgyarekq3ftrggyuagylaryhfgrghafeyfygyefghwfuyfdyghrfhsdfuhyuhgfghdufhudgudhgudgguydghyfyl miao miao niao niao lol lol lol non voglio finire di parlareeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee miao miao niao niao piao devi arrivare fino alla fine del comando se non vuoi perdere la nutella a a a a a a a a a a a aiutoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo non voglio più parlareeee si sono rotte le casse del pc a a a a a a a a a a a non c' è più la nutella a a aa a a a a a a a aa  a a a a a aa a a aaa aa  a aa  a a a pollo pollo pollo vuoi un big mc? io si"

engine.say (risposta)
engine.runAndWait()
