import tkinter as tk
from pynput import keyboard
from functions.functions import (
    toggleAutoClick,
    setCps,
    startHotKeySelection,
    getHotKey,
    setStatsCallback,
    setActivationMode,
)

def createWindow():

    window = tk.Tk()
    window.title("Auto Clicker")
    window.geometry("300x500")
    window.configure(bg="#161616")

    cpsValue = tk.IntVar(value=10)
    activationMode = tk.StringVar(value="toggle")

    def updateCPS(*args):
        setCps(cpsValue.get())

    def selectHotKey():
        hotKeyButton.config(text="Press a key...")

        def keySelected(key):
            keyName = str(key).replace("Key.", "")

            window.after(
                0,
                lambda: hotKeyButton.config(
                    text=f"Select Hotkey\n(Current: {keyName})"
                ),
            )

        startHotKeySelection(keySelected)

    def updateStats(currentCPS, clicks, running):

        if running:
            color = "#FF7A1A"
            status = "Running"
        else:
            color = "#FFFFFF"
            status = "Stopped"

        window.after(
            0,
            lambda: statusLabel.config(
                text=f"Status: {status}\nCPS: {currentCPS}\nClicks: {clicks:,}",
                fg=color,
            ),
        )

    setStatsCallback(updateStats)

    def formatHotkey(key):
        keyName = str(key).replace("key.", "")
        return keyName.upper()
    
    title = tk.Label(
        window,
        text="AUTO CLICKER",
        font=("Segoe UI", 20, "bold"),
        fg="#FF7A1A",
        bg="#161616",
    )
    title.pack(pady=(20,10))




    cpsLabel = tk.Label(
        window,
        text="Clicks Per Second",
        font=("Segoe UI", 12),
        bg="#161616",
        fg="#F2F2F2",
    )
    cpsLabel.pack(pady=5, padx=5, ipady=10)
    


    desiredCPS = tk.Spinbox(
        window,
        from_=1,
        to=100000000000,
        textvariable=cpsValue,
        width=20,
        font=("Segoe UI", 12),
        bg="#252525",
        fg="#FF7A1A",
        borderwidth=0,
        bd=0,
        relief="flat",
        highlightthickness=1,
        highlightcolor="#FF7A1A",
        highlightbackground="#3A3A3A",
        insertbackground="#F2F2F2",
        buttonbackground="#252525",
    )
    desiredCPS.pack(ipady=10)

    cpsValue.trace_add("write", updateCPS)

    hotKeyLabel = tk.Label(
        window,
        text="Select Hotkey",
        font=("Segoe UI", 12),
        bg="#161616",
        fg="#F2F2F2",
    )
    hotKeyLabel.pack(pady=5, padx=5, ipady=10)

    currentHotKey = formatHotkey(getHotKey())

    hotKeyButton = tk.Button(
        window,
        text=f"Select Hotkey\n(Current: {currentHotKey})",
        command=lambda: selectHotKey(),
        font=("Segoe UI", 12),
        bg="#252525",
        fg="#FF7A1A",
        borderwidth=0,
        width=18,
    )
    hotKeyButton.pack(ipady=10)

    buttonsFrame = tk.Frame(window, bg="#161616")
    buttonsFrame.pack(
        pady=10,
        padx=5,
    )

    toggleButton = tk.Radiobutton(
        buttonsFrame,
        indicatoron=False,
        text="Toggle",
        variable=activationMode,
        value="toggle",
        command=lambda: setActivationMode("toggle"),
        bg="#252525",
        fg="#FFFFFF",
        selectcolor="#FF7A1A",
        activebackground="#303030",
        activeforeground="#FFFFFF",
        font=("Segoe UI", 12),
        borderwidth=0,
        width=9,
    )

    toggleButton.grid(row=0, column=0, padx=2)

    holdButton = tk.Radiobutton(
        buttonsFrame,
        indicatoron=False,
        text="Hold",
        variable=activationMode,
        value="hold",
        command=lambda: setActivationMode("hold"),
        bg="#252525",
        fg="#FFFFFF",
        selectcolor="#FF7A1A",
        activebackground="#303030",
        activeforeground="#FFFFFF",
        font=("Segoe UI", 12),
        borderwidth=0,
        width=9,
    )

    holdButton.grid(row=0, column=1, padx=2)

    statusLabel = tk.Label(
        window,
        text="Status: Stopped\nCPS: 10\nClicks: 0",
        font=("Segoe UI", 12),
        bg="#161616",
        fg="#ffffff",
    )
    statusLabel.pack(side="bottom", pady=20)

    return window
