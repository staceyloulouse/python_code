import tkinter as tk
from tkinter import Button
from tkinter import StringVar
from tkinter import Entry
from tkinter import Label

# setup the frame of the interface and give it a title and background color
root = tk.Tk()
root.title('Basic Calculator')
root.configure(background='light blue')

# operator string
operator = ''
textInput = StringVar()
statusText = StringVar()

# setup calculator environment
e = Entry(root, fg = 'green', textvariable= textInput,justify='right',width = 70, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 5, padx=20,pady=20)

# reaction to clicking the numbers and operator buttons
def click_action(input):
    global operator
    global statusText
    operator += str(input)
    textInput.set(operator)
    statusText.set('current entry: ' + operator)
    
#preview area function
def updateStatus():
    global operator
    global statusText
    statusText = statusText + operator
    statusText.set(statusText)

#clear button function
def actionClear():
    global operator
    global statusText
    statusText.set(operator + ' cleared')
    operator = ''
    textInput.set('0')

#equal button function
def actionEqual():
    global operator
    global statusText
    answer = ''
    try:
        answer = str(eval(operator))
        textInput.set(answer)
        statusText.set(operator + '= '+ answer)
    except SyntaxError as y:
        statusText.set('Error')
        print(y.args)
    
#negate button function
def actionNegate():
    global operator
    operator = '-('+operator+')'
    textInput.set(operator)

#percent function
def actionPercent():
    global operator
    try:
        answer = str(eval(operator)/100)
        textInput.set(answer)
        statusText.set('('+ operator + ')%= '+ answer) 
        operator = answer
    except SyntaxError as y:
        statusText.set('Error')
        print(y.args)

def actionFactorial():
    global operator
    try:
        answer = 1
        base = int(str(eval(operator)))
        statusText.set('current entry: '+operator)
        while base>1:
            answer*=base
            base-=1
        textInput.set(answer)
        statusText.set('('+ operator + ')!= '+ str(answer))
    except SyntaxError:
        statusText.set('Error')
    except ValueError:
        statusText.set('Only Integers Expected')

#define buttons in top row (7,8,9,/)=================================================
button7 = Button(root, text = "7", command=lambda: click_action(7),padx=40,pady=20, bg='navy', fg='white')
button7.grid(row=2, column=0)

button8 = Button(root, text = "8", command=lambda: click_action(8),padx=40,pady=20, bg='navy', fg='white')
button8.grid(row=2, column=1)

button9 = Button(root, text = "9", command=lambda: click_action(9),padx=40,pady=20, bg='navy', fg='white')
button9.grid(row=2, column=2)

buttonDivide = Button(root, text = "/", command = lambda: click_action("/"), padx=40,pady=20, bg='navy', fg='white')
buttonDivide.grid(row=2, column=3)

#Second row of buttons (4, 5,6,*)===================================================
button4 = Button(root, text = "4", command=lambda: click_action(4),padx=40,pady=20, bg='navy', fg='white')
button4.grid(row=3, column=0)

button5 = Button(root, text = "5", command=lambda: click_action(5),padx=40,pady=20, bg='navy', fg='white')
button5.grid(row=3,column=1)

button6 = Button(root, text = "6", command=lambda: click_action(6),padx=40,pady=20, bg='navy', fg='white')
button6.grid(row=3, column=2)

buttonMultiply = Button(root, text = "*", command=lambda: click_action('*'),padx=40,pady=20, bg='navy', fg='white')
buttonMultiply.grid(row=3, column=3)

#Third row of buttons (1,2,3,-)=======================================================

button1 = Button(root, text = "1", command=lambda: click_action(1),padx=40,pady=20, bg='navy', fg='white')
button1.grid(row=4, column=0)

button2 = Button(root, text = "2", command=lambda: click_action(2),padx=40,pady=20, bg='navy', fg='white')
button2.grid(row=4, column=1)

button3 = Button(root, text = "3", command=lambda: click_action(3),padx=40,pady=20, bg='navy', fg='white')
button3.grid(row=4, column=2)

buttonSubtract = Button(root, text = "-", command=lambda: click_action('-'),padx=40,pady=20, bg='navy', fg='white')
buttonSubtract.grid(row=4, column=3)

#Fourth row of buttons ((-),0,+,.)=======================================================
buttonNegate = Button(root, text = "(-)", command = lambda: actionNegate(), padx=35,pady=20, bg='navy', fg='white')
buttonNegate.grid(row=5, column=0)

button0 = Button(root, text = "0", command=lambda: click_action(0),padx=40,pady=20, bg='navy', fg='white')
button0.grid(row=5, column=1)

buttonDecimal = Button(root, text = ".", command=lambda: click_action('.'),padx=42,pady=20, bg='navy', fg='white')
buttonDecimal.grid(row=5, column=2)

buttonAdd = Button(root, text = "+", command=lambda: click_action('+'),padx=40,pady=20, bg='navy', fg='white')
buttonAdd.grid(row=5, column=3)

#Fifth row of buttons (x,y,,,%,nPr)==========================================================

buttonFactorial = Button(root, text = "!", command = lambda: actionFactorial(),padx=40,pady=20, bg='navy', fg='white')
buttonFactorial.grid(row=6, column=0)

buttonPercent = Button(root, text = "%", command = lambda: actionPercent(), padx=40,pady=20, bg='navy', fg='white')
buttonPercent.grid(row=6,column=1)

buttonEqual = Button(root, text = "=", command = lambda: actionEqual(), padx=40,pady=20, bg='navy', fg='white')
buttonEqual.grid(row=6, column=2)

buttonClear = Button(root, text = "Clear", command = lambda: actionClear(),padx=30,pady=20, bg='navy', fg='white')
buttonClear.grid(row=6, column=3)

#status message area
statusMessage = Label(root, fg = 'white', textvariable= statusText, bg='grey')
statusMessage.grid(row=9,column=0,columnspan=3)

# repeat root display until window closes
root.mainloop()
