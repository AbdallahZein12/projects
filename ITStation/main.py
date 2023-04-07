import tkinter as tk
from PIL import Image,ImageTk
import pygame
import os, win32net
from tkinter import messagebox
import ast
import win32api,win32con
import shutil
import datetime
import win32netcon
import subprocess




class GlobalCheckbox:
    def __init__(self, master):
        self.master = master
        self.check_state = tk.IntVar(value=1) 
        self.check = tk.Checkbutton(self.master,text="Play sound",font=('impact',12),variable=self.check_state,bg='green',command=self.check_music)
        self.check.place(relx=0.5,rely=0.9,anchor='center')

    def check_music(self):
        if self.check_state.get() == 1:
            sound = os.path.join('media','background_music.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            
        else:
            pygame.mixer.music.stop()
            pass
        
class GlobalMainFrame:
    def __init__(self,master, title):
        self.master = master
        self.background_image = os.path.join("media","background.jpg")
        self.bgimage = Image.open(self.background_image)
        self.canvas = tk.Canvas(self.master,width=self.bgimage.width,height=self.bgimage.height)
        
        self.canvas.pack()
        
        self.bgimage_tk = ImageTk.PhotoImage(self.bgimage)
        self.canvas.create_image(0,0,anchor='nw',image=self.bgimage_tk)
        
        
        self.master.wm_attributes('-alpha',True)
        
        self.geometry = self.master.geometry('800x500')
        self.title = self.master.title("ITStation")

        self.logo = os.path.join('media','logo2.png')
        self.label_image = Image.open(self.logo)
        self.label_image = self.label_image.resize((int(self.label_image.width * 0.5), int(self.label_image.height * 0.5)))
        self.photo = ImageTk.PhotoImage(self.label_image)
        
        self.canvas.create_image(400,250,image=self.photo)
        
        self.main_menu_title = os.path.join('media',title)
        self.top_text = Image.open(self.main_menu_title)
        self.top_text = self.top_text.resize((int(self.top_text.width*0.2),int(self.top_text.height*0.2)))
        self.tk_top_text = ImageTk.PhotoImage(self.top_text)
        self.canvas.create_image(400,50,image=self.tk_top_text)


class StatusReport:
    def __init__(self):
        self.root = tk.Toplevel()
        


class AdobeAdvancedWarfare:
    def __init__(self):
        self.root = tk.Toplevel()
        self.mainframe = GlobalMainFrame(self.root,"ADOBEAW.png")
        
        self.pc_list = []
        
        self.music_check = GlobalCheckbox(self.root)
        
        self.pc_list_text_label = tk.Label(self.root,text="Select Target(s)", font=("Impact",18),bg='green')
        self.pc_list_text_label.place(relx=0.17,rely=0.2,anchor='center')
        
        self.text = tk.Text(self.root,width=20,height=20,wrap="word",bg='green')
        self.text.place(relx=0.17,rely=0.6,anchor='center')
        self.text.bind("<Key>",self.limit_line_length)
        
        self.launcher = tk.Button(self.root,text="Launch",font=("arial",35),bg='green',command=self.install_adobe)
        self.launcher.place(relx=0.8,rely=0.5,anchor='center')
        
        self.root.mainloop()
        
        
    def limit_line_length(self,event):
            
        widget = event.widget
        line,column = widget.index("insert").split('.')
        if len(widget.get(f"{line}.0",f"{line}.end")) > 7:
            widget.insert(f"{line}.{int(column)-1}",'\n')
            
    def install_adobe(self):
        self.pc_list =[]
        for line in self.text.get('1.0','end-1c').splitlines():
            self.pc_list.append(line)
        
        print(self.pc_list)
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d__%H-%M-%S")
        if len(self.pc_list) == 0:
            pass
        else:
            if messagebox.askyesno(title="Install Creative Cloud",message="Are you sure you want to continue?"):
                for pc in self.pc_list:
                    try:
                        remote_host = pc
                        program_path = ##PROGRAM PATH TO CHECK IF IT EXISTS
                        
                        command = f'psexec \\\\{pc} -u {globalusername} -p {globalpassword} cmd /c "if exist {program_path} (echo 1) else (echo 0)"'
                        result = subprocess.check_output(command,shell=True)
                        
                        if result.decode('utf-8') == 1:
                            if messagebox.askyesno(title="All files exist",message=f"It looks like the program already exists on {pc} , continue?"):
                                installation_directory = ##INSTALLATION DIRECTORY OF THE PROGRAM


                                
                                command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                                result = subprocess.check_output(command, shell=True)
                                
                                print(result.decode('utf-8'))
                                
                                if os.path.exists("Reports"):
                                    
                                    reports_directory = os.path.join("Reports",f"ADOBE {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                    
                                else:
                                    os.mkdir("Reports")
                
                                    reports_directory = os.path.join("Reports",f"ADOBE {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                        
                            else:
                                pass
                        else:
                            installation_directory = ##IF PROGRAM DOES NOT EXIST. INSTALL FROM THIS DIRECTORY


                                
                            command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                            result = subprocess.check_output(command, shell=True)
                                
                            print(result.decode('utf-8'))
                                
                            if os.path.exists("Reports"):
                                    
                                reports_directory = os.path.join("Reports",f"ADOBE {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!\n\n")
                                    
                            else:
                                os.mkdir("Reports")
                
                                reports_directory = os.path.join("Reports",f"ADOBE {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!\n\n")
                    except Exception as er:
                        if os.path.exists("Reports"):
                            reports_directory = os.path.join("Reports",f"ADOBE {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                                    
                        else:
                            os.mkdir("Reports")
                
                            reports_directory = os.path.join("Reports",f"ADOBE {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                            
                            
                        messagebox.showinfo(title="Error!",message=f"Experienced errors for target {pc}   check reports folder for more info")
                        
                
                
                
                    
                  
        
        
        
        

class MicrosoftBlackOps:
    def __init__(self):
        self.root = tk.Toplevel()
        self.mainframe = GlobalMainFrame(self.root,"MICROSOFTBO.PNG")
        
        self.pc_list = []
        
        self.music_check = GlobalCheckbox(self.root)
        
        self.pc_list_text_label = tk.Label(self.root,text="Select Target(s)", font=("Impact",18),bg='green')
        self.pc_list_text_label.place(relx=0.17,rely=0.2,anchor='center')
        
        self.text = tk.Text(self.root,width=20,height=20,wrap="word",bg='green') 
        self.text.place(relx=0.17,rely=0.6,anchor='center')
        self.text.bind("<Key>",self.limit_line_length)
        
        
        self.btnframe = tk.Frame(self.root)
        
        self.btnframe.columnconfigure(0,weight=1)
        
        self.btn1 = tk.Button(self.btnframe,text="Microsoft 365",font=('arial',12),width=15,height=3,bg='green',command=self.install_microsoft_365)
        self.btn1.grid(row=0,column=0,sticky=tk.W + tk.E)
        
        self.btn2 = tk.Button(self.btnframe,text="Visio 2013",font=("arial",12),width=15,height=3,bg='green',command=self.install_visio)
        self.btn2.grid(row=1,column=0,sticky=tk.W + tk.E)
        
        self.btn3 = tk.Button(self.btnframe,text="Project Pro 2013",font=('arial',12),width=15,height=3,bg='green',command=self.install_project_pro)
        self.btn3.grid(row=2,column=0,sticky=tk.W +tk.E)
        
        self.btn4 = tk.Button(self.btnframe,text="MS Teams",font=('arial',12),width=15,height=3,bg='green',command=self.install_teams)
        self.btn4.grid(row=3,column=0,sticky=tk.W +tk.E)
        

        self.btnframe.place(relx=0.8,rely=0.5,anchor='center')
        
        self.ms35_list = ["C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE","C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE","C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE","C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE","C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE","C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"]
        
        self.root.mainloop()
        
    def limit_line_length(self,event):
            
        widget = event.widget
        line,column = widget.index("insert").split('.')
        if len(widget.get(f"{line}.0",f"{line}.end")) > 7:
            widget.insert(f"{line}.{int(column)-1}",'\n')
            
    def install_microsoft_365(self):
        self.pc_list = []
        lines = self.text.get('1.0','end-1c').splitlines()
        for line in lines:
            self.pc_list.append(line)
        print(self.pc_list)
            
        if len(self.pc_list) == 0:
            pass
        else:
            if messagebox.askyesno(title="Install Microsoft 365",message="Are you sure you want to continue?"):
                now = datetime.datetime.now()
                formatted_date = now.strftime("%Y-%m-%d__%H-%M-%S")
                all_files_exist = True
                    
                for pc in self.pc_list:
                    try:
                        for location in self.ms35_list:
                            command = f'psexec \\\\{pc} -u {globalusername} -p {globalpassword} cmd /c "if exist {location} (echo 1) else (echo 0)"'
                            result = subprocess.check_output(command,shell=True)
                            
                            if result.decode('utf-8') == 1:
                                print("Exists")
                                continue
                            else:
                                all_files_exist = False
                                continue
                    
                    
                        if all_files_exist == True:
                            if messagebox.askyesno(title="All files exist",message=f"All files seem to exist on target {pc} , continue?"):
                                remote_host = pc
                                program_path = ##PROGRAM INSTALLATION PATH
                                
                                command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{program_path}"'
                                result = subprocess.check_output(command, shell=True)
                                
                                print(result.decode('utf-8'))
                                
                                
                                if os.path.exists("Reports"):
                                    
                                    reports_directory = os.path.join("Reports",f"MS365 {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!\n\n")
                                    
                                else:
                                    os.mkdir("Reports")
                
                                    reports_directory = os.path.join("Reports",f"MS365 {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!\n\n")
                            else:
                                pass
                                        
                        else:
                            remote_host = pc
                            program_path = ##PROGRAM INSTALLATION PATH
                                
                            command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{program_path}"'
                            output = subprocess.check_output(command,shell=True)
                            print(output.decode('utf-8'))
                            
                                
                            if os.path.exists("Reports"):
                                    
                                reports_directory = os.path.join("Reports",f"MS365 {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!\n\n")
                                    
                            else:
                                os.mkdir("Reports")
                
                                reports_directory = os.path.join("Reports",f"MS365 {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!\n\n")
                            
                            
                    except Exception as er:
                        
                        if os.path.exists("Reports"):
                            reports_directory = os.path.join("Reports",f"MS365 {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                                    
                        else:
                            os.mkdir("Reports")
                
                            reports_directory = os.path.join("Reports",f"MS365 {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                            
                            
                        messagebox.showinfo(title="Error!",message=f"Experienced errors for target {pc}   check reports folder for more info")
                        
    def install_visio(self):
        self.pc_list=[]
        lines = self.text.get('1.0','end-1c').splitlines()
        for line in lines:
            self.pc_list.append(line)
        print(self.pc_list)
        
        if len(self.pc_list) == 0:
            pass
        else:
            if messagebox.askyesno(title="Install Microsoft Visio 2013",message="Are you sure you want to continue?"):
                now = datetime.datetime.now()
                formatted_date = now.strftime('%Y-%m-%d__%H-%M-%S')
            
                
                for pc in self.pc_list:
                    try:
                        remote_pc = pc 
                        program_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Visio 2013.lnk"
                        command = f'psexec \\\\{pc} -u {globalusername} -p {globalpassword} cmd /c "if exist {program_path} (echo 1) else (echo 0)"'
                        result = subprocess.check_output(command,shell=True)
                        
                        if result.decode('utf-8') == 1:
                            remote_host = pc
                            if messagebox.askyesno(title="All files exist",message=f"It looks like the program already exists on {pc} , continue?"):
                                installation_directory = ##INSTALLATION DIRECTORY
                                command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                                result = subprocess.check_output(command, shell=True)
                                
                                print(result.decode('utf-8'))  
                                
                                if os.path.exists("Reports"):
                                    
                                    reports_directory = os.path.join("Reports",f"VISIO {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                    
                                else:
                                    os.mkdir("Reports")
                
                                    reports_directory = os.path.join("Reports",f"VISIO {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                        
                            else:
                                pass
                        else:
                            installation_directory = ##INSTALLATION DIRECTORY
                            command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                            result = subprocess.check_output(command, shell=True)
                            
                            print(result.decode('utf-8'))
                            
                            if os.path.exists("Reports"):
                                    
                                reports_directory = os.path.join("Reports",f"VISIO {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!")
                                    
                            else:
                                os.mkdir("Reports")
                
                                reports_directory = os.path.join("Reports",f"VISIO {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!")
                                    
                    except Exception as er:
                        if os.path.exists("Reports"):
                            reports_directory = os.path.join("Reports",f"VISIO {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                                    
                        else:
                            os.mkdir("Reports")
                
                            reports_directory = os.path.join("Reports",f"VISIO {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                                
                        messagebox.showinfo(title="Error!",message=f"Experienced error for target {pc}  check reports folder for more info")
                        
            else: 
                pass
            
            
    def install_project_pro(self):
        self.pc_list =[]
        lines = self.text.get('1.0','end-1c').splitlines()
        for line in lines:
            self.pc_list.append(line)  
        print(self.pc_list)
        now = datetime.datetime.now()
        formatted_date = now.strftime('%Y-%m-%d__%H-%M-%S')
        if len(self.pc_list) == 0:
            pass
        else:
            if messagebox.askyesno(title="Install Project Pro 2013",message="Are you sure you want to continue?"):
                for pc in self.pc_list:
                    try:
                        remote_host = pc
                        program_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Project 2013.lnk"
                        
                        command = f'psexec \\\\{pc} -u {globalusername} -p {globalpassword} cmd /c "if exist {program_path} (echo 1) else (echo 0)"'
                        result = subprocess.check_output(command,shell=True)
                        
                        if result.decode('utf-8') == 1:
                            if messagebox.askyesno(title="All files exist",message=f"It looks like the program already exists on {pc} , continue?"):
                                installation_directory = ##INSTALLATION DIRECTORY
                                
                                command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                                result = subprocess.check_output(command, shell=True)
                                
                                print(result.decode('utf-8'))
                                
                                if os.path.exists("Reports"):
                                    
                                    reports_directory = os.path.join("Reports",f"PROJECTPRO {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                    
                                else:
                                    os.mkdir("Reports")
                
                                    reports_directory = os.path.join("Reports",f"PROJECTPRO {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                
                            else:
                                pass
                        else:
                            installation_directory = ##INSTALLATION DIRECTORY
                                
                            command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                            result = subprocess.check_output(command, shell=True)
                                
                            print(result.decode('utf-8'))
                                
                            if os.path.exists("Reports"):
                                    
                                reports_directory = os.path.join("Reports",f"PROJECTPRO {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!")
                                    
                            else:
                                os.mkdir("Reports")
                
                                reports_directory = os.path.join("Reports",f"PROJECTPRO {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!")
                                    
                    except Exception as er:
                        if os.path.exists("Reports"):
                                    
                            reports_directory = os.path.join("Reports",f"PROJECTPRO {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                            
                                    
                        else:
                            os.mkdir("Reports")
                
                            reports_directory = os.path.join("Reports",f"PROJECTPRO {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                                
                        messagebox.showinfo(title="Error!",message=f"Experienced error for target {pc}  check reports folder for more info")
                        
    def install_teams(self):
        self.pc_list =[]
        lines = self.text.get('1.0','end-1c').splitlines()
        for line in lines:
            self.pc_list.append(line)  
        print(self.pc_list)
        now = datetime.datetime.now()
        formatted_date = now.strftime('%Y-%m-%d__%H-%M-%S')
        if len(self.pc_list) == 0:
            pass
        else:
            if messagebox.askyesno(title="Install MS Teams",message="Are you sure you want to continue?"):
                for pc in self.pc_list:
                    try:
                        remote_host = pc
                        program_path = r"C:\Users\AAbdelmoneim\AppData\Local\Microsoft\Teams\Update.exe"
                        
                        command = f'psexec \\\\{pc} -u {globalusername} -p {globalpassword} cmd /c "if exist {program_path} (echo 1) else (echo 0)"'
                        result = subprocess.check_output(command,shell=True)
                        
                        if result.decode('utf-8') == 1:
                            if messagebox.askyesno(title="All files exist",message=f"It looks like the program already exists on {pc} , continue?"):
                                installation_directory = ##INSTALLATION DIRECTORY
                                
                                command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                                result = subprocess.check_output(command, shell=True)
                                
                                print(result.decode('utf-8'))
                                
                                if os.path.exists("Reports"):
                                    
                                    reports_directory = os.path.join("Reports",f"TEAMS {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                    
                                else:
                                    os.mkdir("Reports")
                
                                    reports_directory = os.path.join("Reports",f"TEAMS {formatted_date}.txt")
                                    with open(reports_directory,'a') as a:
                                        a.write(f"{pc}: Installation launched successfully!")
                                
                            else:
                                pass
                        else:
                            installation_directory = ##INSTALLATION DIRECTORY
                                
                            command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{installation_directory}"'
                            result = subprocess.check_output(command, shell=True)
                                
                            print(result.decode('utf-8'))
                                
                            if os.path.exists("Reports"):
                                    
                                reports_directory = os.path.join("Reports",f"TEAMS {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!")
                                    
                            else:
                                os.mkdir("Reports")
                
                                reports_directory = os.path.join("Reports",f"TEAMS {formatted_date}.txt")
                                with open(reports_directory,'a') as a:
                                    a.write(f"{pc}: Installation launched successfully!")
                                    
                    except Exception as er:
                        if os.path.exists("Reports"):
                                    
                            reports_directory = os.path.join("Reports",f"TEAMS {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                            
                                    
                        else:
                            os.mkdir("Reports")
                
                            reports_directory = os.path.join("Reports",f"TEAMS {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} Failed with error: \n{er}\n\n")
                                
                        messagebox.showinfo(title="Error!",message=f"Experienced error for target {pc}  check reports folder for more info")
        
                        
                            
                            
                        
        
        
        
        
class CarePackage:
    def __init__(self):
        self.root = tk.Toplevel()
        self.mainframe = GlobalMainFrame(self.root,'CarePackage.png')
        self.musicchecker = GlobalCheckbox(self.root)
        
        
        self.source_text_label = tk.Label(self.root, text="Select Sources",font=("Impact",18),bg='green')
        self.source_text_label.place(relx=0.17,rely=0.4,anchor='center')
        
        self.text_source = tk.Text(self.root,width=55,height=5,bg='green')
        self.text_source.place(relx=0.29,rely=0.55,anchor='center')
        
        self.destination_text_label = tk.Label(self.root,text="Select Destination",font=("Impact",18),bg='green')
        self.destination_text_label.place(relx=0.8,rely=0.4,anchor='center')
        
        self.text_destination = tk.Text(self.root,width=40,height=1,bg='green')
        self.text_destination.place(relx=0.78,rely=0.55,anchor='center')
        
        self.launch_button = tk.Button(self.root, text="Launch",font=("arial",12),width=15,height=3,bg='green',command=self.transfer_files)
        self.launch_button.place(relx=0.5,rely=0.76,anchor='center')
        
        
        
        self.root.mainloop()
    def transfer_files(self):
        sources_list = []
        lines = self.text_source.get('1.0','end-1c').splitlines()
        for line in lines:
            sources_list.append(line)
            
        print(sources_list)
        destination = self.text_destination.get('1.0','end-1c')
        now = datetime.datetime.now()
        formatted_date = now.strftime('%Y-%m-%d__%H-%M-%S')
        
        if len(sources_list) == 0:
            pass
        
        else:
            if messagebox.askyesno(title="Transfer files",message="Are you sure you want to continue?"):
                for source in sources_list:
                    try:
                        
                        
                        # print(f'"{destination}"')
                        command = "Copy-Item -PATH " + source  + " -DESTINATION " + destination  + " -Recurse -Force"
                        output = subprocess.check_output(['powershell.exe', '-Command', command])
                        print(output.decode('utf-8'))
                        
                        if os.path.exists("Reports"):
                            
                            reports_directory = os.path.join("Reports",f"TRANSFER {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{source}: Transferred successfully to {destination}\n\n")
                                
                        else:
                            os.mkdir("Reports")
            
                            reports_directory = os.path.join("Reports",f"TRANSFER {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{source}: Transferred successfully to {destination}\n\n")
                                
                    except Exception as er:
                        messagebox.showinfo(title="Errors!",message=f"Errors occured in instance {source}, check reports folder for more info")
                        if os.path.exists("Reports"):
                            
                            reports_directory = os.path.join("Reports",f"TRANSFER {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{source} experienced error: \n{er} \n\n")
                                
                        else:
                            os.mkdir("Reports")
            
                            reports_directory = os.path.join("Reports",f"TRANSFER {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{source} experienced error: \n{er} \n\n")     
            else:
                pass
                        
                        
                        
                        
                        
                        
        
        
        
        
        
class SetupBase:
    def __init__(self):
        self.root = tk.Toplevel()
        
     
class KonicaMinolta:
    def __init__(self):
        self.root1 = tk.Toplevel()
        self.mainframe = GlobalMainFrame(self.root1,"Konica.png")
        
        self.pc_list = []
        
        self.music_check = GlobalCheckbox(self.root1)
        
        self.pc_list_text_label = tk.Label(self.root1,text="Select Target(s)", font=("Impact",18),bg='green')
        self.pc_list_text_label.place(relx=0.17,rely=0.2,anchor='center')
        
        self.text = tk.Text(self.root1,width=20,height=20,wrap="word",bg='green') 
        self.text.place(relx=0.17,rely=0.6,anchor='center')
        self.text.bind("<Key>",self.limit_line_length)
        self.launcher = tk.Button(self.root1,text="Launch",font=("arial",35),bg='green',command=self.Install_Drivers)
        self.launcher.place(relx=0.8,rely=0.5,anchor='center')
        
        
        self.root1.mainloop()
        
        
        
        
        
    def limit_line_length(self,event):
            
        widget = event.widget
        line,column = widget.index("insert").split('.')
        if len(widget.get(f"{line}.0",f"{line}.end")) > 7:
            widget.insert(f"{line}.{int(column)-1}",'\n')
            
        
            
            
            
    def Install_Drivers(self):
        self.pc_list = []
        lines = self.text.get('1.0','end-1c').splitlines()
        for line in lines:
            self.pc_list.append(line)
        print(self.pc_list)
            
        if len(self.pc_list) == 0:
            pass
        else:
            if messagebox.askyesno(title="Install Drivers",message=f"Are you sure you want to proceed? "):
                now = datetime.datetime.now()
                formatted_date = now.strftime("%Y-%m-%d__%H-%M-%S")
                for pc in self.pc_list:
                    remote_host = pc

                    program_path1 = ##PRINTER DRIVER1
                    program_path2 = ##PRINTER DRIVER2
                    print(f"{globalusername}")
                    print(globalpassword)
                    
                    try:
                        
                        
                        psexec_command = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{program_path1}"'
                        result = subprocess.check_output(psexec_command, shell=True)
                        print(result.decode('utf-8'))
                        
                        psexec_command1 = f'psexec \\\\{remote_host} -u {globalusername} -p {globalpassword} cmd /c "{program_path2}"'
                        result1 = subprocess.check_output(psexec_command1,shell=True)
                        print(result1.decode('utf-8'))
                    
                                            
                        if os.path.exists("Reports"):
                            
                            reports_directory = os.path.join("Reports",f"KONICA {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc}: Both Drivers Ran Successfully!")
                                
                        else:
                            os.mkdir("Reports")
            
                            reports_directory = os.path.join("Reports",f"KONICA {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc}: Both Drivers Ran Successfully!")
                    
                    except Exception as er:
                        messagebox.showinfo(title="Errors!",message=f"Errors occured in instance {pc}, check reports folder for more info")
                        if os.path.exists("Reports"):
                            
                            reports_directory = os.path.join("Reports",f"KONICA {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} experienced error: \n{er} \n\n")
                                
                        else:
                            os.mkdir("Reports")
            
                            reports_directory = os.path.join("Reports",f"KONICA {formatted_date}.txt")
                            with open(reports_directory,'a') as a:
                                a.write(f"{pc} experienced error: \n{er} \n\n")     
            else:
                pass
        
            
        
        
   
             


class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.background_image = os.path.join("media","background.jpg")
        self.bgimage = Image.open(self.background_image)
        self.canvas = tk.Canvas(self.root,width=self.bgimage.width,height=self.bgimage.height)
        
        self.canvas.pack()
        
        self.bgimage_tk = ImageTk.PhotoImage(self.bgimage)
        self.canvas.create_image(0,0,anchor='nw',image=self.bgimage_tk)
        
        
        self.root.wm_attributes('-alpha',True)
        
        self.geometry = self.root.geometry('800x500')
        self.title = self.root.title("ITStation")

        self.logo = os.path.join('media','logo2.png')
        self.label_image = Image.open(self.logo)
        self.label_image = self.label_image.resize((int(self.label_image.width * 0.5), int(self.label_image.height * 0.5)))
        self.photo = ImageTk.PhotoImage(self.label_image)
        
        self.canvas.create_image(400,250,image = self.photo)
        
        
        self.main_menu_title = os.path.join('media','top_text.png')
        self.top_text = Image.open(self.main_menu_title)
        self.top_text = self.top_text.resize((int(self.top_text.width*0.2),int(self.top_text.height*0.2)))
        self.tk_top_text = ImageTk.PhotoImage(self.top_text)
        self.canvas.create_image(400,50,image=self.tk_top_text)
        
        self.music_check = GlobalCheckbox(self.root) 
        
        self.btnframe = tk.Frame(self.root)
        self.btnframe.columnconfigure(0,weight=1)
        self.btnframe.columnconfigure(1,weight=1)
        self.btnframe.columnconfigure(2,weight=1)
        
        self.btn1 = tk.Button(self.btnframe,text = "Konica Minolta\nModernWarfare\n(Install Printers)",font=('arial',18),width=15,height=5,bg='green', command=self.Konica)
        self.btn1.grid(row=0,column=0, sticky =tk.W+tk.E)

        self.btn2 = tk.Button(self.btnframe,text = "Adobe\nAdvancedWarfare\n(Adobe Products)",font=('arial',18),width=15,height=5,bg='green',command=self.adobe)
        self.btn2.grid(row=0,column=1, sticky =tk.W+tk.E)

        self.btn3 = tk.Button(self.btnframe,text = "Status Report\n(Check Pc\nHealth)",font=('arial',18),width=15,height=5,bg='green')
        self.btn3.grid(row=0,column=2, sticky =tk.W+tk.E)

        self.btn4 = tk.Button(self.btnframe,text = "Microsoft\nBlackOps\n(Microsoft Products)",font=('arial',18),width=15,height=5,bg='green',command=self.microsoft)
        self.btn4.grid(row=1,column=0, sticky =tk.W+tk.E)

        self.btn5 = tk.Button(self.btnframe,text = "Care Package\n(Transfer Files)",font=('arial',18),width=15,height=5,bg='green',command=self.carepackage)
        self.btn5.grid(row=1,column=1, sticky =tk.W+tk.E)

        self.btn6 = tk.Button(self.btnframe,text = "Special",font=('arial',18),width=15,height=5,bg='green')
        self.btn6.grid(row=1,column=2, sticky =tk.W+tk.E)
        
        self.btnframe.place(relx=0.5,rely=0.5,anchor='center')
        self.root.mainloop()
        
    def Konica(self):
        KonicaMinolta()
        
    def microsoft(self):
        MicrosoftBlackOps()
        
    def adobe(self):
        AdobeAdvancedWarfare()
    
    def carepackage(self):
        CarePackage()



class Main:
    
    def __init__(self):
    
        self.root = tk.Tk()
        self.background_image = os.path.join("media","background.jpg")
        self.bgimage = Image.open(self.background_image)
        self.canvas = tk.Canvas(self.root,width=self.bgimage.width,height=self.bgimage.height)
        
        self.canvas.pack()
        
        self.bgimage_tk = ImageTk.PhotoImage(self.bgimage)
        self.canvas.create_image(0,0,anchor='nw',image=self.bgimage_tk)
        
        
        self.root.wm_attributes('-alpha',True)
        
        self.geometry = self.root.geometry('800x500')
        self.title = self.root.title("ITStation")
        
        self.logo = os.path.join('media','logo2.png')
        self.label_image = Image.open(self.logo)
        self.label_image = self.label_image.resize((int(self.label_image.width * 0.5), int(self.label_image.height * 0.5)))
        self.photo = ImageTk.PhotoImage(self.label_image)
        
        self.canvas.create_image(400,250,image = self.photo)
        
        
        self.login_title = os.path.join('media','login_title.png')
        self.top_text = Image.open(self.login_title)
        self.top_text = self.top_text.resize((int(self.top_text.width*0.2),int(self.top_text.height*0.2)))
        self.tk_top_text = ImageTk.PhotoImage(self.top_text)
        self.canvas.create_image(400,50,image=self.tk_top_text)
        
        self.label_notice = tk.Label(self.root,text=
                                     """
                                     Admin credentials will be used .
                                     to perform any action on this program 
                                     Please note that due to security reason, we are only able 
                                     to verify your username based on user accounts 
                                     that have previously logged into your personal computer. 
                                     Password and account WILL NOT be verified if you 
                                     enter them incorrectly so please make sure you 
                                     enter your information correctly before proceeding 
                                     to ensure program works correctly""", font=("impact",9),fg='red',bg='white')
        self.label_notice.place(relx='0.14',rely='0.83',anchor='center',width='350')
        
        
        self.music_checker = GlobalCheckbox(self.root)
        
        self.enter_account_label = tk.Label(self.root,text="Enter your Admin Account", font=('impact',16),bg='green')
        self.enter_account_label.place(relx=0.5,rely=0.2,anchor='center')
        
        self.username_label = tk.Label(self.root,text="Username",font=('arial',13),bg='green')
        self.username_label.place(relx=0.322,rely=0.35,anchor='center')
        
        self.password_label = tk.Label(self.root,text="Password",font=("arial",13),bg='green')
        self.password_label.place(relx=0.321,rely=0.55,anchor='center')
        
        try:
            creds_path = ".credentials\credentials.txt"
            with open(creds_path,'r') as r:
                list_str = r.read()
                self.creds = ast.literal_eval(list_str)
        except:
            self.creds = ['','']
            print('failed')
                
        self.entry_username = tk.Entry(self.root, width=60,bg='green',textvariable=tk.StringVar(value=self.creds[0]))
        self.entry_username.place(relx=0.5,rely=0.4,anchor='center')
        
        self.entry_password = tk.Entry(self.root,width=60,bg='green',textvariable=tk.StringVar(value=self.creds[1]))
        self.entry_password.place(relx=0.5,rely=0.6,anchor='center')
        
        self.submit_account_btn = tk.Button(self.root,text="Submit",bg='green',command=self.account_checker)
        self.submit_account_btn.place(relx=0.5,rely=0.7,anchor='center')
        
        self.check_rem_acc = tk.IntVar(value=1)
        self.remember_acc_check = tk.Checkbutton(self.root, text='Remember me',font=('arial',8), bg='green',variable=self.check_rem_acc)
        self.remember_acc_check.place(relx=0.5,rely=0.76,anchor='center')
        
        
        self.root.mainloop()
        
            
    def account_checker(self):
        try:
            user_name = self.entry_username.get()
            users_info = win32net.NetUserEnum(None,0,win32netcon.FILTER_NORMAL_ACCOUNT)
            print(users_info)
            for i in users_info[0]:
                if i['name'] == user_name:
                    print("User exists!")
                    self.main_menu()
                
            messagebox.showinfo(title="User not found!",message="User not found on system")
        except Exception as er:
            messagebox.showinfo(title="ERROR",message=f"An error has occured \n\n{er}")
    
    
    def main_menu(self):
        global globalusername
        global globalpassword
        globalusername = self.entry_username.get()
        globalpassword = self.entry_password.get()
    
        new_creds = [self.entry_username.get(), self.entry_password.get()]
        
        if self.check_rem_acc.get() == 1:
            if os.path.exists(".credentials"):
                file_directory = os.path.join(".credentials", "credentials.txt")
                if new_creds != self.creds:
                    with open(file_directory,'w') as w:
                        w.write(str(new_creds))
            else:
                os.mkdir(".credentials")
                try:
                    win32api.SetFileAttributes(".credentials",win32con.FILE_ATTRIBUTE_HIDDEN)
                except:
                    pass
                
                
                file_directory = os.path.join(".credentials", "credentials.txt")
                with open(file_directory,'w') as w:
                    w.write(str(new_creds))    
        else:
            shutil.rmtree(".credentials")
        
            
        self.root.destroy()
        MainMenu()
        
        # main_menu_root = tk.Tk()
        # main_menu_title = self.title
        # main_menu_geometry = self.geometry
        # main_menu_background_image = self.background_image
        # main_menu_bgimage = self.bgimage
        
        # main_menu_canvas = tk.Canvas(main_menu_root,width=main_menu_bgimage.width,height=main_menu_bgimage.height)
        
        
    

    
    
        
            
        
Main()
