# importing tkinter for gui
import sys
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from matplotlib.pyplot import fill
import time

# creating window
Splash = tk.Tk()
Splash.configure(bg='#7EB7AA')

# setting window attribute
#Splash.state('zoomed')
#Splash.title("Prediction | Credit Card Eligibility")
Splash.wm_attributes('-fullscreen', 'True')

def close(event):
    Splash.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

Splash.bind('<Escape>', close)

# splash title
SplashTitle = """Predicting Credit Card Eligibility and Credit Limit
using Naive Bayes"""

# member List
SplashMembers = """Balita, Maria Sophia G.
Cailing, Hannah A.
Santiago, Jeremy Karl C."""

tk.Label(Splash, 
        justify=tk.LEFT,
        bg='#7EB7AA',
        fg='#182C32',
        font='Montserrat 25 bold',
        text=SplashTitle).place(x=100, y=200)

tk.Label(Splash,
        justify=tk.LEFT,
        bg='#7EB7AA',
        fg='#182C32',
        font='Montserrat 15',
        text=SplashMembers).place(x=100, y=370)

style = Style()
style.theme_use('alt') 
# Self test for each subject,'winnative','clam','alt','default','classic' Test successful. 
# windows theme:('winnative','clam','alt','default','classic','vista','xpnative')

style.configure("1.Horizontal.TProgressbar", troughcolor ='#7EB7AA', background='#182C32', thickness=25) 

progress = Progressbar(Splash, style="1.Horizontal.TProgressbar", orient = HORIZONTAL, 
                          length=1150, mode = 'determinate')
progress.pack(side=BOTTOM, pady=100)

progress['maximum']=50       
for i in range(51):
        time.sleep(0.05)
        progress['value'] = i
        progress.update()
if progress['value']==50:
    print("close window")
    Splash.destroy()
    import DataProcessing
    DataProcessing.mainloop()