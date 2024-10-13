import keyboard
from time import sleep
from speak import Speak
from AppOpener import open, close
from pynput.keyboard import Controller


def main():
    if keyboard.read_key() == "ctrl":   # will use this to let the bot is me
        print("ctrl is pressed")


def key_press():
    press = Controller()
    open("notepad")
    sentence = """
    I am viper, a friendly personal ai, that was created by Rick,
    with the intention to automate his pc and keep vital files when
    someone but him is using me, ,, or let's say this laptop."""
    sleep(1)
    for key in sentence:
        sleep(.01)
        press.press(key)
        press.release(key)
    Speak(sentence)
    sleep(2)
    close("notepad")

if __name__ == "__main__":
    key_press()