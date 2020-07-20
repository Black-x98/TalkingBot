import pyttsx3 as tts
import datetime

engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
g_txt = "Hi, this is your talking Py-Bot."
print(g_txt)


tts.speak(g_txt)
bot_name = "blank"

str = "\nSay something: "
print(str)

speech = ''
while(True):

    tts.speak("Say something")
    speech = input()
    if "hi" in speech or "hello" in speech:
        str = "\n*You*: " + speech
        print(str)
        str = "Hello Tariq."
        tts.speak(str)
        print("*Py-Bot*: " + str)

    elif "bye" in speech or "turn off" in speech:
        str = "\n*You*: " + speech
        print(str)
        str = "Okay Tariq, I am shutting down, bye."
        tts.speak(str)
        print("*Py-Bot*: " + str)
        break

    elif "no" in speech: # "what" in speech or "tell" in speech and
        str = "\n*You*: " + speech
        bot_name = str.split()[-1]
        print(str)
        str = "Today is " + datetime.datetime.now().__str__()
        tts.speak(str)
        print("*Py-Bot*: " + str)

    elif "today" in speech: # "what" in speech or "tell" in speech and
        str = "\n*You*: " + speech
        bot_name = str.split()[-1]
        print(str)
        datenow = datetime.datetime.now()
        str = "Today is " + datenow.strftime("%A") + " " + datenow.strftime("%B") + " " +  datenow.strftime("%C") + " year " + (datenow.year).__str__()
        tts.speak(str)
        print("*Py-Bot*: " + str)

    elif "change" in speech or "set" in speech and "your name" in speech:
        str = "\n*You*: " + speech
        bot_name = str.split()[-1]
        print(str)
        str = "Okay Tariq, from now on my name is " + bot_name
        tts.speak(str)
        print("*Py-Bot*: " + str)

    elif "change" in speech and "your name" in speech or "set" in speech and "your name" in speech:
        str = "\n*You*: " + speech
        bot_name = str.split()[-1]
        print(str)
        str = "Okay Tariq, from now on my name is " + bot_name
        tts.speak(str)
        print("*Py-Bot*: " + str)

    elif "what" in speech or "tell" in speech and "your name" in speech:
        if bot_name=="blank":
            str = "\n*You*: " + speech
            print(str)
            str = "I haven't been given any personal name yet.\nBut you can call me Py-Bot for now."
            tts.speak(str)
            print("*Py-Bot*: " + str)
        else:
            str = "\n*You*: " + speech
            print(str)
            str = "My name is " + bot_name
            tts.speak(str)
            print("*Py-Bot*: " + str)

    elif "laugh" in speech:
        str = "\n*You*: " + speech
        print(str)
        str = "Ha ha ha ha ha ha!!!!!"
        tts.speak(str)
        print("*Py-Bot*: " + str)


    elif "language" in speech:
        str = "\n*You*: " + speech
        print(str)
        str = "I am coded using Python."
        tts.speak(str)
        print("*Py-Bot*: " + str)

    elif "how are you" in speech:
        str = "\n*You*: " + speech
        print(str)
        str = "I am just a chatbot, that doesn't apply for me.\nBut I hope you are doing well."
        tts.speak(str)
        print("*Py-Bot*: " + str)
    else:
        str = "\nYou said: " + speech
        tts.speak("You said: " + speech)
        print(str)



