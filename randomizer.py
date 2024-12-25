import tkinter as tk
from tkinter import ttk, Entry
import random
from tkinter import Button

def getRandomNumber():
    leftBorder = entryFrom.get()
    rightBorder = entryTo.get()

    if not leftBorder or not rightBorder:
        label.config(text="Введите границы")
        return

    try:
        leftBorder = int(leftBorder)
        rightBorder = int(rightBorder)
    except ValueError:
        label.config(text="Введите int")
        return

    if leftBorder > rightBorder:
        label.config(text="Введите правильный диапазон")
        return

    label.config(text=random.randint(leftBorder, rightBorder))

root = tk.Tk()
root.geometry('500x500')
root.title("Randomizer")

labelFrom = tk.Label(root, text="От")
labelFrom.place(x=50, y=10, anchor="w")

labelTo = tk.Label(root, text="До")
labelTo.place(x=450, y=10, anchor="e")

entryFrom = tk.Entry(root)
entryFrom.place(x=0, y=25, anchor="w")

entryTo = tk.Entry(root)
entryTo.place(x=500, y=25, anchor="e")

label = tk.Label(text = 0)
label.place(x=250, y=10, anchor="center")
button = Button(text = "Generate", command = getRandomNumber)
button.place(x=250, y=30, anchor="center")


root.mainloop()