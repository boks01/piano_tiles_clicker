from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)  
    time.sleep(0.008)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


num = 0
while keyboard.is_pressed('q') == False:
    if num == 500:
        break
    num += 1
    if pyautogui.pixel(575,538)[0] == 0:
        click(575,538)
    if pyautogui.pixel(508,536)[0] == 0:
        click(508,536)
    if pyautogui.pixel(431,535)[0] == 0:
        click(431,535)
    if pyautogui.pixel(345,531)[0] == 0:
        click(345,531)
    print(num)