from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import time

gameWindow=Tk()
gameWindow.title("Vienādie attēli")
openCardsCount=0 #cik rutinas atvertas
correctAnswers=0 #skaita uzminēto attēlu komplektu skaitu
openCards=[] #saraksts ar atvertajam kartinam (viena vai divas)
answer_dict={} #kas ir piespiests, salidzinas ar atteliem no saraksta

def btnClick(btn,number):
    
    global openCardsCount, openCards, answer_dict, correctAnswers
    
    if btn["image"] == "pyimage6" and openCardsCount < 2:
        btn["image"] = ImageList[number]
        openCardsCount += 1 #viena jauna rūtiņa atklāta
        openCards.append(number) #pievieno kartinas numuru pie atbildēm
        answer_dict[btn]=ImageList[number]
    
    if len(openCards) == 2:#ja atvertas 2 kartites
        
        if ImageList[openCards[0]]==ImageList[openCards[1]]:
            for key in answer_dict:
                key["state"]=DISABLED

            openCards = []
            answer_dict = {}
            openCardsCount = 0
            correctAnswers += 1 #palielinam uzminēto attēlu komplektu skaitu
            messagebox.showinfo("Vienādi attēli", "Esi uzminējis! Kopā uzminēti komplekti: " + str(correctAnswers))
        else :
            Tk.update(btn)
            time.sleep(0.5)
            for key in answer_dict:
                key["image"] = "pyimage6"
            openCardsCount = 0;
            openCards = []
            answer_dict = {}
            #messagebox.showinfo("Vienādi attēli","Neuzminēji!")

    if correctAnswers == 4:
        messagebox.showinfo("Apsveicam!", "Spēle pabeigta")

    return 0


#attēli
myImg1=ImageTk.PhotoImage(Image.open("kakis.jpg").resize((180,180)))
myImg2=ImageTk.PhotoImage(Image.open("pele.jpg").resize((180,180)))
myImg3=ImageTk.PhotoImage(Image.open("ruksis.jpg").resize((180,180)))
myImg4=ImageTk.PhotoImage(Image.open("suns.jpg").resize((180,180)))
myImg5=ImageTk.PhotoImage(Image.open("zirgs.jpg").resize((180,180)))

#fona attels
bgImg=ImageTk.PhotoImage(Image.open("kepa.jpg").resize((180,180)))

btn0=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn0,0))
btn1=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn9,9))

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

#attēlu masīvs
ImageList=[myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5]

#sajauc attēlus
random.shuffle(ImageList)

gameWindow.mainloop()
