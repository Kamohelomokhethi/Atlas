from voice_recognition import Voice_Recognition
from speak import Speak

def remember():
    """Remember a command."""
    try:
        Speak("What should I remember, My Lord?")
        data = Voice_Recognition()

        # Writing to a file things the bot should remember
        Speak(f"You told me to remember that, {data}")
        with open("remember.vp", "a") as file:
            memory = f"you told me to remember that, {data} \n"
            file.write(memory)

    except Exception as e:
        print(e)
        Speak("failed")
        return " "

def remind_me():
    """Remind the user of remembered commands."""
    Speak("Here's what I remember, My lord!")
    try:
        with open("remember.vp", "r") as file2:
            read = file2.read()
            print(read)
            Speak(read)

    except Exception as e:
        print(e)
        Speak("I am not able to recall")
        return " "
