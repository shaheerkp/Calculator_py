from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry('440x530')



textView=Entry(window,width=50,borderwidth=5)
textView.place(x=17,y=10)

global operant
operant=NONE


def buttonPress( text):
    textView.insert(END,text)
    number=textView.get()


def addition():
    first_number=textView.get()
    global operant
    operant="+"
    global number1
    number1=float(first_number)
    textView.delete(0,END)
    print("first number  : "+str(number1))    


def subtraction():
    first_number=textView.get()
    global operant
    operant="-"
    global number2
    number2=float(first_number)
    textView.delete(0,END)
    print("first number  : "+str(number2))    

def multiplication():
    first_number=textView.get()
    global operant
    operant="*"
    global number3
    number3=float(first_number)
    textView.delete(0,END)
    print("first number  : "+str(number3)) 
    
def division():
    first_number=textView.get()
    global operant
    operant="/"
    global number4
    number4=float(first_number)
    textView.delete(0,END)
    print("first number  : "+str(number4))           




def equal():
    
    if(operant=="+"):
        sum=number1+float(textView.get()) 
        textView.delete(0,END)
        textView.insert(0,sum)   
        print(sum)
    elif(operant=="-"):
        dif=number2-float(textView.get())  
        textView.delete(0,END)
        textView.insert(0,dif)
    elif(operant=="*"):
        mul=number3*float(textView.get())  
        textView.delete(0,END)
        textView.insert(0,mul) 
    elif(operant=="/"):
        div=number4/float(textView.get())  
        textView.delete(0,END)
        textView.insert(0,div)    
  
                 
def clear():
    textView.delete(0,END)
    textView.insert(0," ")
    print("cleared")
    number1=0
    operant=""
     


button7      =Button(text="7",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(7)).place(x=17,y=150)
button8      =Button(text="8",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(8)).place(x=120,y=150)
button9      =Button(text="9",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(9)).place(x=225,y=150)
button4      =Button(text="4",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(4)).place(x=17,y=245)
button5      =Button(text="5",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(5)).place(x=120,y=245)
button6      =Button(text="6",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(6)).place(x=225,y=245)
button1      =Button(text="1",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(1)).place(x=17,y=340)
button2      =Button(text="2",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(2)).place(x=120,y=340)
button3      =Button(text="3",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(3)).place(x=225,y=340)
button0      =Button(text="0",width=20,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(0)).place(x=17,y=426)
button_dot   =Button(text=".",width=8,height=3,bg='gray55',activebackground='maroon1',bd=4,command=lambda:buttonPress(".")).place(x=225,y=426)



button_clear =Button(text="CLEAR",width=20,height=3,bg='orange',bd=4,command=clear).place(x=17,y=60)
button_div   =Button(text="/",width=8,height=3,bg='orange',bd=4,command=division).place(x=220,y=60)
button_mul   =Button(text="*",width=8,height=3,bg='orange',bd=4,command=multiplication).place(x=330,y=60)
button_sub   =Button(text="-",width=8,height=3,bg='orange',bd=4,command=subtraction).place(x=330,y=150)
button_add   =Button(text="+",width=8,height=3,bg='orange',bd=4,command=addition).place(x=330,y=245)
button_equal =Button(text="=",width=8,height=8,bg='orange',bd=4,command=equal).place(x=330,y=340)



window.mainloop()