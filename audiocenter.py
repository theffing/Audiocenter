import tkinter as tk
from tkinter import PhotoImage
import vlc

# binded to 'entry'
def get_song():
    songPath = entry.get()
    # shave "" off
    song = songPath[1:-1] 
    print(song)
    player = vlc.MediaPlayer(song)
    player.play()

# Create window and configure background color
window = tk.Tk()
window.configure(bg="#272727")

# Just a label above the file path entry
label = tk.Label(
    text="Retrieve your mp3.",
    bg="#272727",
    fg="white"
)
label.pack()

# Create entry for user song path
entry = tk.Entry(fg="black", bg="white", width=75)
entry.pack()

# button binded to get_song above which plays the mp3 file with vlc
button = tk.Button(window, text="play song", command=get_song)
button.pack()

image = PhotoImage(file="TH_Axial.png")
image_label = tk.Label(window, image=image)
image_label.pack()

# bind button to function
window.bind("<Return>", lambda event: get_song())

window.mainloop()