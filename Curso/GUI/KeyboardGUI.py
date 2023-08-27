#! /usr/bin/env python3
import pyautogui

pyautogui.click(1200,300);pyautogui.typewrite('Hello world!',interval=.08) #semicolon lets you send two functions in a row. Click directs to the window with text edit and ypewrite writes the message
pyautogui.click(1200,300);pyautogui.typewrite(['a','b','left','left','X','Y'],interval=.08) #You can send lists with specific keys
pyautogui.KEYBOARD_KEYS #This puts on the terminal the list of Keyboard keys
pyautogui.press('f1')
pyautogui.hotkey('command','o')