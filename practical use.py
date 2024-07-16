import random
import time
import os
import pyautogui
import PIL
import pyscreeze
import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime

# thanks to geeksforgeeks for this code, im still unsure on tkinter stuff!!
import tkinter 

# Create the default window 
root = tkinter.Tk() 
root.title("What to open.") 
root.geometry('700x500') 

# Create the list of options 
options_list = ["Chrome", "Spotify", "Microsoft Edge", "File Explorer"] 

# Variable to keep track of the option 
# selected in OptionMenu 
value_inside = tkinter.StringVar(root) 

# Set the default value of the variable 
value_inside.set("Chrome") 

# Create the optionmenu widget and passing 
# the options_list and value_inside to it. 
question_menu = tkinter.OptionMenu(root, value_inside, *options_list) 
question_menu.pack() 

# print out what was chosen

def whatSel():
    inputText=format(value_inside.get())
    print('You have selected:',inputText)

# Submit button, on click, basically just submits it (not that hard)
submit_button = tkinter.Button(root, text='Submit', command=whatSel) 
submit_button.pack() 

root.mainloop() 

time.sleep(3)
into=[]
prompts=["Explain the theory of relativity in simple terms.","What are some healthy breakfast ideas?","Recommend a good book for someone who loves mystery novels.",'What are some must-watch movies from the 1990s?',"What are some tips for effective public speaking?"]
genres=['POV: Indie', 'Rock', '90s', '80s', 'Bears In Trees']
pyautogui.press('win')
for i in format(value_inside.get()):
    time.sleep(.1)
    pyautogui.write(i)
pyautogui.press('enter')
time.sleep(1)
if format(value_inside.get()) == "Chrome":
    time.sleep(1)
    pyautogui.press('/')
    pyautogui.write("chatgpt")
    pyautogui.press('enter')
    time.sleep(5)
    print(len(prompts))
    pyautogui.write(prompts[random.randint(0,len(prompts)-1)],interval=.1)
    pyautogui.press('enter')
elif format(value_inside.get()) == "Spotify":
    time.sleep(5)
    pyautogui.press('f11')
    pyautogui.write(genres[random.randint(0,len(genres)-1)])
    pyautogui.press('enter')
elif format(value_inside.get()) == "Microsoft Edge":
    time.sleep(5)
    pyautogui.hotkey('ctrl','w')
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write("Chrome")
    time.sleep(5)
    pyautogui.write("How to delete microsoft edge from my PC",interval=.1)