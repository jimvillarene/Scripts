#! /usr/bin/env python3
import pyautogui

width,height=pyautogui.size()
print(width," ",height)
pyautogui.moveTo(70,800,duration=2)
pyautogui.moveRel(100,0,duration=2) #Move relatively to the actual position of the mouse
pyautogui.position() #Shows the actual position of the mouse
pyautogui.click(339,39) #Moves to the absolute position and clicks
pyautogui.doubleClick(339,39) #Also middleClick, leftClick,tripleClick, etc
#pyautogui has a failsafe, if the program gets loop or buggy you can ge the mouse to the upperleft corner and it will stop pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.