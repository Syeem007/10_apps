import time
from tkinter import *

count = 0


class App():



    def update_clock(self):
        # t = time.localtime()
        self.now = time.strftime("%H:%M:%S")
        self.label.configure(text=self.now)
        self.root.after(1000, self.update_clock)

    def __init__(self):
        self.root = Tk()
        self.head = Label(self.root, text='Digital watch', font=('comic sans', 20))
        self.label = Label(self.root, text="", font="Courier 40 bold")
        self.label.grid(row=4, columnspan=2)
        self.update_clock()
        self.root.mainloop()


a = App()
