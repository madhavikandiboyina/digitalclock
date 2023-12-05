from tkinter import *
from time import strftime
window = Tk()
window.title("My clock")
window.configure(background="green")
label = Label(window,foreground="blue",background="green")
label.pack()
def clock():
    
    string = strftime("%H:%M:%S %p")
    label.configure(text=string,font=("Arial",125))
    label.after(1000,clock)
clock()

window.mainloop()