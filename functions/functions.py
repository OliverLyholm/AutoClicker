import time
import threading
import pyautogui
from pynput import keyboard

pyautogui.PAUSE = 0

running = False
cps = 10


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

def onPress(key):
    if key == keyboard.Key.f6:
        toggleAutoClick()

listener = keyboard.Listener(on_press=onPress)
listener.start()