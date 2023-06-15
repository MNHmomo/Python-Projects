# python3 -m pip install tk
# py -m pip install tk, customtkinter, pytube

import certifi
import ssl

import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text = ytObject.title, text_color = "white")
        finishLabel.configure(text = "")

        video.download(".")
        finishLabel.configure(text="Downloaded!", text_color = "green")
    except:
        finishLabel.configure(text = "Download Error", text_color = "red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text = per + "%")
    pPercentage.update()

    # Update Progress Bar
    progressBar.set(float(percentage_of_completion) / 100)

# System Settings (light mode or dark mode)
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our Application Frame
app = customtkinter.CTk()
app.geometry("720x480+400+200")
app.title("MACH YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text = "Insert a YouTube Link")
title.pack(padx = 10, pady = 10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack()

# Progress Precentage
pPercentage = customtkinter.CTkLabel(app, text = "0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width = 400)
progressBar.set(0)
progressBar.pack(padx = 10, pady = 10)

# Downlaod Button
download = customtkinter.CTkButton(app, text = "Download", command = startDownload)
download.pack(padx = 10, pady = 10)

# Run Application
app.mainloop()