# importing tkinter for gui
import sys
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, filedialog

# creating window
DataProcessing = tk.Tk()
DataProcessing.configure(bg='#FEDA7C')

# setting window attribute
#DataProcessing.state('zoomed')
#DataProcessing.title("Prediction | Credit Card Eligibility")
DataProcessing.wm_attributes('-fullscreen', 'True')

# window texts
Title = """Predicting Credit Card Eligibility and Credit Limit using Naive Bayes"""
WindowTitle = """Data Processing"""
ProcessingInstructions = """In this module, upload the file containing the data set. Kindly note that said file must be in Comma-separated Values (.csv) file type. These data will undergo 
cleaning and feature selection. Do not forget to set the training and testing sizes."""
UploadText = """File upload:"""
TestSize = """Testing size:"""
TrainSize = """Training size:"""
FeatureSubtitle = """Your eligibility will be determined by the 
following parameters."""

# Select file
def fileNameToEntry():
      files = [('CSV Files', '*.csv')]
      filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File.",
                                          filetypes = files,
                                          defaultextension = files)
      filename = filename.strip()

# User select cancel
      if (len(filename) == 0):
         messagebox.showwarning("Warning", "You must select a file")       
         return
# Selection go to Entry widget
      else:
         myStrVar.set(filename)

# Use esc to exit window
def close(event):
    DataProcessing.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing
DataProcessing.bind('<Escape>', close)

# Proceed on button click
def openNewWindow():
     DataProcessing.destroy()
     import TrainTestResults

tk.Label(DataProcessing, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12 bold',
        text=Title).place(x=50, y=30)

tk.Label(DataProcessing, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 25 bold',
        text=WindowTitle).place(x=50, y=55)

tk.Label(DataProcessing, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12',
        text=ProcessingInstructions).place(x=50, y=108)

tk.Label(DataProcessing, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12',
        text=UploadText).place(x=50, y=175)

UploadButton = tk.Button(DataProcessing, 
                   text="UPLOAD", 
                   fg="#FFF",
                   bg="#E64313",
                   font='Montserrat 10 bold',
                   width=15,
                   border=0,).place(x=170, y=175)

#make global variable to access anywhere
global myStrVar
myStrVar = StringVar()
txtFileName  = tk.Label(DataProcessing, 
                        textvariable = myStrVar, 
                        width = 100, 
                        bg='#FEDA7C',
                        fg='#182C32', 
                        font='Montserrat 11 italic', 
                        anchor="w").place(x=330, y=174)

UploadButton = tk.Button(DataProcessing, 
                text="UPLOAD", 
                fg="#FFF",
                bg="#E64313",
                font='Montserrat 10 bold',
                width=15,
                border=0,
                command = fileNameToEntry).place(x=170, y=175)

tk.Label(DataProcessing, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12',
        text=TrainSize).place(x=50, y=210)

InputTrain = tk.Entry(DataProcessing,
                        justify=tk.CENTER,      
                        #height = 1,
                        width = 13,
                        border=0,
                        font='Montserrat 13',).place(x=170, y=215)

tk.Label(DataProcessing, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 12',
        text=TestSize).place(x=400, y=210)

InputTest = tk.Entry(DataProcessing,
                        justify=tk.CENTER,
                        #height=1,
                        width=13,
                        border=0,
                        font='Montserrat 13').place(x=520, y=215)

GoButton = tk.Button(DataProcessing, 
                text="BEGIN PROCESS", 
                fg="#FFF",
                bg="#E64313",
                font='Montserrat 10 bold',
                width=16,
                border=0).place(x=700, y=214)

# configure style for preview table frame
s = Style()
s.configure('Preview Table.TFrame', background='#FFFFFF') 

PreviewFrame = Frame(DataProcessing, style='Preview Table.TFrame',
                        width=951, 
                        height=430).place(x=50, y=293)

tk.Label(PreviewFrame, 
        justify=tk.CENTER,
        bg='#E64313',
        fg='#FFFFFF',
        width=86,
        font='Montserrat 12 bold',
        text='Preview').place(x=50, y=265)

FeatureFrame = Frame(DataProcessing, style='Preview Table.TFrame',
                        width=300, 
                        height=340).place(x=1025, y=293)

tk.Label(PreviewFrame, 
        justify=tk.CENTER,
        bg='#E64313',
        fg='#FFFFFF',
        width=27,
        font='Montserrat 12 bold',
        text='Features Selected').place(x=1024, y=265)

tk.Label(DataProcessing, 
        justify=tk.LEFT,
        bg='#FEDA7C',
        fg='#182C32',
        font='Montserrat 10',
        text=FeatureSubtitle).place(x=1028, y=635)

ProceedButton = tk.Button(DataProcessing, 
                   text="PROCEED", 
                   fg="#FFF",
                   bg="#182C32",
                   font='Montserrat 13 bold',
                   width=27,
                   border=0,
                   command = openNewWindow).place(x=1029, y=685)

DataProcessing.mainloop()