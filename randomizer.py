import tkinter as tk
import random
from tkinter import Button

def getRandomNumber():
    label.config(text=random.randint(1, 100))

root = tk.Tk()
root.geometry('500x500')
root.title("Randomizer")
label = tk.Label(text = 0)
label.pack()
button = Button(text = "Generate", command = getRandomNumber)
button.pack()
root.mainloop()
