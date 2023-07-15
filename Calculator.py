from tkinter import *
from math import*
win=Tk()
width=1366
height=768
global subtract,addition,multiply,division,squareroot
win.geometry("%dx%d" % (width, height))
win.title("My Calculator")
frame1=Frame(win)
global v,result
v=StringVar()
addition=False
subtract=False
multiply=False
division=False
squareroot=False
def button_click(n):
    global v
    p=v.get()
    m=p+str(n)
    v.set(str(m))
def button_clear():
    global v
    v.set('')
def button_add():
    global first,v,addition
    first=int(v.get())
    v.set('')
    addition=True

def button_sub():
    global subtract,first,v,addition
    first=int(v.get())
    v.set('')
    subtract=True
def button_mul():
    global first,v,multiply
    first=int(v.get())
    v.set('')
    multiply=True
def divide():
    global first,v,division
    first=int(v.get())
    v.set('')
    division=True
def square_root():
    global first,v,squareroot
    first=int(v.get())
    squareroot=True
def button_result():
    global subtract,addition,multiply,division,squareroot
    if addition:
        second=int(v.get())
        result=first+second
        v.set(str(result))
        addition=False
        # exit
    elif subtract:
        second=int(v.get())
        result=first-second
        v.set(str(result))
        subtract=False
        # exit
    elif multiply:
        second=int(v.get())
        result=first*second
        v.set(str(result))
        multiply=False
        # exit
    elif division:
        second=int(v.get())
        result=(first/second)
        v.set(str(result))
        division=False
    elif squareroot:
        result=sqrt(first)
        v.set(str(result))
        squareroot=False
        # exit

bg_image = PhotoImage(file="bg23.png")
canvas = Canvas(win, width=width, height=height)
canvas.pack()
canvas.create_image(0, 0, image=bg_image, anchor=NW)
plx,ply=190,270
dis_x=200
dis_y=100
bw=10
clr="black"
txtclr="white"
e=Label(win,width=75,height=4,textvariable=v,borderwidth=bw,relief=RAISED,bg=clr,fg=txtclr,font = ("Times", 16))
e.place(x=195,y=140)
b1=Button(win,text='1',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(1),fg=txtclr,font = ("Times", 16))
b1.place(x=plx,y=ply)
b2=Button(win,text='2',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(2),fg=txtclr,font = ("Times", 16))
b2.place(x=plx+dis_x,y=ply)
b3=Button(win,text='3',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(3),fg=txtclr,font = ("Times", 16))
b3.place(x=plx+dis_x+dis_x,y=ply)

b4=Button(win,text='4',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(4),fg=txtclr,font = ("Times", 16))
b4.place(x=plx+dis_x+dis_x+dis_x,y=ply)
b5=Button(win,text='5',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(5),fg=txtclr,font = ("Times", 16))
b5.place(x=plx+dis_x+dis_x+dis_x+dis_x,y=ply)
b6=Button(win,text='6',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(6),fg=txtclr,font = ("Times", 16))
b6.place(x=plx,y=ply+dis_y)

b7=Button(win,text='7',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(7),fg=txtclr,font = ("Times", 16))
b7.place(x=plx+dis_x,y=ply+dis_y)
b8=Button(win,text='8',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(8),fg=txtclr,font = ("Times", 16))
b8.place(x=plx+dis_x+dis_x,y=ply+dis_y)
b9=Button(win,text='9',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(9),fg=txtclr,font = ("Times", 16))
b9.place(x=plx+dis_x+dis_x+dis_x,y=ply+dis_y)

b0=Button(win,text='0',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click(0),fg=txtclr,font = ("Times", 16))
b0.place(x=plx+dis_x+dis_x+dis_x+dis_x,y=ply+dis_y)

b10=Button(win,text="\u002B",padx=40,pady=20,height=5,borderwidth=bw+2,relief=RAISED,bg=clr,command=button_add,fg=txtclr,font = ("Times", 16))
b10.place(x=plx+dis_x+dis_x+dis_x+dis_x,y=ply+dis_y+dis_y)
b11=Button(win,text="=",padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=button_result,fg=txtclr,font = ("Times", 16))
b11.place(x=plx+dis_x,y=ply+dis_y+dis_y)

sub=Button(win,text="\u2212",padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=button_sub,fg=txtclr,font = ("Times", 16))
sub.place(x=plx+dis_x+dis_x,y=ply+dis_y+dis_y)

mul=Button(win,text='\u00D7',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=button_mul,fg=txtclr,font = ("Times", 16))
mul.place(x=plx+dis_x+dis_x+dis_x,y=ply+dis_y+dis_y)

div=Button(win,text='\u00F7',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=divide,fg=txtclr,font = ("Times", 16))
div.place(x=plx,y=ply+dis_y+dis_y+dis_y)

percent=Button(win,text='\u221A',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=square_root,fg=txtclr,font = ("Times", 16))
percent.place(x=plx+dis_x,y=ply+dis_y+dis_y+dis_y)

b12=Button(win,text='C',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=button_clear,fg=txtclr,font = ("Times", 16))
b12.place(x=plx+dis_x+dis_x,y=ply+dis_y+dis_y+dis_y)
b13=Button(win,text='.',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=lambda : button_click('.'),fg=txtclr,font = ("Times", 16))
b13.place(x=plx,y=ply+dis_y+dis_y)

b15=Button(win,text='OFF',padx=40,pady=20,borderwidth=bw,relief=RAISED,bg=clr,command=win.destroy,fg=txtclr,font = ("Times", 9),height=2)
b15.place(x=plx+dis_x+dis_x+dis_x,y=ply+dis_y+dis_y+dis_y)
win.mainloop()