import pyautogui
import pyperclip
import time 
import os



try:
    while True:
        x, y = pyautogui.position()

        position_str = f"X: {str(x).rjust(4)}  Y: {str(y).rjust(4)}"
     
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass