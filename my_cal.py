from tkinter import *
import pyttsx3


win = Tk()
win.title("Calculator")
win.resizable(width=False,height=False)
win.geometry("296x435")
oprator = ''
num_input = StringVar()
txtDisp = Entry(win,textvariable=num_input,bd=20,insertwidth=4,bg="powder blue",font=10).grid(columnspan=3)


def btnClick(number):
    global oprator
    oprator = oprator + str(number)
    num_input.set(oprator)
def btnclear():
    global oprator
    oprator = ""
    num_input.set("")
def btnEquals():
    global oprator
    sumup = float(eval(oprator))
    num_input.set(sumup)

    voice = pyttsx3.init()
    voice.setProperty("s_V",20)

    voice.say(oprator)
    voice.runAndWait()

    oprator = ""
    Equals = " Equal "
    
    voice.say(Equals)
    voice.runAndWait()
    voice.say(sumup)
    voice.runAndWait()
def btn(text,x,y):
    Button(win,padx=20,pady=20,bd=7,fg="black",bg="powder blue",text=text,command=lambda:btnClick(text),font=25).grid(row=x,column=y)
def btn2(text,command,x,y):
    Button(win,padx=20,pady=20,bd=7,fg="black",bg="powder blue",text=text,command=command,font=10).grid(row=x,column=y)



btn(7,1,0)
btn(8,1,1)
btn(9,1,2)
btn("+",1,4)
btn("-",2,4)
btn("/",3,4)
btn("*",4,4)
#btn("**",5,0)
btn(".",4,1)
btn(4,2,0)
btn(5,2,1)
btn(6,2,2)
btn(1,3,0)
btn(2,3,1)
btn(3,3,2)
btn(0,4,0)
btn2("C",btnclear,0,4)
btn2("=",btnEquals,4,2)


#btn_C = Button(win,padx=20,pady=20,bd=7,fg="black",bg="powder blue",text="C",command=btnclear,font=10).grid(row=0,column=4)
#btn_eq = Button(win,padx=20,pady=20,bd=7,fg="black",bg="powder blue",text="=",command=btnEquals,font=10).grid(row=4,column=2)
#btn_cr =Button(win,padx=100,pady=20,bd=7,fg="black",bg="powder blue",text="CR",command=lambda:btnClick("Credit  ,  Ali Shakiba "),font=25)
#btn_cr.place(x=28,y=400)
lab_cr = Label(win,text="Credit  ,  Ali Shakiba ",fg="black",bg="powder blue",font=30)
lab_cr.place(x=75,y=405)

win.mainloop()
