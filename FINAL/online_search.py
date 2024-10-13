from voice_recognition import Voice_Recognition
import webbrowser as wb
from speak import Speak
import wikipedia

def search_online():
    """Search online using Wikipedia."""
    try:
        Speak("What should I search, my lord!")
        command = Voice_Recognition()
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        print(result)
        Speak(result)
    except wikipedia.exceptions.DisambiguationError as de:
        print(f"Ambiguous search query: {de}")
        Speak("My lord, please provide a more specific search query.")
    except wikipedia.exceptions.PageError as pe:
        print(f"Page not found: {pe}")
        Speak("My apologies, My lord! I could not find any relevant information.")
        return ""


def google():
    """Search on Google."""
    Speak("What should I search? ")
    command = Voice_Recognition()
    search = command.lower()
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    wb.get(edge_path).open("https://www.google.com/search?q=" + search)
    quit()
