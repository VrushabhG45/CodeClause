import tkinter as tk
from tkinter import filedialog
from pygame import mixer

mixer.init()

def play_music():
    file_path = filedialog.askopenfilename(filetypes=(("Audio Files", "*.mp3"), ("All Files", "*.*")))
    if file_path:
        mixer.music.load(file_path)
        mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def main():
    window = tk.Tk()
    window.title("Python Music Player")

    # Create and configure a frame to hold the buttons
    button_frame = tk.Frame(window, padx=20, pady=10)
    button_frame.pack()

    # Create and configure the Play button
    play_button = tk.Button(button_frame, text="Play", command=play_music)
    play_button.grid(row=0, column=0, padx=5, pady=5)

    # Create and configure the Pause button
    pause_button = tk.Button(button_frame, text="Pause", command=pause_music)
    pause_button.grid(row=0, column=1, padx=5, pady=5)

    # Create and configure the Resume button
    resume_button = tk.Button(button_frame, text="Resume", command=resume_music)
    resume_button.grid(row=0, column=2, padx=5, pady=5)

    # Create and configure the Stop button
    stop_button = tk.Button(button_frame, text="Stop", command=stop_music)
    stop_button.grid(row=0, column=3, padx=5, pady=5)

    window.mainloop()

if __name__ == '__main__':
    main()
