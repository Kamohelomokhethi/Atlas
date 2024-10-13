import sys
import updates
import voice_recognition
import music
import online_search
import close_and_open_apps
import memory
import speak
from identify import key_press
import os
from who_are_you import open_and_speak , art


if __name__ == "__main__":
    art()
    updates.greetings()
    while True:
        try:
            command = voice_recognition.Voice_Recognition()

            if "time" in command or "date" in command:
                updates.get_time()
            elif "hey" in command or "hi" in command or "high" in command or "hello" in command:
                speak.Speak("hello there, how can i assist you?")

            elif "hey viper" in command or "hey" in command:
                speak.Speak("hello, how can  i assist you today?")
            if "who are you" in command or "what are you" in command or "what can you do" in command:
                open_and_speak()
            elif "offline" in command:
                speak.Speak("going offline")
                sys.exit()
            elif "cpu" in command:
                updates.check_cpu_and_battery_usage()
            elif "google" in command:
                online_search.google()
            elif "search" in command or "wikipedia" in command:
                online_search.search_online()
            elif "songs" in command or "music" in command:
                music.music()
            elif "open apps" in command:
                close_and_open_apps.run_apps()
            elif "close apps" in command:
                close_and_open_apps.Close_apps()
            elif "store" in command:
                memory.remember()
            elif "recall" in command or "remember" in command:
                memory.remind_me()
            elif "who are you" in command or "what is your name" in command:
                key_press()
            elif "shutdown" in command or "shut down" in command:
                speak.Speak("Shutting down...")
                os.system("shutdown /s /t 1")
            elif "sleep" in command:
                speak.Speak("Sleeping")
                os.system("shutdown /h")
            elif "log out" in command or "log out" in command:
                speak.Speak("Logging out....")
                os.system("shutdown -l")
            elif "restart" in command:
                speak.Speak("Restarting....")
                os.system("shutdown /r /t 1")

        except Exception as e:
            print(e)
