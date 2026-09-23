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
    window.geometry("300x450")
    window.configure(bg="#202020")

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
            color = "#F85B00"
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

    cpsLabel = tk.Label(
        window,
        text="input desired \n Clicks Per Second",
        font=("Consolas", 12, "bold"),
        bg="#202020",
        fg="#F85B00",
    )
    cpsLabel.pack(pady=5, padx=5, ipady=10)

    desiredCPS = tk.Spinbox(
        window,
        from_=1,
        to=100000000000,
        textvariable=cpsValue,
        width=20,
        font=("Consolas", 12, "bold"),
        bg="#3D3D3D",
        fg="#F85B00",
        borderwidth=0,
    )
    desiredCPS.pack(ipady=10)

    cpsValue.trace_add("write", updateCPS)

    hotKeyLabel = tk.Label(
        window,
        text="Select Hotkey \n(Default: F6)",
        font=("Consolas", 12, "bold"),
        bg="#202020",
        fg="#F85B00",
    )
    hotKeyLabel.pack(pady=5, padx=5, ipady=10)

    currentHotKey = formatHotkey(getHotKey())

    hotKeyButton = tk.Button(
        window,
        text=f"Select Hotkey\n(Current: {currentHotKey})",
        command=lambda: selectHotKey(),
        font=("Consolas", 12, "bold"),
        bg="#3D3D3D",
        fg="#F85B00",
        borderwidth=0,
    )
    hotKeyButton.pack(ipady=10)

    buttonsFrame = tk.Frame(window, bg="#202020")
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
        bg="#3D3D3D",
        fg="#202020",
        selectcolor="#F85B00",
        activebackground="#202020",
        activeforeground="#202020",
        font=("Consolas", 12),
        borderwidth=0,
        width=10,
    )

    toggleButton.grid(row=0, column=0, padx=2)

    holdButton = tk.Radiobutton(
        buttonsFrame,
        indicatoron=False,
        text="Hold",
        variable=activationMode,
        value="hold",
        command=lambda: setActivationMode("hold"),
        bg="#3D3D3D",
        fg="#202020",
        selectcolor="#F85B00",
        activebackground="#202020",
        activeforeground="#202020",
        font=("Consolas", 12),
        borderwidth=0,
        width=10,
    )

    holdButton.grid(row=0, column=1, padx=2)

    statusLabel = tk.Label(
        window,
        text="Status: Stopped\nCPS: 10\nClicks: 0",
        font=("Consolas", 12, "bold"),
        bg="#202020",
        fg="#ffffff",
    )
    statusLabel.pack(side="bottom", pady=20)

    return window
