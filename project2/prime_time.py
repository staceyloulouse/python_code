import tkinter as tk
from tkinter import Button
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Entry
from tkinter import Label
import random
import time
from PIL import ImageTk, Image
from playsound import playsound


#setup the frame of the interface and give it a title
root = tk.Tk()
root.title("Prime Time Game")
root.iconbitmap('C:\\Users\\stace\\OneDrive\\Documents\\python\\1PrimeTime\\iconImage.ico')
root.configure(background='light grey')

#variable definitions
operator = ''
textInput = StringVar()
f1Input = StringVar()
f2Input = StringVar()
score = 0
statusText = StringVar(root,'Select Difficulty Level')
scoreText = StringVar(root,'Score = '+ str(score))
life1=True
life2=True
zap_life=2
primes=[2,3,5,7,11]

increase_by=100

#setup prime time game environment
e = Entry(root, fg = 'navy', textvariable= textInput, justify='right', width = 10, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 5, padx=10,pady=10)

f1 = Entry(root, fg = 'navy', textvariable= f1Input,justify='right',width = 10,borderwidth = 5)
f1.grid(row = 1, column = 0, columnspan = 2, padx=10,pady=10)
f2 = Entry(root, fg = 'navy', textvariable= f2Input, justify='right', width = 10, borderwidth = 5)
f2.grid(row = 1, column = 2, columnspan = 3, padx=10,pady=10)
signLabel = Label(root, fg='navy', text='x', justify='center', bg='light grey', padx=10, pady=10)
signLabel.grid(row=1,column=1,columnspan=2, padx=10, pady=10)

#reaction to clicking the number buttons
def numClick(number):
    global operator
    global statusText
    global f1Input, f2Input
    
    statusText.set('current entry: ' + str(number))
    if f1.get() == '':
        operator = str(number)
        f1Input.set(operator)
    else:
        operator+='*'+ str(number)
        f2Input.set(number)
        checkEntry()

# checking to see if the selections are correct        
def checkEntry():
    global f1Input, f2Input, operator
    global life1,life2
    try:
        answer = str(eval(operator))
        statusText.set(operator + '= '+ answer)

        if str(answer) == textInput.get():
            statusText.set('Excellent! Click Next.')
            scoreUp()
            scoreText.set('Score: '+ str(score))
            #play chime or applause
            playsound('C:\\Users\\stace\\OneDrive\\Documents\\python\\1PrimeTime\\TaDaSound.mp3')
        else:
            statusText.set('Wrong!')
            life_loss()
            #play chime or smashing
            playsound('C:\\Users\\stace\\OneDrive\\Documents\\python\\1PrimeTime\\Smashing.mp3')
    except SyntaxError as y:
        statusText.set('Error')
        print(y.args)

# changing the difficulty level    
def setLevel(level):
    global primes
    global increase_by

    if level == 'EASY':
        increase_by=100
        primes = [2,3,5,7,11,13,17]
        statusText.set('Level EASY, Let\'s PLAY!')
    else:
        increase_by=500
        statusText.set('Level: HARD, You\'re Brave!')
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41]
#lose a life
def life_loss():
    global zap_life
    
    if zap_life>1:
        buttonLife2.destroy()
        zap_life-=1
    elif zap_life>0:
        buttonLife1.destroy()
        zap_life-=1
    else:
        gameOver()

# action for the play button
def play():
    #Start or restart the game
    global operator
    global score
    global primes

    statusText.set('New Game. Let\'s Go!')
    score=0
    scoreText.set('Score: '+ str(score))
    buttonLife1.config(text = '\u2764 LIFE \u2764') 
    buttonLife2.config(text = '\u2764 LIFE \u2764')
    # clear the display fields
    operator = ''
    textInput.set('')
    f1Input.set('')
    f2Input.set('')
    actionNext()
    buttonPlay.config(state='disabled')

#destroy the prime number buttons when the game is over    
def gameOver():
    for blink in range(1,101):
        statusText.set('GAME OVER! Click Quit or Play')
        textInput.set('Game Over')
        if blink%2==0:
            showScore.config(fg='red')
            statusMessage.config(fg = 'red')
        else:
            showScore.config(fg='white')
            statusMessage.config(fg = 'white')
        statusText.set('Click NEXT or Quit!')

# increase the player's score by the increment amount
def scoreUp():
    global score
    global increase_by
    score += increase_by
    scoreText.set('Score: '+ str(score))
    if score>5000:
        statusText.set('Leveled Up to HARD!')
        setLevel('HARD')
    elif score>7000:
        increase_by=1000

