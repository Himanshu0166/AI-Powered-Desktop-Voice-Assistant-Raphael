from shlex import quote
import subprocess
import time
import pyautogui
from urllib.parse import quote
import struct
import subprocess
import time
import webbrowser
import hugchat
from playsound import playsound
import eel
import pvporcupine
import pyautogui
from engine.command import speak
from engine.constant import ASSISTANT_NAME
import os
import pywhatkit as kit
import pyaudio
import pyttsx3
import sqlite3
from hugchat import hugchat
from engine.helper import extract_yt_term, remove_words

con = sqlite3.connect("raphael.db")
cursor = con.cursor()
# Playing assiatnt sound function
@eel.expose
def playAssistantSound():
    music_dir = "frontend\\data\\audio\\startsound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME , "")
    query = query.replace("open", "")
    query.lower()
    app_name = query.strip()
    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:      
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("o")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# Find contacts from the database
import re

def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']

    try:
        # Clean query
        pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
        cleaned_query = re.sub(pattern, '', query, flags=re.IGNORECASE).strip().lower()

        if not cleaned_query:
            speak("I couldn't understand the contact name. Please try again.")
            return 0, 0

        # Parameterized LIKE query for case-insensitive partial match
        cursor.execute("""
            SELECT name, mobile_no 
            FROM contacts 
            WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?
        """, ('%' + cleaned_query + '%', cleaned_query + '%'))

        results = cursor.fetchall()

        if not results:
            speak('Contact not found in your contacts list.')
            return 0, 0

        name, mobile_number = results[0]
        mobile_number_str = str(mobile_number).replace(" ", "")
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, name

    except Exception as e:
        print(f"[ERROR] findContact(): {e}")
        speak('An error occurred while finding the contact.')
        return 0, 0


def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "Message sent successfully to " + name
    elif flag == 'call':
        target_tab = 7
        whatsapp_url = f"whatsapp://send?phone={mobile_no}"
        # Construct the full command to open WhatsApp
        full_command = f'start "" "{whatsapp_url}"'

        # Open WhatsApp with the constructed URL using cmd.exe
        subprocess.run(full_command, shell=True)

        # Add a delay to give WhatsApp time to open
        time.sleep(5)  # Wait for WhatsApp to load properly

        pyautogui.hotkey('ctrl', 'f')  # Open the search bar
        time.sleep(1)
        for i in range(1, target_tab):
            pyautogui.hotkey('tab')  # Navigate tabs to get to the right one
            time.sleep(1)
        jarvis_message = "Calling " + name
        pyautogui.hotkey('enter')  # Select the correct option (message)
        time.sleep(1)
        
    elif flag == 'video call':
        target_tab = 6
        whatsapp_url = f"whatsapp://send?phone={mobile_no}"
        # Construct the full command to open WhatsApp
        full_command = f'start "" "{whatsapp_url}"'

        # Open WhatsApp with the constructed URL using cmd.exe
        subprocess.run(full_command, shell=True)

        # Add a delay to give WhatsApp time to open
        time.sleep(5)  # Wait for WhatsApp to load properly

        pyautogui.hotkey('ctrl', 'f')  # Open the search bar
        time.sleep(1)
        for i in range(1, target_tab):
            pyautogui.hotkey('tab')  # Navigate tabs to get to the right one
            time.sleep(1)
        jarvis_message = "Starting video call with " + name
        pyautogui.hotkey('enter')  # Select the correct option (message)
        time.sleep(1)
        
        

    # Encode the message for URL
    encoded_message = quote(message)
    print("Encoded Message:", encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command to open WhatsApp
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)

    # Add a delay to give WhatsApp time to open
    time.sleep(5)  # Wait for WhatsApp to load properly

    if flag == 'message':
        # Ensure WhatsApp is focused and navigate to the message input field
        pyautogui.hotkey('ctrl', 'f')  # Open the search bar
        time.sleep(1)

        for i in range(1, target_tab):
            pyautogui.hotkey('tab')  # Navigate tabs to get to the right one
            time.sleep(1)

        pyautogui.hotkey('enter')  # Select the correct option (message)
        time.sleep(1)

        # Now we send the message
        pyautogui.write(message)  # Type the message
        pyautogui.press('enter')  # Send the message
        time.sleep(2)


    speak(jarvis_message)  # Speak the confirmation message

# chat bot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response


def makeCall(name, mobileNo):
    mobileNo = mobileNo.replace(" ", "")
    speak("Calling " + name)
    command = f' adb -s 192.168.1.12:5555 shell am start -a android.intent.action.DIAL -d tel:{mobileNo}'
    os.system(command)
