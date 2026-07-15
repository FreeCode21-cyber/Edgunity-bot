import pyautogui
import pyperclip
import time
import random
import os
import subprocess
import sys


print('Running scan: ')
time.sleep(2)

start_copy_x = 1036 
start_copy_y = 398

end_copy_x = 1566
end_copy_y = 736

switch_tab_x = 1099
switch_tab_y = 31

target_box_x = 1291
target_box_y = 1070


gemini_response_x = 1065
gemini_response_y = 392

edge_tab_x = 1550
edge_tab_y = 21


done_button_x = 1877
done_button_y = 1048

next_button_x = 1694
next_button_y = 996

button_a_x  = random.randint(1543, 1755)#x vaulues random.randint choses and random vaule with in a box
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





def run_main_bot():#to call to other function
    while True:  # this is my loop

        print("Bot starting in 5 seconds... Quickly switch to your browser or source window.")
        time.sleep(5)
        print("Step 1: Highlighting text...")

        pyautogui.moveTo(start_copy_x, start_copy_y, duration=0.5)
        pyautogui.dragTo(end_copy_x, end_copy_y, duration=1.0, button='left')

        print("Step 2: Copying text...")
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)

        print("Step 3: switch tabs")
        pyautogui.moveTo(switch_tab_x, switch_tab_y, duration=0.8)
        pyautogui.click()
        time.sleep(0.5)

        print("Step 4: Moving to destination and pasting...")
        pyautogui.moveTo(target_box_x, target_box_y, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')

        time.sleep(0.5)
        print("Step 4: Pressing enter")
        pyautogui.press('enter')
        time.sleep(7)

        for seconds in range(2, 0, -1):
            print(f"Waiting for Gemini response: {seconds} seconds")
            time.sleep(1)

        gemini_answer = ""

        try:
            pyautogui.moveTo(gemini_response_x, gemini_response_y, duration=0.5)  # Gemini answer copier
            time.sleep(0.2)
            print("Triple-clicking")
            pyautogui.click(clicks=3, interval=0.20, button='left')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.3)

            gemini_answer = pyperclip.paste().strip()  # this puts whatever the answer is into your clipboard
            print(f"Gemini replied: {gemini_answer}")

            pyautogui.moveTo(edge_tab_x, edge_tab_y, duration=0.5)
            pyautogui.click()

        except Exception as e:
            print(f"CRASH DETECTED! The code stopped because of this error: {e}")
            gemini_answer = ""

        choice = parse_choice(gemini_answer)
        was_clicked = False

        if choice == "A":
            was_clicked = True
            print("Clicking Option A")
            pyautogui.moveTo(button_a_x, button_a_y, duration=0.5)
            pyautogui.click()
        elif choice == "B":
            was_clicked = True
            print("Clicking Option B")
            pyautogui.moveTo(button_b_x, button_b_y, duration=0.5)
            pyautogui.click()
        elif choice == "C":
            was_clicked = True
            print("Clicking Option C")
            pyautogui.moveTo(button_c_x, button_c_y, duration=0.5)
            pyautogui.click()
        elif choice == "D":
            was_clicked = True
            print("Clicking Option D")
            pyautogui.moveTo(button_d_x, button_d_y, duration=0.5)
            pyautogui.click()
        elif gemini_answer:
            print("Gemini answer is text, not a single choice letter.")

        if not was_clicked:
            print("⚠️ SAFETY TRIGGERED: No option buttons were clicked. Launching test1.py and stopping this script.")
            sys.exit()

if __name__ == "__main__": # only run if it being called by main
    run_main_bot()