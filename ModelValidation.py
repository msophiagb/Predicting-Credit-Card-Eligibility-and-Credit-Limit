# importing tkinter for gui
import sys
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image


from matplotlib.pyplot import fill

# creating window
ModelValidation = tk.Tk()
ModelValidation.configure(bg='#FEDA7C')

# setting window attribute
#ModelValidation.state('zoomed')
#ModelValidation.title("Prediction | Credit Card Eligibility")
ModelValidation.wm_attributes('-fullscreen', 'True')

# window texts
Title = """Predicting Credit Card Eligibility and Credit Limit using Naive Bayes"""
WindowTitle = """Model Validation"""
ValidationSubtitle = """In this module, model outputs are (systematically) compared to independent real-world observations to judge the quantitative and 
qualitative correspondence with reality. Kindly input values below to see your predicted eligibility status and credit limit."""

# Use esc to exit window
def close(event):
    ModelValidation.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing
ModelValidation.bind('<Escape>', close)

# Proceed on button click
def openNewWindow():
     ModelValidation.destroy()
     import DataProcessing

tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text=Title).place(x=50, y=30)

tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 25 bold',
        text=WindowTitle).place(x=50, y=55)

tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12',
        text=ValidationSubtitle).place(x=50, y=108)

tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text="Monthly Gross Income").place(x=50, y=185)

InputIncome = tk.Entry(ModelValidation,
                        justify=tk.RIGHT,      
                        #height = 1,
                        width = 20,
                        border=0,
                        font='Montserrat 13',).place(x=55, y=218)

tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text="Total Good Debt").place(x=50, y=255)

InputGoodDebt = tk.Entry(ModelValidation,
                        justify=tk.RIGHT,      
                        #height = 1,
                        width = 20,
                        border=0,
                        font='Montserrat 13',).place(x=55, y=288)

tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text="Total Bad Debt").place(x=50, y=328)

InputBadDebt = tk.Entry(ModelValidation,
                        justify=tk.RIGHT,      
                        #height = 1,
                        width = 20,
                        border=0,
                        font='Montserrat 13',).place(x=55, y=361)

PredictButton = tk.Button(ModelValidation,
                text="PREDICT", 
                fg="#FFF",
                bg="#E64313",
                font='Montserrat 11 bold',
                width=22,
                border=0).place(x=54, y=413)


tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 15 bold',
        text="Predicted Eligibility Status").place(x=54, y=480)

PredictedStatus = tk.Entry(ModelValidation,
                        justify=tk.CENTER,      
                        #height = 1,
                        width = 22,
                        border=0,
                        font='Montserrat 14',
                        state='disabled').place(x=54, y=515)

tk.Label(ModelValidation, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 15 bold',
        text="Predicted Credit Limit").place(x=54, y=550)

PredictedLimit = tk.Entry(ModelValidation,
                        justify=tk.CENTER,      
                        #height = 1,
                        width = 22,
                        border=0,
                        font='Montserrat 14',
                        state='disabled').place(x=54, y=585)

# Configure style for preview table frame
s = Style()
s.configure('Guide Table.TFrame', background='#7EB7AA') 

GuideFrame = Frame(ModelValidation, style='Guide Table.TFrame',
                        width=900, 
                        height=500).place(x=375, y=190)

ModelValidation.mainloop()