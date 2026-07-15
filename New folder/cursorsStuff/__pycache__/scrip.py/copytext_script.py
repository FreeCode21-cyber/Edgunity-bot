import pyautogui
import time
import sys
import random


print('running')
time.sleep(5)
edge_tab_x = 1567
edge_tab_y = 44



word_top_x = 994
word_top_y = 465

word_bottom_x = 1794
word_bottom_y = 757

text_box_top_x = random.randint(1041, 1404)
text_box_top_y = random.randint(677, 767)

pyautogui.moveTo(word_top_x, word_top_y, duration=0.5) 

pyautogui.moveTo(word_top_x, word_top_y, duration=0.5)
pyautogui.dragTo(word_bottom_x, word_bottom_y, duration=1.0, button='left')
time.sleep(0.5)

pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)


pyautogui.moveTo(edge_tab_x, edge_tab_y, duration=0.5)
pyautogui.click()
time.sleep(0.5)

pyautogui.moveTo(text_box_top_x, text_box_top_y, duration=0.5)
pyautogui.click()

pyautogui.hotkey('ctrl','v')





