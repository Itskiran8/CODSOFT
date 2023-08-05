
from tkinter import *
 
# globally declare the expression variable 
expression = ""
 
 
# Function to update expression in the entry box
def press(num):
    global expression
 
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
 
 
def equalpress():
          # used try and except statement to handle the errors 
    try:
        global expression
 
        result = str(eval(expression)) 
        equation.set(result)
    
        expression = ""
 
    except:
        equation.set(" error ")
        expression = ""
 
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
    # created a window
root = Tk()
 
root.configure(background="grey")
root.title("Kiran's Calculator")
root.geometry("350x360")
    
equation = StringVar()
 
    
expression_field = Entry(root,font=("ariel",20),bd=8, textvariable=equation)
 
    #used grid method for placing the widgets at respective positions in table like structure .
expression_field.grid(columnspan=4, ipadx=14,ipady=9)
 
    # created Buttons at a particular place
    
button1 = Button(root, text=' 1 ', fg='black', bg='powder blue',
                 command=lambda: press(1), height=4, width=10)
button1.grid(row=3, column=2)
 
button2 = Button(root, text=' 2 ', fg='black', bg='powder blue',
                    command=lambda: press(2), height=4, width=10)
button2.grid(row=3, column=1)
 
button3 = Button(root, text=' 3 ', fg='black', bg='powder blue',
                    command=lambda: press(3), height=4, width=10)
button3.grid(row=3, column=0)
 
button4 = Button(root, text=' 4 ', fg='black', bg='powder blue',
                command=lambda: press(4), height=4, width=10)
button4.grid(row=2, column=2)
 
button5 = Button(root, text=' 5 ', fg='black', bg='powder blue',
                    command=lambda: press(5), height=4, width=10)
button5.grid(row=2, column=1)
 
button6 = Button(root, text=' 6 ', fg='black', bg='powder blue',
                    command=lambda: press(6), height=4, width=10)
button6.grid(row=2, column=0)
 
button7 = Button(root, text=' 7 ', fg='black', bg='powder blue',
                    command=lambda: press(7), height=4, width=10)
button7.grid(row=1, column=2)
 
button8 = Button(root, text=' 8 ', fg='black', bg='powder blue',
                    command=lambda: press(8), height=4, width=10)
button8.grid(row=1, column=1)
 
button9 = Button(root, text=' 9 ', fg='black', bg='powder blue',
                    command=lambda: press(9), height=4, width=10)
button9.grid(row=1, column=0)
 
button0 = Button(root, text=' 0 ', fg='black', bg='powder blue',
                    command=lambda: press(0), height=4, width=10)
button0.grid(row=4, column=2)
 
plus = Button(root, text=' + ', fg='black', bg='powder blue',
                command=lambda: press("+"), height=4, width=10)
plus.grid(row=1, column=3)
 
minus = Button(root, text=' - ', fg='black', bg='powder blue',
                command=lambda: press("-"), height=4, width=10)
minus.grid(row=2, column=3)
 
multiply = Button(root, text=' * ', fg='black', bg='powder blue',
                    command=lambda: press("*"), height=4, width=10)
multiply.grid(row=3, column=3)
 
divide = Button(root, text=' / ', fg='black', bg='powder blue',
                    command=lambda: press("/"), height=4, width=10)
divide.grid(row=4, column=3)
 
equal = Button(root, text=' = ', fg='black', bg='powder blue',
                command=equalpress, height=4, width=10)
equal.grid(row=4, column=1)
 
clear = Button(root, text='C', fg='black', bg='powder blue',
                command=clear, height=4, width=10)
clear.grid(row=4, column='0')

root.mainloop()