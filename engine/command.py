import pyttsx3
import speech_recognition as sr
import eel
import time




def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            eel.DisplayMessage("Timeout: No speech detected. Returning to standby...")
            return ""  # Returning to main loop or 'hood'

    try:
        print('recognizing....')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        return query.lower()

    except sr.UnknownValueError:
        print("Could not understand the audio.")
        eel.DisplayMessage("Could not understand, please try again.")
        return ""

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        eel.DisplayMessage("Service error, please check your connection.")
        return ""

    except Exception as e:
        print(f"Error: {str(e)}")
        eel.DisplayMessage("An unexpected error occurred.")
        return ""
@eel.expose

def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall
            contact_no, name = findContact(query)
            if contact_no != 0:
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()

                if preferance.strip() == "":
                    speak("No input received")
                    eel.ShowHood()
                    return

                print(preferance)

                if "mobile" in preferance:
                    if "phone call" in query:
                        makeCall(name, contact_no)
                    elif "send message" in query:
                        speak("Currently this feature is not present But you can get it in later upgrade")
                    else:
                        speak("Please try again")

                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("What message to send")
                        query = takecommand()
                    elif "phone call" in query:
                        message = 'call'
                    elif "video call" in query:
                        message = 'video call'

                    whatsApp(contact_no, query, message, name)

        else:
            from engine.features import chatBot
            chatBot(query)

    except Exception as e:
        print("error:", str(e))

    eel.ShowHood()
