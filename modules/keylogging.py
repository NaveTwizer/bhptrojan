from pynput.keyboard import Listener
import os

#import MyModule

def on_press(key):
    key = str(key)
    print(key)
    #MyModule.test()


with Listener(on_press=on_press) as listener:
    listener.join()
