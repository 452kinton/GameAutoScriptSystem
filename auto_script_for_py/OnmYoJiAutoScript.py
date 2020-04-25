from baseInterface import gameScriptInterface
from utils import bitmapUtils
import time 
import autopy

def startSetting():
    pos = gameScriptInterface.find_pic_position_on_screen("temp/setting.png",0.5)
    print(pos)
    if pos != None:
        gameScriptInterface.mouse_move_to(pos[0],pos[1])
        autopy.mouse.click()
        time.sleep(2)
        for number in range(0,9):
            if number < 5:
                gameScriptInterface.mouse_move_to(2120,566+number*105)
                autopy.mouse.click()
            else :
                startPoint = [2120,566+4*96]
                endPoint =[2120,566+3*96]
                gameScriptInterface.mouse_move_with_pressing(startPoint,endPoint)
                gameScriptInterface.mouse_move_to(startPoint[0],startPoint[1])
                autopy.mouse.click()
            setRunningBtn()
            
        pos = gameScriptInterface.find_pic_position_on_screen("temp/back.png",0.5)
        if pos != None:
            gameScriptInterface.mouse_move_to(pos[0],pos[1])
            autopy.mouse.click()
            time.sleep(2)

def setRunningBtn():
    time.sleep(2)
    pos = gameScriptInterface.find_pic_position_on_screen("temp/run.png",0.5)
    if pos != None:
        gameScriptInterface.mouse_move_to(pos[0],pos[1])
        autopy.mouse.click()
        time.sleep(2)
    pos = gameScriptInterface.find_pic_position_on_screen("temp/setting_back.png",0.5)
    if pos != None:
        gameScriptInterface.mouse_move_to(pos[0],pos[1])
        autopy.mouse.click()
        time.sleep(2)

            
def startScript():
    count = 0 
    while True:
        if count == 0:
            count = 28
            startSetting()
        else :
            count =count-1
            pos = gameScriptInterface.find_pic_position_on_screen("temp/onekey.png",0.5)
            print(pos)
            if pos != None:
                gameScriptInterface.mouse_move_to(pos[0],pos[1])
                autopy.mouse.click()
                time.sleep(2)
                autopy.mouse.click()
        time.sleep(660)

startScript()


