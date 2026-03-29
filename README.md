---

# 🎙️ Raphael – Personal Voice Assistant

> An intelligent desktop-based voice assistant that listens, understands, and performs tasks using voice commands.

---

## 📌 Project Overview

**Raphael** is a smart AI-powered voice assistant built using Python and modern web technologies. It allows users to interact with their system hands-free by giving voice commands.

The assistant can:

* 🎧 Listen to voice input
* 💬 Convert speech to text
* ⚙️ Execute system-level tasks
* 🔊 Respond using text-to-speech
* 🌐 Provide AI-generated responses

---

## 🚀 Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech response
* 💻 Open desktop applications
* 🌍 Open websites (YouTube, WhatsApp, etc.)
* 💬 Chat interface with history
* 📱 WhatsApp automation (message, call, video call)
* 🤖 AI conversation using HugChat
* 🔁 Real-time frontend-backend communication (Eel)

---

## 🛠️ Tech Stack

### 🔹 Frontend

* HTML
* CSS
* JavaScript
* Bootstrap
* SiriWave.js
* Textillate.js

### 🔹 Backend

* Python
* Eel

### 🔹 Libraries Used

* `pyttsx3` (Text-to-Speech)
* `speech_recognition` (Speech-to-Text)
* `pyaudio` (Mic input)
* `pyautogui` (Automation)
* `sqlite3` (Database)
* `hugchat` (AI responses)

---

## 🧠 How It Works

1. User clicks mic 🎤
2. Speech is captured using `pyaudio`
3. Converted to text via `speech_recognition`
4. Command is processed:

   * Custom logic OR
   * AI (HugChat)
5. Action is executed:

   * Open app / website / send message
6. Response is:

   * Displayed on UI 💻
   * Spoken using `pyttsx3` 🔊

---

## 🏗️ Architecture

```
Frontend (HTML/CSS/JS)
        ⬇️
       Eel (Bridge)
        ⬇️
Python Backend (Logic + AI + Automation)
        ⬇️
System / APIs / Database
```

---

## 📂 Project Structure

```
Raphael-Voice-Assistant/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   ├── commands.py
│   └── database.db
│
├── assets/
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/raphael-voice-assistant.git
cd raphael-voice-assistant
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Project

```bash
python main.py
```

---

## 📱 Key Functional Modules

### 🔹 Voice Processing

* Speech input via microphone
* Real-time speech-to-text

### 🔹 AI Response

* HugChat integration
* Context-based replies

### 🔹 Automation

* Open apps using OS commands
* WhatsApp automation
* YouTube playback

### 🔹 Database

* SQLite for storing:

  * Commands
  * Contacts

---

## ⚠️ Challenges Faced

* 🔧 Frontend–Backend integration using Eel
* 🗣️ Speech recognition accuracy (noise, accents)
* 🔐 Managing AI session authentication
* 📱 WhatsApp automation reliability
* 📞 Mobile integration via ADB

---

## 🔮 Future Enhancements

* 🌐 Multilingual support
* 🎤 Wake word detection (e.g., “Hey Raphael”)
* 📱 Mobile application version
* 🧠 Advanced AI model integration
* 🔐 Voice-based authentication

---

## 📊 Learning Outcomes

* Full-stack development (Frontend + Python Backend)
* Voice processing & speech recognition
* API integration (AI models)
* Automation using Python
* Real-world project architecture

---

## 🙌 Conclusion

Raphael demonstrates how AI, voice processing, and automation can be combined to create a powerful and user-friendly assistant. It is scalable, interactive, and a strong showcase of real-world development skills.

---

## 📸 Interface

*<img width="810" height="697" alt="image" src="https://github.com/user-attachments/assets/59889fe4-6510-4508-9c8c-16c6269ec316" />


---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---

---

