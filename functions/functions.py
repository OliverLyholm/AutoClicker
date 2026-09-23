import time
import threading
import pyautogui
from pynput import keyboard
import json
import os

pyautogui.PAUSE = 0

running = False
cps = 10

activationMode = "toggle"


selectingHotkey = False


SETTINGS_DIR = os.path.join(
    os.environ["LOCALAPPDATA"],
    "AutoClicker"
)

os.makedirs(SETTINGS_DIR, exist_ok=True)


HOTKEY_FILE = os.path.join(
    SETTINGS_DIR,
    "clickerSettings.json"
)



clickCount = 0

#callbacks
hotkeyCallback = None
statsCallback = None



def setCps(newCps):
    global cps
    cps = newCps



def autoClick():
    
    global running, cps, clickCount
    
    delay = 1 / cps
    
    while running:
        pyautogui.click()
        
        clickCount += 1
        
        if statsCallback:
            statsCallback(cps, clickCount, running)
        
        time.sleep(delay)
        
def toggleAutoClick():
    global running, clickCount
   
    
    if running:
        running = False

        
        if statsCallback:
            statsCallback(cps, clickCount, running)
        
    else:
        running = True
        clickCount = 0
        

        
        if statsCallback:
            statsCallback(cps, clickCount, running)

        thread = threading.Thread(
            target=autoClick,
            daemon=True
        )
        thread.start()
        
def setHotKey(key):
    global hotKey

    hotKey = key
    saveHotKey(key)

    
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
        
        if activationMode == "toggle":
            toggleAutoClick()
        elif activationMode == "hold":
            if not running:
                toggleAutoClick()




    
def saveHotKey(key):
    if isinstance(key, keyboard.Key):
        keyName = key.name
        keyType = "special"
    else:
        keyName = key.char
        keyType = "char"
    with open(HOTKEY_FILE, "w") as file:
        json.dump({
            "type": keyType,
            "key": keyName
        }, file)

def loadHotkey():
    if not os.path.exists(HOTKEY_FILE):
        return keyboard.Key.f6
    
    with open(HOTKEY_FILE, "r") as file:
        data = json.load(file)
        
    if data["type"] == "special":
        return keyboard.Key[data["key"]]
    
    return keyboard.KeyCode.from_char(data["key"])

hotKey = loadHotkey()

def getHotKey():
    return hotKey

def setStatsCallback(callback):
    global statsCallback
    statsCallback = callback

def setActivationMode(mode):
    global activationMode
    activationMode = mode
    
def onRelease(key):
    if key == hotKey:
        
        if activationMode == "hold":
            if running:
                toggleAutoClick()
                
listener = keyboard.Listener(on_press=onPress, on_release=onRelease)
listener.start()