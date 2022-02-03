# Import the required libraries
from tkinter import *
import turtle



# Create an instance of tkinter frame or window
display = Tk()
display.configure(background = "black")
display.title("My JOURNEY")


# Create two frames in the window
calc = Frame(display)
paint = Frame(display)
paint.configure(background = "blue")
calc.configure(background = "lavender", width = 2000, height = 2000)


# Define a function for switching the frames
def change_to_calc():
    calc.pack(fill='both', expand=1)
    paint.pack_forget()
    display.title("Calculator")

def change_to_paint():
    paint.pack(fill='both', expand=1)
    calc.pack_forget()
    display.title("Paint")


# Add a button to switch between two frames
label1 = Label(display,text="WELCOME TO MY PROJECT", font="arial 25 bold" ,bg="black",fg="white")
label1.pack()
btn1 = Button(display, text="Calculator", command=change_to_calc,background = "black", fg = "white")
btn1.pack(pady= 20)

btn2 = Button(display, text="Paint", command=change_to_paint,background = "black", fg="white")
btn2.pack(pady=20)

#paint
canvas = Canvas(master = paint, width = 1360, height = 700)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')

#draw = turtle.Turtle()
draw = turtle.RawTurtle(canvas)
textarea = Entry(master=paint,width=30,font="arial 20")
textarea.grid(row=0,column=5)


def square():
    draw.reset()
    global textarea
    for i in range(4):
       draw.forward(int(textarea.get()))
       draw.left(90)
    
def circle():
    draw.reset()
    global textarea
    draw.circle(int(textarea.get()))

def triangle():
    draw.reset()
    global textarea
    for i in range(4):
      draw.forward(int(textarea.get()))
      draw.left(120)

def Dimen():
    draw.reset()
    global textarea
    d = int(textarea.get())
    for i in range(50):
       draw.forward(d)
       draw.left(90)
       draw.forward(d)
       draw.left(90)
       d = d + 1
       draw.forward(d)

def spiral():
    draw.reset()
    global textarea
    a = int(textarea.get())     
    for i in range(30):
        draw.left(90)
        draw.forward(a)
        draw.left(90)
        draw.forward(a)
        draw.left(90)
        a = a + 20
        draw.forward(a)
        draw.left(90)
        draw.forward(a)
        a = a + 20
def Death():
    draw.reset()
    global textarea
    c = int(textarea.get())
    for i in range(4):
      draw.forward(c)
      draw.left(120)
    c = c/2
    b = c/1.73
    v = c*1.71
    draw.forward(c)
    draw.circle(b)
    draw.left(180)
    draw.forward(c)
    draw.left(240)
    draw.forward(c)
    draw.right(90)
    draw.forward(v)
    


sqButton = Button(master = paint, text ="⬛", command = square)
sqButton.grid(row=0,column=1)
sqButton.config(bg="black",fg="white")

cButton = Button(master = paint, text ="〇", command = circle)
cButton.grid(row=1,column=1)
cButton.config(bg="black",fg="white")

tButton = Button(master = paint, text ="∆", command = triangle)
tButton.grid(row=2,column=1)
tButton.config(bg="black",fg="white")


dButton = Button(master = paint, text ="▢", command = Dimen)
dButton.grid(row=3,column=1)
dButton.config(bg="black",fg="white")

sButton = Button(master = paint, text ="Spiral", command = spiral)
sButton.grid(row=4,column=1)
sButton.config(bg="black",fg="white")

DeaButton = Button(master = paint, text ="Deathly Hallows", command = Death)
DeaButton.grid(row=5,column=1)
DeaButton.config(bg="black",fg="white")

#Claculator
expression = ""
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression += str(num)
 
    # update the expression by using set method
    test.set(expression)


def equal():
    try:
        global expression

        total = str(eval(expression))

        test.set(total)

        expression = ""

    except:
 
        test.set("Sorry")
        expression = ""

def retry():
    global expression
    expression = ""
    test.set("")



test = StringVar()

label = Label(master=calc, textvariable=test, width = 15, height=5)
label.grid(row = 0, column = 10)


button1 = Button(master = calc, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=5, width=16)
button1.grid(row=2, column=9)
 
button2 = Button(master = calc, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=5, width=15)
button2.grid(row=2, column=10)
 
button3 = Button(master = calc, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=5, width=16)
button3.grid(row=2, column=11)
 
button4 = Button(master = calc, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=5, width=16)
button4.grid(row=3, column=9)
 
button5 = Button(master = calc, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=5, width=16)
button5.grid(row=3, column=10)
 
button6 = Button(master = calc, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=5, width=16)
button6.grid(row=3, column=11)
 
button7 = Button(master = calc, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=5, width=16)
button7.grid(row=4, column=9)
 
button8 = Button(master = calc, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=5, width=16)
button8.grid(row=4, column=10)
 
button9 = Button(master = calc, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=5, width=16)
button9.grid(row=4, column=11)
 
button0 = Button(master = calc, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=5, width=16)
button0.grid(row=5, column=9)

plus = Button(master = calc, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=5, width=16)
plus.grid(row=2, column=12)

minus = Button(master = calc, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=5, width=16)
minus.grid(row=3, column=12)

multiply = Button(master = calc, text=' x ', fg='black', bg='white', command=lambda: press("*"), height=5, width=16)
multiply.grid(row=4, column=12)

divide = Button(master = calc, text=' ÷ ', fg='black', bg='white', command=lambda: press("/"), height=5, width=16)
divide.grid(row=5, column=12)

equal_button = Button(master = calc, text=' = ', fg='black', bg='white', command=lambda: equal(), height=5, width=16)
equal_button.grid(row=5, column=10)

clear = Button(master = calc, text='⌫ ', fg='black', bg='white', command=lambda: retry(), height=5, width=16)
clear.grid(row=5, column=11)

display.mainloop()