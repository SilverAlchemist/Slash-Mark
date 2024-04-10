import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust the speaking rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said: " + query + "\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble processing your request.")
        return ""

if __name__ == '__main__':
    speak("Hi there! I'm your Voice Assistant")

    while True:
        query = listen()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Can you be more specific?")
        elif 'are you' in query:
            speak("I am your voice assistant")
        elif any(keyword in query for keyword in ['youtube', 'google', 'github', 'stackoverflow', 'spotify']):
            for keyword in ['youtube', 'google', 'github', 'stackoverflow', 'spotify']:
                if keyword in query:
                    speak(f"Opening {keyword.capitalize()}...")
                    webbrowser.open(f"https://www.{keyword}.com")
                    break
        elif any(keyword in query for keyword in ['whatsapp', 'music']):
            for keyword in ['whatsapp', 'music']:
                if keyword in query:
                    speak(f"Opening {keyword.capitalize()}...")
                    if keyword == 'whatsapp':
                        print("No whatsapp for now")
                    else:
                        webbrowser.open("https://www.spotify.com")
                    break
        elif any(disk in query for disk in ['d', 'c', 'e']):
            for disk in ['d', 'c', 'e']:
                if disk in query:
                    speak(f"Opening local disk {disk.upper()}...")
                    os.startfile(f"{disk.upper()}:\\")
                    break
        elif 'sleep' in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")
