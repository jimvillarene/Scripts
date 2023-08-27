#! /usr/bin/env python3
import pyautogui, PIL,os,pyscreeze
__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

dir_path = os.path.dirname(os.path.realpath(__file__))
imgPath=os.path.join(dir_path,'Img.PNG')
pyautogui.screenshot(imgPath)
btnPath=os.path.join(dir_path,'RunBtn.PNG')

print(pyautogui.locateOnScreen(btnPath)) #You pass an image and Python will tell you the position x,y and w&h of the item

position=pyautogui.locateCenterOnScreen(btnPath)#Same but puts the location on the center of the image to pass
positionList=list(position)
j=0
for i in positionList: 
    print(i)
    positionList[j]=int(i)/2
    j+=1
print(positionList)
pyautogui.moveTo(positionList,duration=2)
pyautogui.click()