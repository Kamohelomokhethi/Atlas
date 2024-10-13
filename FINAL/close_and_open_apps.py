from voice_recognition import Voice_Recognition
from AppOpener import open, close
from speak import Speak
import os


def run_apps():
    """Run applications based on voice command."""
    Speak("Which application should I open, My Lord!")
    my_app = Voice_Recognition()
    try:
        if "settings" in my_app:
            Speak("Opening settings......")
            open("settings", match_closest=True)

        elif "files" in my_app or "explorer" in my_app:
            open("File Explorer", match_closest=True)

        elif "notepad" in my_app:
            Speak("Opening notepad....")
            open("notepad", match_closest=True)

        elif "word" in my_app or "microsoft word" in my_app:
            Speak("Opening microsoft word..")
            open("word", match_closest=True)

        elif "whatsapp" in my_app or "whats up" in my_app or "what's up" in my_app:
            Speak("Opening whatsapp")
            open("whatsapp", match_closest=True)

        elif "music" in my_app or "groove music" in my_app or "groove" in my_app:
            Speak("Opening groove music..")
            open("Groove Music", match_closest=True)

        elif "edge" in my_app or "microsoft edge" in my_app:
            Speak("Opening microsoft edge...")
            open("Microsoft Edge", match_closest=True)

        elif "vlc" in my_app or "video player" in my_app:
            Speak("Opening Vlc media player..")
            open("VLC media player", match_closest=True)

    except Exception as e:
        print(e)

        with(open("error.er", "r")) as file:
            file.write(e)
        Speak("Failed to open the app, My lord! ")


def Close_apps():
    """Close applications based on voice command."""
    Speak("Which Application should I close, my lord")
    app_to_close = Voice_Recognition()
    try:
        if "files" in app_to_close or "explorer" in app_to_close:
            Speak("Closing file explorer")
            close("File Explorer", match_closest=True)

        elif "whatsapp" in app_to_close or "whats app" in app_to_close or "what's up" in app_to_close:
            Speak("Closing whatsapp")
            close("whatsapp", match_closest=True)

        elif "word" in app_to_close or "microsoft word" in app_to_close:
            Speak("Closing microsoft word")
            os.system("taskkill /f /im WINWORD.EXE /t")

        elif "notepad" in app_to_close:
            Speak("Closing notepad")
            close("notepad", match_closest=True)

        elif "edge" in app_to_close or "microsoft edge" in app_to_close:
            Speak("Closing Microsoft edge")
            close("Microsoft Edge", match_closest=True)

        elif "settings" in app_to_close:
            Speak("Closing settings")
            close("settings", match_closest=True)

        elif "music" in app_to_close:
            Speak("Closing groove music")
            os.system("taskkill /f /im Music.UI.exe /t")

        elif "vlc" in app_to_close or "video player" in app_to_close:
            os.system("taskkill /f /im vlc.exe /t")

    except Exception as e:
        print(e)
        Speak("Failed to close the application, my lord! I apologize.")
