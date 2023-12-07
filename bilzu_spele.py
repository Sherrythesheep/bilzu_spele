from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox
gameWindow=Tk()
gameWindow.title("Vienādie attēli")

btn0=Button(width=4,height=4)
btn1=Button(width=4,height=4)
btn2=Button(width=4,height=4)
btn3=Button(width=4,height=4)
btn4=Button(width=4,height=4)
btn5=Button(width=4,height=4)
btn6=Button(width=4,height=4)
btn7=Button(width=4,height=4)
btn8=Button(width=4,height=4)
btn9=Button(width=4,height=4)

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=1, column=2)
btn6.grid(row=2, column=0)
btn7.grid(row=2, column=1)
btn8.grid(row=2, column=2)
btn9.grid(row=0, column=0)

gameWindow.mainloop()