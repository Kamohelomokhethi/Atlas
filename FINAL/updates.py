import speak
import datetime
import psutil
import time


def get_time():
    """Get and speak the current time."""
    current_time = time.ctime()
    speak.Speak(f"The current date and time is, {current_time}...")


def greetings():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak.Speak("Good Morning sir,")
    elif 12 <= hour < 18:
        speak.Speak("Good afternoon sir!")
    elif 18 <= hour < 24:
        speak.Speak("Good evening sir!")
    speak.Speak("Your loyal servant is ready to serve, my lord! I'm yours to command... ")


def check_cpu_and_battery_usage():
    """Check CPU and battery usage."""
    cpu_usage = str(psutil.cpu_percent())
    #speak.Speak(f"CPU usage is currently at {cpu_usage}")

    battery = psutil.sensors_battery()
    speak.Speak(f"Battery percentage is currently at {battery.percent}")

if __name__ == "__main__":
    check_cpu_and_battery_usage()
"""def get_my_mood():
    Speak("someone is in danger!!!!!  ")
    command = Voice_Recognition()
    if "red one" in command or "asus" in command:
        try:
            Speak("starting theme..")
            os.startfile("C:/backup/ROG.deskthemepack")
        except Exception as e:
            print(e)
            Speak("failed to start")

    elif "windows theme" in command or "white" in command:
        try:
            Speak("starting theme...")
            os.startfile("C:/WINDOWS/Resources/Themes/Light.theme")
        except Exception as e:
            print(e)
            Speak("failed to start.")"""
