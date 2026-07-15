import pyautogui
import pyperclip
import time
import random
import sys
print('Running scan2: ')
time.sleep(2)

start_copy_x = 981
start_copy_y = 488
end_copy_x = 1626
end_copy_y = 998

switch_tab_x = 1099
switch_tab_y = 31

target_box_x = 1291
target_box_y = 1070


gemini_response_x = 1008
gemini_response_y = 451

edge_tab_x = 1567
edge_tab_y = 44


done_button_x = 1877
done_button_y = 1048

next_button_x = 1694
next_button_y = 996

def parse_choice(answer):
    normalized = answer.strip().upper()
    if not normalized:
        return None
    if normalized in {"A", "B", "C", "D", "[A]", "[B]", "[C]", "[D]"}:
        return normalized[1] if normalized.startswith("[") else normalized[0]
    if len(normalized) == 2 and normalized[0] in "ABCD" and normalized[1] in ".):-":
        return normalized[0]
    return None

while True:# this is my loop
 button_a_x = random.randint(1543, 1755)#x vaulues random.randint choses and random vaule with in a box
 button_a_y = random.randint(579, 613) #y vaules
 
 

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
 if choice == "A":
    print("Clicking Option A")
    pyautogui.moveTo(button_a_x, button_a_y, duration=0.5)
    pyautogui.click()
 elif choice == "B":
    print("Clicking Option B")
    pyautogui.moveTo(button_a_x, button_a_y, duration=0.5)
    pyautogui.click()
    pyautogui.press('pgdn', presses=1, interval=0.2)
    
 elif choice == "C":
    print("Clicking Option C")
    pyautogui.moveTo(button_a_x, button_a_y, duration=0.5)
    pyautogui.click()
    pyautogui.press('pgdn', presses=2, interval=0.2)
   
    print("Clicking Option D")
    pyautogui.moveTo(button_a_x, button_a_y, duration=0.5)
    pyautogui.click()
    pyautogui.press('pgdn', presses=3, interval=0.2)
 elif gemini_answer:
   print("Gemini answer is text, not a single choice letter.")
    
 pyautogui.moveTo(next_button_x, next_button_y, duration=0.5)
 pyautogui.click()

   
    



