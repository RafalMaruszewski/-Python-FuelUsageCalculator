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
        self.create_widgets(root)
        root.resizable(False, False)

    def create_widgets(self, root):

        
        fuelAmountWindow = ttk.Entry()#.grid(column=1,row=1, sticky='E')
        kmDrivenWindow = ttk.Entry()#.grid(column=1,row=2, sticky='E')
        fuelAmountWindow.grid(column=1,row=1, sticky='E')
        kmDrivenWindow.grid(column=1,row=2, sticky='E') 

    
       # fuelAmount = fuelAmountWindow.get()
       # print("fuelAmount value: "+fuelAmount)
       # kmDriven = kmDrivenWindow.get()
        #print("kmDriven value: "+kmDriven)
        
#tk.DoubleVar()

        ttk.Label(root, text="Zatankowano: ").grid(column=0, row=1, sticky='E')
       
        text2 = ttk.Label(text="Przejechano kilometrow: ").grid(column=0, row=2, sticky='E')

        text3 = ttk.Label(text = "").grid(column=1, row=3)
        try:    
            button = ttk.Button(text="Oblicz!", command=lambda: self.oblicz(fuelAmountWindow.get(),kmDrivenWindow.get())).grid(column=0, row=3)
        except AttributeError:
            pass
        
    def say_hi(self):
        print("hi there, everyone!")
        
    def oblicz(self, no1, no2):
    
        try:
           # print("no1 value: "+str(no1))
           # print("no2 value: "+str(no2))
            print (round((float(no1)/float(no2))*100, 2))
        except ValueError:  
            pass
        
    def callback(self):
        print("Hi!")
        
        
root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1000,400)
app.mainloop()