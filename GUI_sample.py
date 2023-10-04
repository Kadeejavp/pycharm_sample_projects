from tkinter import *

root = Tk()
root.geometry("280x440+400+100")
root.configure(bg="#e3d9ca")
root.title("Calculator")

text = ""

def button_press(num):
    global text
    if equation.get() == "ERROR":
        clear_press()
    text = equation.get() + str(num)
    equation.set(text)

def clear_press():
    equation.set("")

def equal_press():
    try:
        text=eval(equation.get())
        equation.set(text)
    except:
        text="ERROR"
        equation.set(text)



equation = StringVar()
textfield = Entry(root, textvariable=equation,width=10,font=('Helvetica 45'))
textfield.grid(row=0, column=0, columnspan=4)

b7 = Button(root, text="7", width=8, height=4, bg="#e6c99c", command=lambda: button_press(7))
b8 = Button(root, text="8", width=8, height=4, bg="#e6c99c", command=lambda: button_press(8))
b9 = Button(root, text="9", width=8, height=4, bg="#e6c99c", command=lambda: button_press(9))
b4 = Button(root, text="4", width=8, height=4, bg="#e6c99c", command=lambda: button_press(4))
b5 = Button(root, text="5", width=8, height=4, bg="#e6c99c", command=lambda: button_press(5))
b6 = Button(root, text="6", width=8, height=4, bg="#e6c99c", command=lambda: button_press(6))
b1 = Button(root, text="1", width=8, height=4, bg="#e6c99c", command=lambda: button_press(1))
b2 = Button(root, text="2", width=8, height=4, bg="#e6c99c", command=lambda: button_press(2))
b3 = Button(root, text="3", width=8, height=4, bg="#e6c99c", command=lambda: button_press(3))
bdot = Button(root, text=".", width=8, height=4, bg="#e6c99c", command=lambda: button_press("."))
b0 = Button(root, text="0", width=8, height=4, bg="#e6c99c", command=lambda: button_press(0))
bequal = Button(root, text="=", width=18, height=4, bg="#e6c99c", command=lambda: equal_press())
bplus = Button(root, text="+", width=8, height=4, bg="#e6c99c", command=lambda: button_press("+"))
bminus = Button(root, text="-", width=8, height=4, bg="#e6c99c", command=lambda: button_press("-"))
bmul = Button(root, text="x", width=8, height=4, bg="#e6c99c", command=lambda: button_press("*"))
bdiv = Button(root, text="/", width=8, height=4, bg="#e6c99c", command=lambda: button_press("/"))
bclear = Button(root, text="C", width=28, height=4, bg="#e6c99c", command=lambda: clear_press())

bclear.place(x=0, y=70)
bdiv.place(x=210, y=70)
b7.place(x=0, y=143)
b8.place(x=70, y=143)
b9.place(x=140, y=143)
bmul.place(x=210, y=143)
b4.place(x=0, y=216)
b5.place(x=70, y=216)
b6.place(x=140, y=216)
bminus.place(x=210, y=216)
b1.place(x=0, y=289)
b2.place(x=70, y=289)
b3.place(x=140, y=289)
bplus.place(x=210, y=289)
bdot.place(x=0, y=363)
b0.place(x=70, y=363)
bequal.place(x=140, y=363)

root.mainloop()
