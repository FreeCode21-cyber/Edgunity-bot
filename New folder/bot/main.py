import os
import time
import pyautogui
import sys

print('running')
timebar_x = 1619
timebar_y = 782

next_video_x = 1635 
next_video_y = 825

orange_rgb = (222, 84, 19)

switching_script_x = 1751
switchig_Script_y = 820
switch_rgb = (247, 247, 247)

while True:
    if pyautogui.pixelMatchesColor(timebar_x, timebar_y, orange_rgb, tolerance=10):
        pyautogui.moveTo(next_video_x, next_video_y, duration=0.5)
        pyautogui.click()
        time.sleep(4)
        
        if pyautogui.pixelMatchesColor(switching_script_x, switchig_Script_y, switch_rgb, tolerance=10):
            from answer_bot import run_main_bot
            run_main_bot()
            break

pyautogui.FAILSAFE = True
