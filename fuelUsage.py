'''

from tkinter import *
import tkinter as tk

mainWindow = Tk()
mainWindow.title("Fuel usage calculator")

class Application(tk.Frame):

	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
	
	def createWidgets(self):
		self.hi = tk.Button(self)
		self.hi.pack(side = "top")

	mainWindow.mainloop()
	
	'''
	
	
	
import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(self.oblicz(32, 350))
        

    def create_widgets(self, wartosc):
        fuelAmount = tk.StringVar()
        fuel = ttk.Entry(textvariable=fuelAmount)
        fuel.pack(side="bottom")
        
        kilometersDriven = tk.StringVar()
        kilometersDriven = ttk.Entry(textvariable=kilometersDriven)
        kilometersDriven.pack(side="bottom")
        
        text = ttk.Label(text="Zatankowano: ")
        text.pack(side="bottom")
        
        
        text2 = ttk.Label(text="Przejechano kilometrów: ")
        text2.pack(side="bottom")
        
        
        text3 = ttk.Label(text = wartosc)
        text3.pack(side="bottom")
        
    
        '''self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.progressbar = ttk.Progressbar(orient="horizontal")
        self.progressbar.pack(side="bottom")
    
    '''
    def say_hi(self):
        print("hi there, everyone!")
        
    def oblicz(self, fuelFilled, kilometersDriven):
        return round((fuelFilled/kilometersDriven)*100, 2)
        
        

root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1000,400)
app.mainloop()