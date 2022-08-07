from pynput.keyboard import Listener
import os


def on_press(key):
    key = str(key)
    print(key)


with Listener(on_press=on_press) as listener:
    listener.join()
