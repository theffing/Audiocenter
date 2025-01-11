import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
import re
import vlc

# binded to 'entry'
def get_song():
    songPath = entry.get()
    # shave "" off
    song = songPath[1:-1] 
    print(song)
    player = vlc.MediaPlayer(song)
    player.play()

def browse_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")))
    if filename:
        # Do something with the selected file
        # shave "" off
        filename = re.sub(r"file:///", "", filename)
        print(filename)
        player = vlc.MediaPlayer(filename)
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

# Brain Picture
image = PhotoImage(file="TH_Axial.png")
image_label = tk.Label(window, image=image)
image_label.pack()


button = tk.Button(window, text="Get Song", command=browse_file)
button.pack()

window.mainloop()