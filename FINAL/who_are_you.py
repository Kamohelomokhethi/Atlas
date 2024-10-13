import keyboard
from time import sleep
from speak import Speak
import pyfiglet
from AppOpener import open, close
from pynput.keyboard import Key, Controller


def simulate_typing(message):
    press = Controller()
    sleep(1)
    for key in message:
        sleep(.01)
        press.press(key)
        press.release(key)


def open_and_speak():
    open("notepad")
    message = """
   I am Viper, your personal AI designed to assist with file management, application access, 
   and system control on your PC. I possess the ability to open files and applications, 
   toggle the power state of your computer, and safeguard designated folders. 
   My primary function is to enhance your productivity and security by streamlining tasks and protecting your sensitive data. 
   I operate autonomously, responding to your commands and executing tasks promptly. With my intuitive interface, 
   I simplify complex operations and ensure efficient management of your digital assets. 
   Additionally, I prioritize your privacy and security, 
   employing encryption and access controls to safeguard your confidential information. As a customizable AI, 
   I adapt to your preferences and evolve with your usage patterns, continually improving my performance and effectiveness. 
   Through my seamless integration into your workflow, 
   I empower you to optimize your digital experience and achieve your goals with ease.
    """
    simulate_typing(message)
    Speak(message)
    sleep(2)
    close("notepad")


def main():
    keys = Controller()

    if keyboard.read_key() == "ctrl":  # will use this to let the bot know it's you
        print("ctrl is pressed")
    else:
        print("ndjson")


def art():
    result = pyfiglet.figlet_format("[viper]", font="bulbhead")
    print(result)


if __name__ == "__main__":
    art()
    open_and_speak()
