import pyautogui
import time 
import random
import pyperclip
import os
import subprocess
import sys

print('starting Test one')
time.sleep(2)
button_a_x = random.randint(1543, 1755)#x vaulues random.randint choses and random vaule with in a box
button_a_y = random.randint(579, 613) #y vaules
 
button_b_x = random.randint(1543, 1594)
button_b_y = random.randint(642, 668)  

button_c_x = random.randint(1542, 1578)
button_c_y = random.randint(706, 730)

button_d_x = random.randint(1541, 1595)
button_d_y = random.randint(767, 791)



def parse_choice(answer):
    normalized = answer.strip().upper()
    if not normalized:
        return None
    if normalized in {"A", "B", "C", "D", "[A]", "[B]", "[C]", "[D]"}:
        return normalized[1] if normalized.startswith("[") else normalized[0]
    if len(normalized) == 2 and normalized[0] in "ABCD" and normalized[1] in ".):-":
        return normalized[0]
    return None




gemini_answer = pyperclip.paste().strip()  # this puts whatever the answer is into your clipboard
if not gemini_answer and len(sys.argv) > 1:
    gemini_answer = " ".join(sys.argv[1:]).strip()
print(f"Gemini replied: {gemini_answer}")

choice = parse_choice(gemini_answer)
was_clicked = False
 

if choice == "A":
    print("Clicking Option A")
    pyautogui.moveTo(button_a_x, button_a_y, duration=0.5)
    pyautogui.click()
elif choice == "B":
    print("Clicking Option B")
    pyautogui.moveTo(button_b_x, button_b_y, duration=0.5)
    pyautogui.click()
elif choice == "C":
    print("Clicking Option C")
    pyautogui.moveTo(button_c_x, button_c_y, duration=0.5)
    pyautogui.click()
elif choice == "D":
    print("Clicking Option D")
    pyautogui.moveTo(button_d_x, button_d_y, duration=0.5)
    pyautogui.click()
elif gemini_answer:
   print("Gemini answer is text, not a single choice letter.")
