import tkinter as tk
from tkinter import messagebox,ttk
import qrcode 
from PIL import Image,ImageTk
import os
import pygame
import helper
import traceback
from datetime import datetime
import time

class QrShower:
    def __init__(self,QRCODE,width,height):
        self.QRCODE = QRCODE
        self.root1 = tk.Toplevel()
        self.width,self.height = width,height
        self.x = (self.root1.winfo_screenwidth() //2) 
        self.y = (self.root1.winfo_screenheight() //2)
        self.root1.title("QrCode")
        self.root1.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.root1.maxsize(self.width,self.height)
        self.root1.minsize(self.width,self.height)
        self.canvas = tk.Canvas(self.root1,width=self.width,height=self.height)
        self.canvas.pack()
        self.canvas.create_image(0,0,anchor='nw',image=self.QRCODE)
        
        
        self.root1.mainloop()
        


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.width, self.height = 500 , 400
        self.x = (self.root.winfo_screenwidth()- self.width) // 2
        self.y = (self.root.winfo_screenheight() - self.height) // 2
        self.root.maxsize(self.width,self.height)
        self.root.minsize(self.width,self.height)
        self.root.title("QRCodeGen")
        self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.canvas = tk.Canvas(self.root,width=self.width,height=self.height)
        self.canvas.pack()
        self.background_image_directory = os.path.join("Media","bg.jpg")
        self.bg_image_opened = Image.open(self.background_image_directory)
        self.bg_resized = self.bg_image_opened.resize((self.width,self.height),Image.LANCZOS)
        self.tk_bg = ImageTk.PhotoImage(self.bg_resized)
        self.canvas.create_image(0,0,anchor='nw',image=self.tk_bg)
        self.logo_directory = os.path.join("Media","logo.gif")
        self.logo_image = Image.open(self.logo_directory)
        self.frames = []
        for i in range(self.logo_image.n_frames):
            self.logo_image.seek(i)
            self.frame = self.logo_image.copy()
            self.frames.append(ImageTk.PhotoImage(self.frame))
        
        self.logo_label = tk.Label(self.root)
        self.logo_label.place(relx=0.5,rely=0.07,anchor='center')
        self.logo_label.config(image=self.frames[0])
        
        def animate_gif(frame_idx):
            self.logo_label.config(image=self.frames[frame_idx])
            self.root.after(10,animate_gif,(frame_idx+1)%len(self.frames))
        animate_gif(0)
        
        self.canvas.create_text(250,150,text="Input your URL", font=("impact",22),fill="Silver")
        
        self.input_text = tk.Entry(self.root,width=50,bg='silver',font=("arial"))
        self.input_text.place(relx=0.5,rely=0.5,anchor='center')
        
        self.button = tk.Button(self.root,text="Generate",font=("impact",25),bg="silver",command=self.convert_to_QR)
        self.button.place(relx=0.5,rely=0.7,anchor='center')
        
        self.check_state = tk.IntVar(value=0)
        self.check = tk.Checkbutton(self.root,text="Play sound",font=("impact",12),variable=self.check_state,bg='silver',command=self.music_player)
        self.check.place(relx=0.5,rely=0.9,anchor='center')
        
        self.canvas.create_text(85,250,text="Back Color",font=("impact",12),fill="silver")
        self.canvas.create_text(400,250,text="Fill Color",font=("Impact",12),fill="silver")
        
        self.selected_item = tk.StringVar(value="White")
        
        self.dropdown = ttk.Combobox(self.root,textvariable=self.selected_item,state='readonly')
        self.dropdown['values'] = ('Black',"White","Blue","Red","Green","Cyan","Purple")
        self.dropdown.place(relx=0.19,rely=0.7,anchor='center')
        
        self.selected_item2 = tk.StringVar(value="Black")
        self.dropdown_fill = ttk.Combobox(self.root,textvariable=self.selected_item2,state='readonly')
        self.dropdown_fill['values'] = ('Black',"White","Blue","Red","Green","Cyan","Purple")
        self.dropdown_fill.place(relx=0.80,rely=0.7,anchor='center')
        
        
        def on_select(event):
            pass
            # print(self.selected_item2.get())
            # print(self.selected_item.get())

        self.dropdown_fill.bind("<<ComboboxSelected>>",on_select)
        self.dropdown.bind('<<ComboboxSelected>>', on_select)  
        self.root.mainloop()
        
    def convert_to_QR(self):
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d__%H-%M-%S")
        url = self.input_text.get()
         
        if url == "":
            messagebox.showinfo(title="Error!",message="Please input a url!!")
            pass
        else:
            try:
                qr = qrcode.QRCode(version=None, box_size=10, border=3)
                data = url
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(fill_color=self.selected_item2.get(),back_color=self.selected_item.get())
                if os.path.exists("QRCodes"):
                    os.chdir("QRCodes")
                    img.save(f"{formatted_time}.png")
                    os.chdir("..")
                else:
                    os.mkdir("QRCodes")
                    os.chdir("QRCodes")
                    img.save(f"{formatted_time}.png")
                    os.chdir("..")
                tk_qr = ImageTk.PhotoImage(image=img)
                QrShower(tk_qr,tk_qr.width(),tk_qr.height())
            except:
                helper.logger.error(f"Experienced Error: \n\n{traceback.format_exc()}\n\n")
                
    def music_player(self):
        if self.check_state.get() == 1:
            sound = os.path.join("Media","bgmusic.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()
            pass
        
                
        
        
        
        
        
        


Main()
    