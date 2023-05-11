import tkinter as tk
import os
import pygame
from PIL import Image, ImageTk

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
        
class loading_screen:
    def __init__(self,root):
        self.root = root
        self.media_directory = os.path.join("chatgpt","static")
        self.loading_gif = os.path.join(self.media_directory,"loading.gif")
        self.opened_loading_gif = Image.open(self.loading_gif)
        self.frames = []
        for i in range(self.opened_loading_gif.n_frames):
            self.opened_loading_gif.seek(i)
            frame = self.opened_loading_gif.copy()
            self.frames.append(ImageTk.PhotoImage(frame))
            
        self.loading_label = tk.Label(self.root)
        self.loading_label.place(relx=0.5,rely=0.5,anchor='center')
        self.loading_label.config(image=self.frames[0])
        
        def animate_gif(frame_idx):
            self.loading_label.config(image=self.frames[frame_idx])
            self.root.after(50,animate_gif,(frame_idx+1)%len(self.frames))
        animate_gif(0)
        
    def close(self):
        self.loading_label.destroy()
        


        
        
        
            