#next button function
def actionNext():
    global operator
    global statusText
    global primes
    statusText.set(operator + ' cleared')
    operator = ''
    textInput.set('')
    f1Input.set('')
    f2Input.set('')
    # display a random composite number 
    n=len(primes)-1
    num1=primes[random.randint(0,n)]
    num2=primes[random.randint(0,n)]
    textInput.set(num1*num2)

# buttons
#define buttons in top row (2,3,5,EASY)=================================================
button2 = Button(root, text = "2", command=lambda: numClick(2),padx=40,pady=20, bg='navy', fg='white')
button2.grid(row=2, column=0)

button3 = Button(root, text = "3", command=lambda: numClick(3),padx=40,pady=20, bg='navy', fg='white')
button3.grid(row=2, column=1)

button5 = Button(root, text = "5", command=lambda: numClick(5),padx=42,pady=20, bg='navy', fg='white')
button5.grid(row=2, column=2)

# Second row of buttons (7,11,13,HARD)===================================================
button7 = Button(root, text = "7", command=lambda: numClick(7),padx=40,pady=20, bg='navy', fg='white')
button7.grid(row=3, column=0)

button11 =Button(root, text = "11", command=lambda: numClick(11),padx=40,pady=20, bg='navy', fg='white')
button11.grid(row=3,column=1)

button13 =Button(root, text = "13", command=lambda: numClick(13),padx=40,pady=20, bg='navy', fg='white')
button13.grid(row=3, column=2)

#Third row of buttons (17,19,23,PLAY)=======================================================

button17 =Button(root, text = "17", command=lambda: numClick(17),padx=40,pady=20, bg='navy', fg='white')
button17.grid(row=4, column=0)

button19 =Button(root, text = "19", command=lambda: numClick(19),padx=40,pady=20, bg='navy', fg='white')
button19.grid(row=4, column=1)

button23 = Button(root, text = "23", command=lambda: numClick(23),padx=40,pady=20, bg='navy', fg='white')
button23.grid(row=4, column=2)

#Fourth row of buttons (29,31,37,NEXT)=======================================================
button29 = Button(root, text = "29", command = lambda: numClick(29), padx=40,pady=20, bg='navy', fg='white')
button29.grid(row=5, column=0)

button31 = Button(root, text = "31", command=lambda: numClick(31),padx=40,pady=20, bg='navy', fg='white')
button31.grid(row=5, column=1)

button37 = Button(root, text = "37", command=lambda: numClick(37),padx=40,pady=20, bg='navy', fg='white')
button37.grid(row=5, column=2)

#Fifth row of buttons (41,Life,Life,QUIT)==========================================================

button41 = Button(root, text = "41", command = lambda: numClick(41), padx=40,pady=20, bg='navy', fg='white')
button41.grid(row=6, column=0)

# navigation buttons on fourth column (EASY, HARD, PLAY, NEXT, QUIT)
buttonEasy = Button(root, text = "EASY", command = lambda: setLevel('EASY'), padx=37,pady=20, bg='light blue', fg='navy',borderwidth = 5)
buttonEasy.grid(row=2, column=3)

buttonHard = Button(root, text = "HARD", command=lambda: setLevel('HARD'),padx=35,pady=20, bg='light blue', fg='navy',borderwidth = 5)
buttonHard.grid(row=3, column=3)

buttonPlay = Button(root, text = "PLAY", command=play,padx=37,pady=20, bg='light blue', fg='navy',borderwidth = 5)
buttonPlay.grid(row=4, column=3)

buttonNext = Button(root, text = "NEXT", command=lambda: actionNext(),padx=37,pady=20, bg='light blue', fg='navy',borderwidth = 5)
buttonNext.grid(row=5, column=3)

buttonQuit = Button(root, text = "QUIT", command = root.quit,padx=37,pady=20, bg='light blue', fg='navy',borderwidth = 5)
buttonQuit.grid(row=6, column=3)

global buttonLife1
buttonLife1 = Button(root, text = "\u2764 LIFE \u2764" ,padx=35,pady=20, bg='light blue', fg='red',borderwidth = 5)
buttonLife1.grid(row=6, column=1)

global buttonLife2
buttonLife2 = Button(root, text = "\u2764 LIFE \u2764", padx=35,pady=20, bg='light blue', fg='red',borderwidth = 5)
buttonLife2.grid(row=6,column=2)

#status message area
statusMessage = Label(root, fg = 'navy', textvariable= statusText, bg='light grey')
statusMessage.grid(row=9,column=0,columnspan=2)

# label for score report
showScore = Label(root, textvariable = scoreText)
showScore.grid(row=9, column=3)

# repeat root display until window closes
root.mainloop()
