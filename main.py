import speech_recognition as sr
import webbrowser
import win32com.client
import musicLibrary
import time  # Added to handle loop delays

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def set_voice(voice_name):
    voices = speaker.GetVoices()
    for i in range(voices.Count):
        voice = voices.Item(i)
        if voice_name.lower() in voice.GetDescription().lower():
            speaker.Voice = voice
            break

def speak(text):
    print(f"🤖 Arya says: {text}")
    try:
        # Using 1 for async mode. 
        speaker.Speak(text, 1)

        # FIX 1: Give Windows a brief moment to process the speech stream 
        # so it doesn't overlap with the microphone opening

        time.sleep(2) 
    except Exception as e:
        print(f"⚠️ Speech Engine Warning: {e}")

def processcommand(command):
    command = command.lower().strip()
    print(f"🧠 Processing command: '{command}'")

    if "female voice" in command:
        set_voice("Zira")
        speak("Female voice activated.")
        return True      # Keep Arya awake after changing voice

    elif "male voice" in command:
        set_voice("David")
        speak("Male voice activated.")
        return True      # Keep Arya awake after changing voice

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True      # Keep Arya awake after opening Google

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True      # Keep Arya awake after opening YouTube

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        return True      # Keep Arya awake after opening Facebook

    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        return True     # Keep Arya awake after opening LinkedIn
    
    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"I couldn't find '{song}' in your music library.")
        return True 
    
    elif "sleep" in command or "stop" in command or "exit" in command:
        speak("Going back to sleep. Wake me up if you need me.")
        return False 
    
    else:
        speak("I heard you, but I don't have a programmed response for that.")
        return True 


if __name__ == "__main__":
    set_voice("David")
    speak("Initializing Arya....")
    
    r = sr.Recognizer()
    
    while True:
        print("\n--- SLEEP MODE ---")
        print("Listening for wake word 'Arya'...") 

        try:
            with sr.Microphone() as source:
                 # We set a hardcoded threshold here so we DO NOT need adjust_for_ambient_noise
                 r.adjust_for_ambient_noise(source, duration=1)
                 r.energy_threshold = 300
                 audio = r.listen(source, timeout=2, phrase_time_limit=4)

            word = r.recognize_google(audio).lower()
            print(f"🗣️ You said: {word}")

            if "arya" in word:
                speak("Yes Yuvi?")
                
                is_awake = True
                while is_awake:
                    try:
                        with sr.Microphone() as source:
                             print("\n👂 [ACTIVE MODE] Ready for your command...")
                             r.adjust_for_ambient_noise(source, duration=1)
                             r.energy_threshold = 200
                             audio = r.listen(source, timeout=8, phrase_time_limit=5)

                        command = r.recognize_google(audio).lower()
                        print(f"🗣️ You commanded: {command}")
                        is_awake = processcommand(command)

                    except sr.WaitTimeoutError:
                        speak("I didn't hear anything. Going back to sleep.")
                        is_awake = False

                    except sr.UnknownValueError:
                        print("Active Mode: Could not understand the audio.")

        except sr.UnknownValueError:
            print("Sleep Mode: Listening...")
            time.sleep(0.5)
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print(f"🚨 System Alert: {e}")
            time.sleep(1)    # Brief pause before retrying