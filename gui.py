from tkinter import *
from environment import Environment, Food
from individual import Individual
import sys
import os

# hyper parameters
windowSize = 100

# create the MAIN and ONLY window
window = Tk()
window.title("Simple Digital Life Instance")
window.geometry('1350x675')

environment = Environment(windowSize)

# Run forever!
window.mainloop()
