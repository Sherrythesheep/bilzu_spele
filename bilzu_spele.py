from tkinter import*
from PIL import ImageTk, Image
#import random
#from tkinter import messagebox
gameWindow=Tk()
gameWindow.title("Vienādie attēli")

myImg1=ImageTk.PhotoImage(Image.open("kakis.jpg"))
myImg2=ImageTk.PhotoImage(Image.open("pele.jpg"))
myImg3=ImageTk.PhotoImage(Image.open("ruksis.jpg"))
myImg4=ImageTk.PhotoImage(Image.open("suns.jpg"))
myImg5=ImageTk.PhotoImage(Image.open("zirgs.jpg"))

#fona attels
bgImg=ImageTk.PhotoImage(Image.open("kakis.jpg"))
bgImg=ImageTk.PhotoImage(Image.open("pele.jpg"))
bgImg=ImageTk.PhotoImage(Image.open("ruksis.jpg"))
bgImg=ImageTk.PhotoImage(Image.open("suns.jpg"))
bgImg=ImageTk.PhotoImage(Image.open("zirgs.jpg"))

btn0=Button(width=10,height=10,Image=bgImg)
btn1=Button(width=10,height=10,Image=bgImg)
btn2=Button(width=10,height=10,Image=bgImg)
btn4=Button(width=10,height=10,Image=bgImg)
btn5=Button(width=10,height=10,Image=bgImg)
btn6=Button(width=10,height=10,Image=bgImg)
btn7=Button(width=10,height=10,Image=bgImg)
btn8=Button(width=10,height=10,Image=bgImg)
btn9=Button(width=10,height=10,Image=bgImg)

btn0=Button(width=10,height=10)
btn1=Button(width=10,height=10)
btn2=Button(width=10,height=10)
btn3=Button(width=10,height=10)
btn4=Button(width=10,height=10)
btn5=Button(width=10,height=10)
btn6=Button(width=10,height=10)
btn7=Button(width=10,height=10)
btn8=Button(width=10,height=10)
btn9=Button(width=10,height=10)

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