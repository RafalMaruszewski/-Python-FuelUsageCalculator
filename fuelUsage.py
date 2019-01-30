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
        fuelAmount = tk.DoubleVar()
        kmDriven = tk.DoubleVar()
        fuelAmountWindow = ttk.Entry().grid(column=1,row=1, sticky='E')
        kmDrivenWindow = ttk.Entry().grid(column=1,row=2, sticky='E')

        ttk.Label(root, text="Zatankowano: ").grid(column=0, row=1, sticky='E')
       
        text2 = ttk.Label(text="Przejechano kilometrow: ").grid(column=0, row=2, sticky='E')

        text3 = ttk.Label(text = "").grid(column=1, row=3)
  
        button = ttk.Button(text="Oblicz!", command=self.oblicz(fuelAmount, kmDriven)).grid(column=0, row=3)

    def say_hi(self):
        print("hi there, everyone!")
        
    def oblicz(self, fuelFilled, kilometersDriven):
        return round((fuelFilled/kilometersDriven)*100, 2)

root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1000,400)
app.mainloop()