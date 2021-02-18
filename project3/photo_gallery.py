import tkinter as tk
from tkinter import Label
from tkinter import Button
from PIL import ImageTk, Image

#main screen
screen = tk.Tk()
screen.title('Python Code Course - Photo Gallery')
screen.iconbitmap('C:\\Users\\stace\\OneDrive\\Documents\\python\\2quizBit\\iconImage.ico')
screen.geometry('800x850')

# initialize variables
images = []
count = 0

def load_photos():
    global images
    album = open('C:\\Users\\stace\\OneDrive\\Documents\\python\\3mediaViewer\\photos.txt')
    next_photo = album.readlines()
    next_photo = next_photo[0].split(',')
    for item in next_photo:
        images.append(ImageTk.PhotoImage(Image.open(item)))
    album.close()

def view_next():
    global count
    global images

    if count<len(images)-1:
        count+=1
        photo_label.config(image = images[count])
    else:
        count = 0
        photo_label.config(image = images[count])
    return images

def view_previous():
    global count
    global images

    if count>0:
        count-=1
        photo_label.config(image = images[count])
    else:
        count = len(images)-1
        photo_label.config(image = images[count])
    return images

# function call
load_photos()

#define widgets for the screen
photo_label = Label(image = images[count], width = 800, height = 750)
photo_label.grid(row = 0, column = 0, columnspan = 2)

next_button = Button(screen, text = 'Next', font = ('Arial black', 20), command = view_next)
next_button.grid(row = 1, column = 1)

previous_button = Button(screen, text = 'Previous', font = ('Arial black', 20), command = view_previous)
previous_button.grid(row = 1, column = 0)

screen.mainloop()