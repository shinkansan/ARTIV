from tkinter import *
import tkinter.messagebox
import subprocess
import psutil
import os
import threading

class ServerUI:

    def __init__(self):
        self.root = Tk()
        frame = Frame(self.root)
        frame.pack(padx=5, pady=5)

        self.server_pids = self.get_server_process_list()
        if len(self.server_pids):
            self.status_label = Label(text="IMU Server Running")
            self.start_button = Button(frame, text ="Start", command = self.start_server, state="disabled")
        else:
            self.status_label = Label(text="IMU Server Stopped")
            self.start_button = Button(frame, text ="Start", command = self.start_server)    
        self.status_label.pack(side=TOP, anchor=W)
        self.start_button.pack(side=LEFT)
        
        self.stop_button = Button(frame, text ="Stop", command = self.stop_server)
        self.stop_button.pack(side=RIGHT)

        self.monitor()
        self.root.mainloop()

    def monitor(self):
        self.root.after(1000, self.monitor)
        self.server_pids = self.get_server_process_list()
        if len(self.server_pids):
            self.status_label["text"] = "IMU Server Running"
            self.start_button["state"] = "disabled"
        else:
            self.status_label["text"] = "IMU Server Stopped"
            self.start_button["state"] = "normal"
       
    def find_server(self, name):
        ls = []
        for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
            if 'Python' == p.info['name']:      # find running Python things
                try:
                    if p.info['cmdline'][1] == name:     #match to server name
                        ls.append(p.pid)
                except:
                    pass
        return ls

    def get_server_process_list(self):
        ls = self.find_server('server.py')
        return ls
    
    def start_server(self):
        proc = subprocess.Popen(["python3", "server.py"])
        self.status_label["text"] = "IMU Server Running"

    def stop_server(self):
        server_pids = self.get_server_process_list()
        for pid in server_pids:
            p = psutil.Process(pid)
            p.kill()


server_ui = ServerUI()
