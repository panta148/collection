from tkinter import *


def button_clear():
    global calculation
    calculation=" "
    text.set(" ")


def button_backspace():
    global calculation
    lastindex=len(calculation)-1
    calculation=calculation[:lastindex]
    text.set(calculation)


def button_click(number):
    global calculation
    calculation=calculation+str(number)
    text.set(calculation)




def button_equal():
    global calculation
    try:
        result=str(eval(calculation))
        text.set(result)
        calculation=""
    except:
        text.set("ERROR")
        calculation=" " 





root=Tk()
root.title("Simple calculator")
root.resizable(0,0)
root.geometry('300x450')
text=StringVar() #it is the text which is seen on the black screen
calculation=''#it is for the calculation
label=Label(root,text="A",font="Arial 10",bg="black",fg="black")
label.pack(expand=True,fill="both")
label=Label(root,text="label",anchor=SE,font="Arial 20",textvariable=text,bg="black",fg="white")
print(text)
label.pack(expand=True,fill="both")
# row 1-5
row1=Frame(root)
row1.pack(expand=True,fill="both")
row2=Frame(root)
row2.pack(expand=True,fill="both")
row3=Frame(root)
row3.pack(expand=True,fill="both")
row4=Frame(root)
row4.pack(expand=True,fill="both")
row5=Frame(root)
row5.pack(expand=True,fill="both")
# row1
button_clear=Button(row1,text="C",font="Arial 26",command=button_clear,bg="#d1d1d1",border=0)
button_clear.pack(side=LEFT,expand=True,fill="both")
button_backspace=Button(row1,text="CE",font="Arial 26",command=button_backspace,bg="#d1d1d1",border=0)
button_backspace.pack(side=LEFT,expand=True,fill="both")
button_modulus=Button(row1,text="%",font="Arial 26",command=lambda:button_click("%"),bg="#d1d1d1",border=0)
button_modulus.pack(side=LEFT,expand=True,fill="both")
button_divide=Button(row1,text="/",font="Arial 42",command=lambda:button_click("/"),bg="#ff8000",fg="white",border=0)
button_divide.pack(side=LEFT,expand=True,fill="both")
# row2
button7=Button(row2,text="7",font="Arial 26",command=lambda:button_click(7),activebackground="#d1d1d1",border=0)
button7.pack(side=LEFT,expand=True,fill="both")
button8=Button(row2,text="8",font="Arial 26",command=lambda:button_click(8),activebackground="#d1d1d1",border=0)
button8.pack(side=LEFT,expand=True,fill="both")
button9=Button(row2,text="9",font="Arial 26",command=lambda:button_click(9),activebackground="#d1d1d1",border=0)
button9.pack(side=LEFT,expand=True,fill="both")
button_multiply=Button(row2,text="*",font="Arial 29",command=lambda:button_click("*"),bg="#ff8000",fg="white",border=0)
button_multiply.pack(side=LEFT,expand=True,fill="both")
#row3
button4=Button(row3,text="4",font="Arial 26",command=lambda:button_click(4),activebackground="#d1d1d1",border=0)
button4.pack(side=LEFT,expand=True,fill="both")
button5=Button(row3,text="5",font="Arial 26",command=lambda:button_click(5),activebackground="#d1d1d1",border=0)
button5.pack(side=LEFT,expand=True,fill="both")
button6=Button(row3,text="6",font="Arial 26",command=lambda:button_click(6),activebackground="#d1d1d1",border=0)
button6.pack(side=LEFT,expand=True,fill="both")
buttomn_subtract=Button(row3,text="-",font="Arial 31",command=lambda:button_click("-"),bg="#ff8000",fg="white",border=0)
buttomn_subtract.pack(side=LEFT,expand=True,fill="both")
# row4
button1=Button(row4,text="1",font="Arial 26",command=lambda:button_click(1),activebackground="#d1d1d1",border=0)
button1.pack(side=LEFT,expand=True,fill="both")
button2=Button(row4,text="2",font="Arial 26",command=lambda:button_click(2),activebackground="#d1d1d1",border=0)
button2.pack(side=LEFT,expand=True,fill="both")
button3=Button(row4,text="3",font="Arial 26",command=lambda:button_click(3),activebackground="#d1d1d1",border=0)
button3.pack(side=LEFT,expand=True,fill="both")
button_add=Button(row4,text="+",font="Arial 26",command=lambda:button_click("+"),bg="#ff8000",fg="white",border=0)
button_add.pack(side=LEFT,expand=True,fill="both")
#row5
button_point=Button(row5,text=".",font="Arial 26",command=lambda:button_click("."),activebackground="#d1d1d1",border=0)
button_point.pack(side=LEFT,expand=True,fill="both")
button0=Button(row5,text="0",font="Arial 26",command=lambda:button_click(0),activebackground="#d1d1d1",border=0)
button0.pack(side=LEFT,expand=True,fill="both")
button_equal=Button(row5,text="=",font="Arial 26",command=button_equal,activebackground="#d1d1d1",border=0)
button_equal.pack(side=LEFT,expand=True,fill="both")
button_square=Button(row5,text="^",font="Arial 26",command=lambda:button_click("^"),bg="#ff8000",fg="white",border=0)
button_square.pack(side=LEFT,expand=True,fill="both")
root.mainloop()