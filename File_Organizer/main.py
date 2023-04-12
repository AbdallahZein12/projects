import os, shutil
import tkinter as tk
from PIL import Image,ImageTk
import pygame
import pygifsicle
from tkinter import messagebox
import datetime

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', ".svg"]
audio_extensions = ['.mp3', '.wav', '.aiff', '.aac', '.ogg', '.wma', '.flac']
video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.mpeg']
document_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', 
                       '.rtf', '.csv','.dotx','.docm','.dotm','.dot','.pub','.accdb','.mdb','.accde',
                       '.ade','.adp','.accdr','.mde','.mpp','.mpt','.vsdx','.vssx','.vstx','.vdw',
                       '.vdx','.vsd','.vss','.vst','.pst','.msg','.ost','.oft']
archive_extensions = ['.zip','.rar','.tar.gz','.7z','.bz2']
program_extensions = ['.exe', '.dll', '.jar', '.py', '.java', '.cpp', '.c', '.html', '.css', '.js', '.php']
font_extensions = ['.ttf', '.otf', '.woff', '.woff2']
data_extensions = ['.xml', '.json', '.sql', '.dat', '.log', '.ini', '.cfg']




class Main:
    def __init__(self):
        self.root = tk.Tk()
        
        self.width = 500
        self.height = 400
        
        self.x = (self.root.winfo_screenwidth()- self.width) // 2
        self.y = (self.root.winfo_screenheight()- self.height) // 2
        self.root.minsize(self.width, self.height)
        self.root.maxsize(self.width, self.height)
        
        self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.root.title("FileOrganizer")
        
        self.background_image_directory = os.path.join("Media","bg.jpg")
        self.bgimage= Image.open(self.background_image_directory)
    
        
        self.resized_image = self.bgimage.resize((self.width,self.height),Image.LANCZOS)
        
        self.canvas = tk.Canvas(self.root,width=self.width,height=self.height)
        self.canvas.pack()
        
        self.image_tk = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(0,0,anchor='nw',image=self.image_tk)
        
       
        
        self.logo_directory = os.path.join("Media","logo.gif")
        
        self.logo_image = Image.open(self.logo_directory)
        
        
        self.logo_image_resized = self.logo_image
        
        
        
        self.frames = []
        
        for i in range(self.logo_image_resized.n_frames):
            self.logo_image_resized.seek(i)
            self.frame = self.logo_image_resized.copy()
            self.frames.append(ImageTk.PhotoImage(self.frame))
            
        self.logo_label = tk.Label(self.root)
        self.logo_label.place(relx=0.5,rely=0.07,anchor='center')
        self.logo_label.config(image=self.frames[0])
        
        def animate_gif(frame_idx):
            self.logo_label.config(image=self.frames[frame_idx])
            self.root.after(10,animate_gif,(frame_idx+1)%len(self.frames))
            
        animate_gif(0)
        
    
        
        self.canvas.create_text(250, 150, text="Select Target", font=("Arial", 20), fill="cyan")
        
        self.text = tk.Text(self.root,height=3,width=60,bg='cyan')
        self.text.place(relx=0.5,rely=0.5,anchor='center')
        
        self.button = tk.Button(self.root,text="Launch",font=("impact",25),bg='cyan',command=self.organize_files)
        self.button.place(relx=0.5,rely=0.7,anchor='center')
        
        self.check_state = tk.IntVar(value=0)
        self.check = tk.Checkbutton(self.root,text="Play sound",font=("impact",12),variable=self.check_state,bg='cyan',command=self.check_music)
        self.check.place(relx=0.5,rely=0.9,anchor='center')
        self.root.mainloop()
        
    def check_music(self):
        if self.check_state.get() == 1:
            sound = os.path.join('Media','bgmusic.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()
            pass
        
        
        
        
     
    def organize_files(self):
        list_of_directories = set()
        lines = self.text.get('1.0','end-1c').splitlines()
        for line in lines:
            list_of_directories.add(line)
            
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d__%H-%M-%S")
            
        image_folder = "Images  {}".format(current_time)
        video_folder = "Videos  {}".format(current_time)
        audio_folder = "Audio  {}".format(current_time)
        document_folder = "Documents  {}".format(current_time)
        archive_folder = "Archives  {}".format(current_time)
        program_folder = "Programs  {}".format(current_time)
        fonts_folder = "Fonts  {}".format(current_time)
        data_folder = "Data  {}".format(current_time)
            
        for directory in list_of_directories:
            try:
                os.chdir(directory)
                current_dir = os.getcwd()
                files = os.listdir(directory)
                # print(files)
                for file in files:
                    file_extension = os.path.splitext(file)
                   
                    if file_extension[1] in image_extensions:
                        if os.path.exists(image_folder):
                            shutil.move(file,image_folder)
                        else:
                            os.mkdir(image_folder)
                            shutil.move(file,image_folder)
                    elif file_extension[1] in video_extensions:
                        if os.path.exists(video_folder):
                            shutil.move(file,video_folder)
                        else:
                            os.mkdir(video_folder)
                            shutil.move(file,video_folder)
                    elif file_extension[1] in audio_extensions:
                        if os.path.exists(audio_folder):
                            shutil.move(file,audio_folder)
                        else:
                            os.mkdir(audio_folder)
                            shutil.move(file,audio_folder)
                    elif file_extension[1] in document_extensions:
                        if os.path.exists(document_folder):
                            shutil.move(file,document_folder)
                        else:
                            os.mkdir(document_folder)
                            shutil.move(file,document_folder)
                    elif file_extension[1] in archive_extensions:
                        if os.path.exists(archive_folder):
                            shutil.move(file,archive_folder)
                        else:
                            os.mkdir(archive_folder)
                            shutil.move(file,archive_folder)
                    elif file_extension[1] in program_extensions:
                        if os.path.exists(program_folder):
                            shutil.move(file,program_folder)
                        else:
                            os.mkdir(program_folder)
                            shutil.move(file,program_folder)
                    elif file_extension[1] in font_extensions:
                        if os.path.exists(fonts_folder):
                            shutil.move(file,fonts_folder)
                        else:
                            os.mkdir(fonts_folder)
                            shutil.move(file,fonts_folder)
                    elif file_extension[1] in data_extensions:
                        if os.path.exists(data_folder):
                            shutil.move(file,data_folder)
                        else:
                            os.mkdir(data_folder)
                            shutil.move(file,data_folder)
                    else:
                        pass
                
            except Exception as er:
                messagebox.showinfo(title="Error!",message=f"Error occured in instance {directory}.\n\nCode: {er}")
        messagebox.showinfo(title="Complete!", message="All processes are done.")   

Main()
    



        # self.frames = self.logo_image.n_frames
        # # print(self.frames)
        # self.im = [tk.PhotoImage(file=self.logo_image,format=f'gif -index {i}') for i in range(self.frames)]
        
        # self.count = 0
        # def animation():
        #     im2 = self.im[self.count]
        #     self.logo_label.config(image=im2)
            
        #     self.count += 1
        #     if self.count == self.frames:
        #         count = 0 
                
        #     self.root.after(50,animation(count))
            
        # self.logo_label = tk.Label(image="")
        # self.logo_label.pack()
        
        
        # # self.resized_logo = self.logo_image.resize((int(self.logo_image.width*0.2),int(self.logo_image.height*0.2)),Image.LANCZOS)
        
        # self.frames = []
        
        # for i in range(self.logo_image.n_frames):
        #     self.logo_image.seek(i)
        #     frame = self.logo_image.copy()
        #     self.frames.append(ImageTk.PhotoImage(frame))
        # # print(self.frames)
        # self.logo_label = tk.Label(self.root)
        # self.logo_label.place(relx=0.5,rely=0.5,anchor='center')
        
        # def animage_gif(frame_idx):
        #     self.logo_label.config(image=self.frames[frame_idx])
        #     self.root.update()
        #     self.root.after(100,animage_gif,(frame_idx+1)%len(self.frames))
        # animage_gif(0)
        
        
        # self.root.wm_attributes("-transparentcolor", "cyan")
