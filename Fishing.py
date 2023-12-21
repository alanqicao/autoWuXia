import pyautogui
import time

time.sleep(2)
size = pyautogui.size()
print(size)

mouse_pos = pyautogui.position()
print(mouse_pos)
# pyautogui.alert("This is alert")
pyautogui.useImageNotFoundException()

try:
    location = pyautogui.locateOnScreen('hulu.png', confidence=0.8)
    print('image found')
    print(location)
    centerLocation = pyautogui.center(location)
    pyautogui.moveTo(centerLocation)
    pyautogui.click()
except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')