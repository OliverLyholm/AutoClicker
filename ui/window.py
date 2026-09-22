import tkinter as tk
from functions.functions import toggleAutoClick, setCps

def createWindow():
    
    window = tk.Tk()
    window.title("Auto Clicker")
    window.geometry("300x450")
    
    desiredCPS = tk.Spinbox(
        window,
        from_=1,
        to=100000000000,
        width=20,
        font=("Consolas", 12, "bold"),
        
    )
    desiredCPS.pack(pady=20, padx=20, ipady=10)
    
    def updateCPS():
        setCps(int(desiredCPS.get()))
        window.after(100, updateCPS)
    
    updateCPS()
    
    
    def StartAutoClick():
        cps = int(desiredCPS.get())
        
        print(f"Button CPS: {cps}")
        
        toggleAutoClick(cps)
    
    startButton = tk.Button(
        window,
        text="Start",
        width=10,
        height=2,
        font=("Consolas", 15),
        borderwidth=0,
        relief="flat",
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        
    )
    startButton.pack()
    
    return window