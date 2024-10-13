import speech_recognition as SR
from speak import Speak


def Voice_Recognition():
    """Perform voice recognition."""
    r = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        command = r.recognize_google(audio, language='en-in').lower()
        print(command)
        return command

    except Exception as e:
        print(e)
        Speak("Sorry, may you please repeat your command, my lord!")
        return None
