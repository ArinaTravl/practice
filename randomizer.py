import tkinter as tk
from tkinter import ttk, Entry
from tkinter import messagebox
from tkinter import Button
import random

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

    exceptions = listboxExceptions.get(0, tk.END)

    while True:
        randomNumber = random.randint(leftBorder, rightBorder)
        if randomNumber not in exceptions:
            break
    label.config(text=randomNumber)




def addException():
    try:
        exception = int(entryException.get())
    except ValueError:
        label.config(text="Введите int")
        return

    if exception and exception not in listboxExceptions.get(0, tk.END):
        listboxExceptions.insert(tk.END, exception)
    else:
        messagebox.showwarning("Ошибка", "Некорректное или повторяющееся исключение")
    print(listboxExceptions.get(0, tk.END))




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


entryException = tk.Entry(root)
entryException.place(x=250, y=75, anchor="center")

buttonAdd = tk.Button(root, text="Добавить исключение", command=addException)
buttonAdd.place(x=250, y=100, anchor="center")

listboxExceptions = tk.Listbox(root)
listboxExceptions.place(x=50, y=150, width=400, height=150)


root.mainloop()