# importing tkinter for gui
import sys
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# creating window
TTResult = tk.Tk()
TTResult.configure(bg='#FEDA7C')

# setting window attribute
#Splash.state('zoomed')
#Splash.title("Prediction | Credit Card Eligibility")
TTResult.wm_attributes('-fullscreen', 'True')

def close(event):
    TTResult.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing
TTResult.bind('<Escape>', close)

# Proceed on button click
def openNewWindow():
     TTResult.destroy()
     import ModelValidation

# window texts
Title = """Predicting Credit Card Eligibility and Credit Limit using Naive Bayes"""
WindowTitle = """Training and Testing Results"""
TrainTitle = """Training Set"""
TestTitle = """Testing Set"""

tk.Label(TTResult, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text=Title).place(x=50, y=30)

tk.Label(TTResult, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 25 bold',
        text=WindowTitle).place(x=50, y=55)

tk.Label(TTResult, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text=TrainTitle).place(x=50, y=130)

# configure style for preview table frame
s = Style()
s.configure('Training Table.TFrame', background='#FFFFFF') 
s.configure('Testing Table.TFrame', background='#FFFFFF') 

TrainFrame = Frame(TTResult, style='Training Table.TFrame',
                        width=600, 
                        height=450).place(x=50, y=160)

tk.Label(TTResult, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 underline',
        text="Download Training set in .xlsx file.").place(x=50, y=615)

tk.Label(TTResult, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text=TestTitle).place(x=710, y=130)    

TestFrame = Frame(TTResult, style='Testing Table.TFrame',
                        width=600, 
                        height=450).place(x=710, y=160) 

tk.Label(TTResult, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 underline',
        text="Download Testing set in .xlsx file.").place(x=710, y=615)   

ProceedButton = tk.Button(TTResult, 
                   text="PROCEED", 
                   fg="#FFF",
                   bg="#182C32",
                   font='Montserrat 13 bold',
                   width=27,
                   border=0,
                   command=openNewWindow).place(x=500, y=680)

TTResult.mainloop()