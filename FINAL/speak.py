import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def Speak(audio):
    """Converts text to speech and speaks it.
    @rtype: object
    """
    words = audio.split()
    cleaned_words = [word.replace("_", " ") for word in words]
    cleaned_audio = " ".join(cleaned_words)
    engine.say(cleaned_audio)
    engine.runAndWait()

