import tkinter as tk
from functions.functions import toggleAutoClick, setCps, startHotKeySelection
from pynput import keyboard

def createWindow():
    
    window = tk.Tk()
    window.title("Auto Clicker")
    window.geometry("300x450")
    window.configure(bg="#202020")
    
    cpsValue = tk.IntVar(value=10)
    
    def updateCPS(*args):
        setCps(int(desiredCPS.get()))
    
    desiredCPS = tk.Spinbox(
        window,
        from_=1,
        to=100000000000,
        textvariable=cpsValue,
        width=20,
        font=("Consolas", 12, "bold"),
        bg="#3D3D3D",
        fg="#F85B00",
        borderwidth=0
        
    )
    desiredCPS.pack(pady=20, padx=20, ipady=10)
    
    def StartAutoClick():
        cps = int(desiredCPS.get())
        
        print(f"Button CPS: {cps}")
        
        toggleAutoClick(cps)
    
    def selectHotKey():
        hotKeyButton.config(text="Press a key...")
        
        def keySelected(key):
            keyName = str(key).replace("Key.", "")
            
            window.after(
                0,
                lambda: hotKeyButton.config(text=f"Hotkey: {keyName}")
            )
        
        startHotKeySelection(keySelected)
        
    hotKeyButton = tk.Button(
        window,
        text="Select Hotkey",
        command=lambda: selectHotKey(),
        font=("Consolas", 12, "bold"),
        bg="#3D3D3D",
        fg="#F85B00",
        borderwidth=0
    )
    hotKeyButton.pack()
    
    
    return window