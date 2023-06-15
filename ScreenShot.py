# pythom3 -m pip install pyautogui
# py -m pip install pyautogui

import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def takeScreenshot():
    myscreensot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreensot.save(save_path+"_screenshot.png")

myButton = tk.Button(text = "Capture ScreenShot", command = takeScreenshot, font = 10)
canvas1.create_window(150, 150, window = myButton)

tk.mainloop()