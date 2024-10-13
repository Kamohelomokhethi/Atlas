import os
import time
import random
from voice_recognition import Voice_Recognition
from speak import Speak


def music():
    """Play songs from a predefined folder."""
    Speak("which kind of music, my lord!")
    command = Voice_Recognition()
    if "sad" in command:
        try:
            music_path = "../../../../Music/good&bad"
            songs = os.listdir(music_path)
            random.shuffle(songs)

            for song_names in songs:
                song_path = os.path.join(music_path, song_names)
                song_info = os.path.getsize(song_path)
                print(f"Playing... {song_names}")
                Speak(f"Playing... {song_names}")
                os.startfile(song_path)
                time.sleep(200)

        except Exception as e:
            print(e)
            Speak("Failed to open songs, my lord!")
    elif "instrumentals" in command:
        try:
            music_path = "../../../../Music/[musiv-v]"
            songs = os.listdir(music_path)
            random.shuffle(songs)

            for song_names in songs:
                song_path = os.path.join(music_path, song_names)
                song_info = os.path.getsize(song_path)
                print(f"Playing... {song_names}")
                Speak(f"Playing... {song_names}")
                os.startfile(song_path)
                time.sleep(200)
        except Exception as e:
            print(e)
            Speak("failed to open songs!")

    elif "deep" in command or "deep house" in command:
        try:
            music_path = "../../../../Music/[DEEP-HOUSE]"
            songs = os.listdir(music_path)
            random.shuffle(songs)

            for song_names in songs:
                song_path = os.path.join(music_path, song_names)
                song_info = os.path.getsize(song_path)
                print(f"Playing... {song_names}")
                Speak(f"Playing... {song_names}")
                os.startfile(song_path)
                time.sleep(200)
        except Exception as e:
            print(e)
            Speak("failed to open songs!")

    elif "club" in command or "club house" in command:
        try:
            music_path = "../../../../Music/Club house"
            songs = os.listdir(music_path)
            random.shuffle(songs)

            for song_names in songs:
                song_path = os.path.join(music_path, song_names)
                song_info = os.path.getsize(song_path)
                print(f"Playing... {song_names}")
                Speak(f"Playing... {song_names}")
                os.startfile(song_path)
                time.sleep(200)
        except Exception as e:
            print(e)
            Speak("failed to open songs!")
