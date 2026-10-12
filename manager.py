#Develop the project's core information

from tkinter import *
from tkinter import ttk
from login import Login
from login import Registro
from container import Container
# It deals exclusively with "system" matters that directly affect how Python is running at that moment.
import sys
# Handling Word files
import os

class Manager(Tk):
    def __init__(self, *args, **kwagrs ):
        super().__init__(*args, **kwagrs)
        self.title("Mini store")
        self.geometry("1100x650+120+20")#window size, and coordinates
        self.resizable(False,False)
        
        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.configure(bg="#C6D9E3") #Bg color
        
        self.frames = {}
        for i in (Login, Registro, Container):
            frame = i(container, self)
            self.frames[i] = frame
        
        self.show_frame(Container)
        
        self.style = ttk.Style()
        self.style.theme_use("clam")      
        
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise
        
def main():
    app = Manager()
    app.mainloop()
    
if __name__ == "__main__":
    main()
