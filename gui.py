from tkinter import *
from environment import Environment, Food
from individual import Individual
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

# hyper parameters
windowSize = 100

# create the MAIN and ONLY window
window = Tk()
window.title("Simple Digital Life Instance")
window.geometry('1350x675')
environment = Environment(windowSize)


def displayEnvironment(environment):
    # squares with nothing are shown as grass.jpg
    # squares with food are shown as food.jpg
    # squares with individuals are shown as cell.jpg
    window.destroy()
    t = Table(window)


class Table:

    def __init__(self, root):
        grass = ttk.Treeview(root,
                             columns=('one'))
        grass.heading('one', text='one')
        grass.pack()

        grass.img = Image.new(mode='RGBA', size=(10, 20), color='green')
        grass.img = ImageTk.PhotoImage(grass.img)

        # code for creating table
        for i in range(windowSize):
            for j in range(windowSize):

                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                locationList = environment.getPos((i, j))

                if len(locationList) == 0:
                    self.e.insert(END, grass.img)
                elif type(locationList[0]) == Individual:
                    self.e.insert(END, cell.jpg)
                else:
                    self.e.insert(END, food.jpg)


displayEnvironment(environment)

for x in range(100):
    environment.step()
    displayEnvironment(environment)

# Run forever!
window.mainloop()
