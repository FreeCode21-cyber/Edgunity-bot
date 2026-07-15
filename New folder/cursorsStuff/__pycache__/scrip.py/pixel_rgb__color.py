import pyautogui
import time
print('okay')
time.sleep(3)
print("Position your mouse over the target spot. Recording in 3 seconds...")
time.sleep(3)

# Get current mouse position
x, y = pyautogui.position()
# Get the RGB color of that pixel
color = pyautogui.pixel(x, y)

print(f"Target X: {x}, Target Y: {y}")
print(f"Target Color (RGB): {color}")