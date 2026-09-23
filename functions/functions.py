import time
import threading
import pyautogui
from pynput import keyboard

pyautogui.PAUSE = 0

running = False
cps = 10
hotKey = keyboard.Key.f6
selectingHotkey = False
hotkeyCallback = None


def setCps(newCps):
    global cps
    cps = newCps


def autoClick():
    
    global running, cps
    
    delay = 1 / cps
    
    while running:
        pyautogui.click()
        time.sleep(delay)
        
def toggleAutoClick():
    global running
   
    
    if running:
        running = False
        print("Stopped")
    else:
        running = True
        print(f"Started at {cps} CPS")

        thread = threading.Thread(
            target=autoClick,
            daemon=True
        )
        thread.start()
        
def setHotKey(key):
    global hotKey
    hotKey = key
    
def startHotKeySelection(callback=None):
    global selectingHotkey, hotkeyCallback
    
    selectingHotkey = True
    hotkeyCallback = callback

def onPress(key):
    global selectingHotkey

    if selectingHotkey:
        setHotKey(key)
        selectingHotkey = False

        if hotkeyCallback:
            hotkeyCallback(key)
        return



    if key == hotKey:
        toggleAutoClick()


listener = keyboard.Listener(on_press=onPress)
listener.start()