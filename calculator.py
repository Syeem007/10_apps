from tkinter import *

expression = ""


def btn_clear():
    global expression
    expression = ''
    input_text.set('')


def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    input_text.set(expression)


def btn_equal():
    # global expression
    # result=str(eval(expression))
    # input_text.set(result)
    # input_text(0,result)

    answer = str(eval(input_text.get()))
    input_text.set(answer)




root = Tk()
root.title("Calculator")
root.geometry('300x300')
input_text = StringVar()
userinput = Entry(root, textvariable=input_text, font=('comic sans', 20), width=13)
userinput.place(x=10, y=5)
bt1 = Button(root, bd='3', text="1", width=4, command=lambda: press(1), font="Arial 12 bold")
bt1.place(x=10, y=50)
bt1 = Button(root, bd='3', text="2", width=4, command=lambda: press(2), font="Arial 12 bold")
bt1.place(x=60, y=50)
bt1 = Button(root, bd='3', text="3", width=4, command=lambda: press(3), font="Arial 12 bold")
bt1.place(x=110, y=50)
bt1 = Button(root, bd='3', text="4", width=4, command=lambda: press(4), font="Arial 12 bold")
bt1.place(x=10, y=100)
bt1 = Button(root, bd='3', text="5", width=4, command=lambda: press(5), font="Arial 12 bold")
bt1.place(x=60, y=100)
bt1 = Button(root, bd='3', text="6", width=4, command=lambda: press(6), font="Arial 12 bold")
bt1.place(x=110, y=100)
bt1 = Button(root, bd='3', text="7", width=4, command=lambda: press(7), font="Arial 12 bold")
bt1.place(x=10, y=150)
bt1 = Button(root, bd='3', text="8", width=4, command=lambda: press(8), font="Arial 12 bold")
bt1.place(x=60, y=150)
bt1 = Button(root, bd='3', text="9", width=4, command=lambda: press(9), font="Arial 12 bold")
bt1.place(x=110, y=150)
bt1 = Button(root, bd='3', text="0", width=4, command=lambda: press(0), font="Arial 12 bold")
bt1.place(x=60, y=200)
bt1 = Button(root, bd='3', text="clear", width=4, command=lambda: btn_clear(), font="Arial 12 bold")
bt1.place(x=10, y=200)
bt1 = Button(root, bd='3', text="Root", width=4, command=lambda: press(1), font="Arial 12 bold")
bt1.place(x=110, y=200)
bt1 = Button(root, bd='3', text="=", width=4, command=lambda: btn_equal(), font="Arial 12 bold")
bt1.place(x=60, y=250)
bt1 = Button(root, bd='3', text=".", width=4, command=lambda: press('.'), font="Arial 12 bold")
bt1.place(x=10, y=250)
bt1 = Button(root, bd='3', text="Pi", width=4, command=lambda: press(3.1246), font="Arial 12 bold")
bt1.place(x=110, y=250)
bt1 = Button(root, bd='3', text="%", width=4, command=lambda: press(1), font="Arial 12 bold")
bt1.place(x=160, y=250)
bt1 = Button(root, bd='3', text="+", width=4, command=lambda: press('+'), font="Arial 12 bold")
bt1.place(x=160, y=50)
bt1 = Button(root, bd='3', text="-", width=4, command=lambda: press('-'), font="Arial 12 bold")
bt1.place(x=160, y=100)
bt1 = Button(root, bd='3', text="*", width=4, command=lambda: press('*'), font="Arial 12 bold")
bt1.place(x=160, y=150)
bt1 = Button(root, bd='3', text="/", width=4, command=lambda: press('/'), font="Arial 12 bold")
bt1.place(x=160, y=200)

root.mainloop()
