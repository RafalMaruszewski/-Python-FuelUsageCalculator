import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets(root)
        root.resizable(False, False)

    def create_widgets(self, root):
        fuelAmountWindow = ttk.Entry()
        kmDrivenWindow = ttk.Entry()
        fuelAmountWindow.grid(column=1,row=1, sticky='E')
        kmDrivenWindow.grid(column=1,row=2, sticky='E') 

        ttk.Label(root, text="Zatankowano: ").grid(column=0, row=1, sticky='E')
       
        text2 = ttk.Label(text="Przejechano kilometrow: ").grid(column=0, row=2, sticky='E')
        
        text3 = ttk.Label(text="Spalanie: ").grid(column=0, row=3, sticky='E')
        
        try:    
            button = ttk.Button(text="Oblicz!", command=lambda: self.oblicz(fuelAmountWindow.get(),kmDrivenWindow.get())).grid(column=0, row=4)
        except AttributeError:
            pass
        
        spalanieWidget = ttk.Label().grid(column=1, row=3)     

    def say_hi(self):
        print("hi there, everyone!")
        
    def oblicz(self, no1, no2):
        try:
            spalanie = (round((float(no1)/float(no2))*100, 2))
            print (spalanie)
            #self.spalanieWidget.insert(spalanie)
        except ValueError:  
            pass

    def callback(self):
        print("Hi!")
  
root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1000,400)
app.mainloop()