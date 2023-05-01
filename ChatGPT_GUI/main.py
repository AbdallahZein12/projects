import tkinter as tk    
from tkinter import messagebox,ttk  
import os
from PIL import Image,ImageTk
import pygame
import json
import bcrypt
import base64
import win32api
import win32con
from chatgpt.global_variables import global_music_box
from chatgpt.run import default_login as run
            

class main:
    def __init__(self):
        self.root = tk.Tk()
        self.width, self.height = 700, 600
        self.x = (self.root.winfo_screenwidth() - self.width) //2 
        self.y = (self.root.winfo_screenheight() - self.height ) //2
        self.root.title("ChatGPT")
        self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.root.maxsize(self.width,self.height)
        self.root.minsize(self.width,self.height)
        self.canvas = tk.Canvas(self.root,width=self.width,height=self.height)
        self.canvas.pack()
        self.media_directory = os.path.join("chatgpt","static")
        self.icon = os.path.join(self.media_directory,"icon.ico")
        self.root.iconbitmap(self.icon)
        self.bg_image = os.path.join(self.media_directory,"bg.jpg")
        self.opened_bg_image = Image.open(self.bg_image)
        self.resized_bg_image = self.opened_bg_image.resize((self.width,self.height),Image.LANCZOS)
        self.tk_bg_image = ImageTk.PhotoImage(self.resized_bg_image)
        self.canvas.create_image(0,0,anchor='nw',image=self.tk_bg_image)
        self.logo_directory = os.path.join(self.media_directory,"logo.gif")
        self.logo_image_opened = Image.open(self.logo_directory)
        self.frames = []
        for i in range(self.logo_image_opened.n_frames):
            self.logo_image_opened.seek(i)
            self.frame = self.logo_image_opened.copy()
            self.frames.append(ImageTk.PhotoImage(self.frame))
        self.logo_label = tk.Label(self.root)
        self.logo_label.place(relx=0.5,rely=0.07,anchor='center')
        self.logo_label.config(image=self.frames[0])
        
        def animate_gif(frame_idx):
            self.logo_label.config(image=self.frames[frame_idx])
            self.root.after(10,animate_gif,(frame_idx+1)%len(self.frames))
        animate_gif(0)
        
        self.canvas.create_text(350,150,text="                    Welcome to ChatGPT\n\n Login with your OpenAI account to continue",font=("Bauhaus 93",18),fill="White")
        self.email_entry = tk.Entry(self.root,width=80)
       
        self.email_entry.insert(0,"Email")
        def on_email_entry_click(event):
            if self.email_entry.get() == "Email":
                self.email_entry.delete(0,tk.END)
        self.email_entry.bind('<FocusIn>',on_email_entry_click)
        self.email_entry.place(relx=0.5,rely=0.4,anchor='center')
        
        self.password_entry = tk.Entry(self.root,width=80,show="*")
        self.password_entry.insert(0,"Password")
        
        def on_password_entry_click(event):
            if self.password_entry.get() == "Password":
                self.password_entry.delete(0,tk.END)
        self.password_entry.bind('<FocusIn>',on_password_entry_click)
        self.password_entry.place(relx=0.5,rely=0.5,anchor='center')
        
        def get_creds():
            try:
                os.chdir("credentials")
                with open("credentials.json",'r') as f:
                    creds = json.load(f)
                    email = creds["email"]
                    hashed_password = creds['password']
                    decoded_password = hashed_password.encode('utf-8')
                    decoded_password = base64.b64decode(decoded_password)
                    decoded_password = decoded_password.decode("utf-8")
                    os.chdir("..")
                    return email,decoded_password
            except FileNotFoundError:
                print("Creds file not found")
                pass
        try:
            retreived_email, retreived_password = get_creds()
            self.email_entry.delete(0,tk.END)
            self.password_entry.delete(0,tk.END)
            self.email_entry.insert(0,retreived_email)
            self.password_entry.insert(0,retreived_password)
        except Exception as e:
            print(e)
        
    
        
        self.login_button = tk.Button(self.root,text="Login",width=20,background="Magenta",font=("Bauhaus 93",18),command=self.default_login)
        self.login_button.place(relx=0.5,rely=0.6,anchor='center')
        
        self.show_password_var = tk.IntVar(value=0)
        self.show_password_button = tk.Checkbutton(self.root,text="Show Pass",background="magenta",font=("Bauhaus 93",10),variable=self.show_password_var,command=self.check_password_show) 
        self.show_password_button.place(relx=0.8,rely=0.6,anchor='center')
        
        
        self.sign_up_button = tk.Button(self.root,text="SignUp",width=10,background="Magenta",font=("Bauhaus 93",12))
        self.sign_up_button.place(relx=0.5,rely=0.7,anchor='center')
        
        self.continute_with_google = tk.Button(self.root,text="Continue with\nGoogle",width=15,height=5,background="Magenta",font=("Bauhaus 93",9))
        self.continute_with_google.place(relx=0.2,rely=0.8,anchor='center')
        
        self.continute_with_microsoft = tk.Button(self.root,text="Continue with\nMicrosoft",width=15,height=5,background="Magenta",font=("Bauhaus 93",9))
        self.continute_with_microsoft.place(relx=0.8,rely=0.8,anchor='center')
        self.music_checker = global_music_box(self.root)
        
        self.remember_me_variable = tk.IntVar(value=1)
        
        
        self.remember_me = tk.Checkbutton(self.root,text="Remember me",font=("Bauhaus 93",8),background="magenta",variable=self.remember_me_variable)
        self.remember_me.place(relx=0.5,rely=0.8,anchor='center')
        
        self.root.mainloop()
        
    def check_password_show(self):
        if self.show_password_var.get() ==1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
        
    def default_login(self):
        if self.email_entry.get() == "Email" or self.email_entry.get() == "":
            email_error = self.canvas.create_text(180,260,text="Please enter your email!",font=("Bauhaus 93",10),fill='red')
            pass
        if self.password_entry.get() == "Password" or self.email_entry.get() == "":
            password_error = self.canvas.create_text(190,320,text="Please enter your password!",font=("Bauhaus 93",10),fill="red")
            pass
        
        password = self.password_entry.get()
        email = self.email_entry.get()
        
        if self.remember_me_variable.get() == 1:
            password_bytes = password.encode('utf-8')
            password_base64 = base64.b64encode(password_bytes)
            password_base64_str = password_base64.decode("utf-8")
            creds = {"email":email,"password":password_base64_str}
            if os.path.exists("credentials"):
                os.chdir("credentials")
                with open("credentials.json",'w') as f:
                    json.dump(creds,f)
                os.chdir("..")
                win32api.SetFileAttributes("credentials",win32con.FILE_ATTRIBUTE_HIDDEN)
            else:
                os.mkdir("credentials")
                os.chdir("credentials")
                with open("credentials.json",'w') as f:
                    json.dump(creds,f)
                os.chdir("..")
                win32api.SetFileAttributes("credentials",win32con.FILE_ATTRIBUTE_HIDDEN)
                
            default_login = run(email=self.email_entry.get(),password=self.password_entry.get())
            print(default_login)
            
                
        
            
        
        
        
        
            
            

        
        
        

main()
