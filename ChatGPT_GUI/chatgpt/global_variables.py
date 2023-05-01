import tkinter as tk
import os
import pygame

class global_music_box:
    def __init__(self,root):
        self.root = root
        self.check_state = tk.IntVar(value=1)
        self.media_directory = os.path.join("chatgpt","static")
        self.music_check_box = tk.Checkbutton(self.root,text="Play Sound",font=("Bauhaus 93",9),background="Magenta",variable=self.check_state,command=self.check_music)
        self.music_check_box.place(relx=0.5,rely=0.9,anchor='center')
        music = os.path.join(self.media_directory,"bg_music.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(music)
    def check_music(self):
        if self.check_state.get() == 1:
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()
            pass