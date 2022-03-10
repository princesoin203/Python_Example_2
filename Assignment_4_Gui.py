# Assignment 4 - Graphical User Interface
# Author - Prince Soin
# Student ID - u3229940
# Description - Comparing Airplanes using a graphical user interface.


# GUI
from tkinter import *


# Functions
def length_1():
    result = round((eval(speed_1.get()) * eval(speed_1.get())) / (2 * eval(acceleration_1.get())), 2)
    guiResult1.set(result)


def seconds_1():
    result = 3 * eval(length_1.get())
    guiResult1.set(result)


def length_2():
    result = round((eval(speed_2.get()) * eval(speed_2.get())) / (2 * eval(acceleration_2.get())), 2)
    guiResult2.set(result)


def seconds_2():
    result = 3 * eval(length_2.get())
    guiResult2.set(result)


def testcolour(event):
    lstOptions["bg"] = lstOptions.get(lstOptions.curselection())


def close_window():
    window.destroy()


# List
L = ["Blue", "Pink", "Orange"]
colour_option = ["blue", "green", "yellow", "red", "pink"]
lstItems = [0]
window = Tk()
window.title("Comparing Airplanes")


# Adding labels
MyFirstLabel = Label(window, text="Speed of Plane 1:")
MyFirstLabel.grid(row=0, column=0)


MySecondLabel = Label(window, text="Acceleration of Plane 1:")
MySecondLabel.grid(row=2, column=0)


MyThirdLabel = Label(window, text="Speed of Plane 2:")
MyThirdLabel.grid(row=4, column=0)


MyFourthLabel = Label(window, text="Acceleration of Plane 2:")
MyFourthLabel.grid(row=6, column=0)


MyFifthLabel = Label(window, text="Plane 1 length required (metres):")
MyFifthLabel.grid(row=1, column=5)


MySixthLabel = Label(window, text="Plane 2 length required (metres):")
MySixthLabel.grid(row=5, column=5)


MySeventhLabel = Label(window, text="Test planes colour:")
MySeventhLabel.grid(row=7, column=3)


# Adding entries
speed_1 = StringVar()
entFirst = Entry(window, width=5, textvariable=speed_1)
entFirst.grid(row=1, column=0)


acceleration_1 = StringVar()
entSecond = Entry(window, width=5, textvariable=acceleration_1)
entSecond.grid(row=3, column=0)


speed_2 = StringVar()
entThird = Entry(window, width=5, textvariable=speed_2)
entThird.grid(row=5, column=0)


acceleration_2 = StringVar()
entFourth = Entry(window, width=5, textvariable=acceleration_2)
entFourth.grid(row=7, column=0)


guiResult1 = StringVar()
entFourth = Entry(window, width=8, textvariable=guiResult1)
entFourth.grid(row=2, column=5)


guiResult2 = StringVar()
entFourth = Entry(window, width=8, textvariable=guiResult2)
entFourth.grid(row=6, column=5)


# Adding buttons
btnExit = Button(window, width=3, text='Exit', command=close_window)
btnExit.grid(row=0, column=7, padx=15, pady=5)


btnlength1 = Button(window, width=29, text='Calculate Plane 1 length requirement', command=length_1)
btnlength1.grid(row=3, column=3, padx=15, pady=5)


btnlength2 = Button(window, width=29, text='Calculate Plane 2 length requirement', command=length_2)
btnlength2.grid(row=4, column=3, padx=15, pady=5)


# Colour list
varOptions = StringVar()
lstOptions = Listbox(window, width=10, height=5, listvariable=varOptions)
lstOptions.grid(row=12, column=3)
varOptions.set(tuple(colour_option))
lstOptions.bind("<<ListboxSelect>>", testcolour)


window.mainloop()
