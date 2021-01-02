from tkinter import *
from tkinter import ttk
from unitconvert import lengthunits
from unitconvert import massunits
from unitconvert import digitalunits
# window
root = Tk()
#root.geometry('300x350')
# name of app
head = Label(root, text='Unit Converter', font=('comic sans', 20))
head.grid(row=0, column=0, columnspan=1)

# inputbox
userin = IntVar()
userinput = Entry(root, textvariable=userin, font=('comic sans', 20), width=10)
userinput.grid(row=1, column=0, padx=10, pady=10)

# for combobox dropdown menu
uf = StringVar()
unitfirst = ttk.Combobox(root, textvariable=uf, font=('comic sans', 20), width=10)
#unitfirst['value'] = ('mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi')
#unitfirst['value'] = ('mg', 'gm', ' oz', 'lb', 'kg')
unitfirst['value'] = ('B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB' ,'KiB', 'MiB', 'GiB','TiB', 'PiB','EiB',' ZiB',' YiB')
unitfirst.grid(row=1, column=1, padx=10, pady=10)

resultin = IntVar()
result = Label(root, textvariable=resultin, font=('comic sans', 20), width=10)
result.grid(row=2, column=0, padx=10, pady=10)

us = StringVar()
unitsecond = ttk.Combobox(root, textvariable=us, font=('comic cans', 20), width=10)
#unitsecond['value'] = ('mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi')
#unitsecond['value'] = ('mg', 'gm', ' oz', 'lb', 'kg')
unitsecond['value'] = ('B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB' ,'KiB', 'MiB', 'GiB','TiB', 'PiB','EiB',' ZiB',' YiB')
unitsecond.grid(row=2, column=1, padx=10, pady=10)


def conv():
    #a = lengthunits.LengthUnit(userin.get(), f'{uf.get()}', f'{us.get()}').doconvert()
    # b = massunits.MassUnit(userin.get(), f'{uf.get()}', f'{us.get()}').doconvert()
    c=digitalunits.DigitalUnit(userin.get(), f'{uf.get()}', f'{us.get()}').doconvert()
    #resultin.set(a)
    #resultin.set(b)
    resultin.set(c)


def clearFunc():
    resultin.set(0)

# Button
submit = Button(root, text='SUBMIT', font=('comic cans', 20), command=conv)
submit.grid(row=3, columnspan=2)

reset = Button(root, text='RESET', font=('comic cans', 20),command=clearFunc)
reset.grid(row=4, columnspan=2)

root.mainloop()
