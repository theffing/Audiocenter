import re
import vlc
import time
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import filedialog

# Class Audiocenter
class audiocenter(tk.Tk):

    def __init__(self, root):
        self.player = vlc.MediaPlayer()
        self.root = root
        # Just a label above the file path entry
        self.label = tk.Label(text="",bg="#272727",fg="white")
        self.label.grid(row=0,column=0,pady=2)
        # File Explorer Button
        browse_button = tk.Button(root, text="MP3", command=self.browse_file)
        browse_button.grid(row=0,column=1,padx=1,pady=2)
        # Play Button
        play_button = tk.Button(root, text="Play", command=self.play_song)
        play_button.grid(row=0,column=2,pady=2)
        # Pause Button
        pause_button = tk.Button(root, text="Pause", command=self.pause_song)
        pause_button.grid(row=0,column=3,pady=2)
        # Fast-Forward 10secs
        forward_button = tk.Button(root, text="+10s", command=self.forward)
        forward_button.grid(row=0,column=4,pady=2)
        # Rewind 10secs
        rewind_button = tk.Button(root, text="-10s", command=self.rewind)
        rewind_button.grid(row=0,column=5,pady=2)
        # Mute Button
        mute_button = tk.Button(root, text="Mute",command=self.mute_song)
        mute_button.grid(row=0,column=6,pady=2)
        # Pause/Play Icon
        self.image = PhotoImage(file='pause.png')
        self.image_label = tk.Label(root,bg="#272727",image=self.image)
        self.image_label.grid(row=1,column=0,pady=2)
        # Track time playing and total duration
        self.track_time = tk.Label(text="",bg="#272727",fg="white")
        self.track_time.grid(row=1,column=1,pady=2)

    # ------------------------------------------------------------------

    def browse_file(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")))
        if filename:
            # Do something with the selected file
            # shave off
            global is_playing
            is_playing = False
            self.player.stop()
            filename = re.sub(r"file:///", "", filename)
            print(filename)
            self.player = vlc.MediaPlayer(filename)
            # Get Title of Song
            title = filename.rsplit('/', 1)[1]
            self.label.config(text=title)
            # Grab Length of song
            self.player.play(); self.player.audio_toggle_mute()
            time.sleep(.1)
            length = self.player.get_length() / 1000
            self.min = length // 60
            self.sec = length % 60
            self.track_time.config(text=f"0:00/{int(self.min)}:{int(self.sec)}")
            self.player.pause(); self.player.audio_toggle_mute()
            # Set player icon for first time

    def pause_song(self):
        global is_playing
        self.player.pause()
        self.image = tk.PhotoImage(file='pause.png')
        self.image_label.config(image=self.image)
        is_playing = False

    def play_song(self):
        global start_time, is_playing
        is_playing = True
        self.player.play()
        self.image = tk.PhotoImage(file='play.png')
        self.image_label.config(image=self.image)
        self.track_media_time()

    def forward(self):
        self.player.set_time(self.player.get_time() + 10000)

    def rewind(self):
        self.player.set_time(self.player.get_time() - 10000)

    def mute_song(self):
        self.player.audio_toggle_mute()

    def track_media_time(self):
        global start_time, is_playing
        if is_playing:
            self.length = self.player.get_time() / 1000
            self.el_min = self.length // 60
            self.el_sec = self.length % 60
            if int(self.el_sec) < 10:
                time = (f"{int(self.el_min)}:0{int(self.el_sec)}")
            else:
                time = (f"{int(self.el_min)}:{int(self.el_sec)}")
            self.track_time.config(text=f"{time}/{int(self.min)}:{int(self.sec)}")
            self.root.after(1000, self.track_media_time)  # Update every second

# ------------------------------------------------------------------

def main(): 
    # Create root and configure background color
    root = tk.Tk()
    # Resize root window
    root.geometry("500x100")
    # root Icon
    root.iconbitmap("smiley.ico")
    # root Title
    root.title("AudioCenter")
    # root Background Color
    root.configure(bg="#272727")
    # Instantiate Class and run root Loop
    #image = PhotoImage(file="Spikeball.png")
    app = audiocenter(root)
    # Start updates
    root.mainloop()

if __name__ == "__main__":
    main()