import pyttsx3 as tts
import speech_recognition as sr

engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
g_txt = "Hi, this is your talking Py-Bot."
print(g_txt)
r = sr.Recognizer()

tts.speak(g_txt)
bot_name = "blank"
with sr.Microphone() as source:

    str = "\nSay something: "
    r.adjust_for_ambient_noise(source, 3)
    print(str)

    speech = ''
    while(True):
        try:
            tts.speak("Say something")
            audio = r.listen(source)
            speech = r.recognize_google(audio,language='en-US')
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

            elif "set your name" in speech:
                str = "\n*You*: " + speech
                bot_name = str.split()[-1]
                print(str)
                str = "Okay Tariq, from now on my name is " + bot_name
                tts.speak(str)
                print("*Py-Bot*: " + str)

            elif "your name" in speech:
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

        except sr.UnknownValueError:
            str = "\nSorry, could not understand what you said."
            tts.speak(str)
            print(str)

        except sr.RequestError as e:
            str = "\nRequest Error"
            tts.speak(str)
            print(str)

