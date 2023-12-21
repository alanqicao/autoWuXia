import pyautogui
import time


time.sleep(2)
size = pyautogui.size()
print(size)

mouse_pos = pyautogui.position()
print(mouse_pos)

res = pyautogui.locateCenterOnScreen("google2.png")
print(res)