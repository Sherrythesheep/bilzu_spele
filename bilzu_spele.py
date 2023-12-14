from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox


gameWindow=Tk()
gameWindow.title("Vienādie attēli")
count=0 #cik rutinas atvertas
correctAnswers=0 #skaita pareizās atbildes
answers=[]#saraksts ar atbildem , define tiksu sarakstu un speles laika tas tiek aizpildits
answer_dict={}#kas ur piespiests, salidzinas ar atteliem no saraksta

def btnClick(btn,number):
    global count, correctAnswers, answers, answer_dict
    if btn["image"]=="pyimage6" and count<2:
        btn["image"]=ImageList[number]
        count+=1#viena rūtiņa atklāta
        answers.append(number)#pievieno pie atbildēm
        answer_dict[btn]=ImageList[number]
    if len(answers)==2:#ja atvertas 2 kartites
        if ImageList[answers[0]]==ImageList[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
        if correctAnswers==2:
            messagebox.showinfo("Vienādi attēli", "Esi uzminējis!")
    else: 
        messagebox.showinfo("Vienādi attēli","Neuzminēji!")
        for key in answer_dict:
            key["image"]="pyimage6"
            count=0
            answers=[]
            answer_dict={}
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
btn3=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn2,2))
btn2=Button(width=180,height=180,image=bgImg, command=lambda:btnClick(btn3,3))
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