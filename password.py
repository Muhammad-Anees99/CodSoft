import random
import string
from tkinter import *
from tkinter import messagebox
def reset_btn():
    global password
    r=messagebox.askquestion("Alert","Do You want to Reset Password")
    if r:
        password=''
        label_password.config(text=password,font=("Times",16),width=30,borderwidth=bw,relief=RAISED)
    else:
        exit
def saved():
    messagebox.showinfo("Info","Your Password saved")
def generate_password():
    global password,entry_length
    length = (entry_length.get())

    if (length):
        length = int(entry_length.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        label_password.config(text= password,font=("Times",16),width=30,borderwidth=bw,relief=RAISED)
    else:
        messagebox.showwarning("Alert","Please Enter Password Length")

win = Tk()
global entry_length
width=1366
height=768
bw=8
clr="black"
fc="white"
win.title("Password Generator")
win.geometry("%dx%d" % (width, height))
win.configure(background="black")
# Create label and entry for password length
Top_Label= Label(win,text="Password Generator",fg=fc,font = ("Times", 45),bg=clr)
Top_Label.place(x=480,y=120)
user=Label(win,text="User Name",font=("Times",18),bg=clr,fg=fc)
user.place(x=430,y=270)
user_entry=Entry(win,font=("Times",16),width=33,borderwidth=bw,relief=RAISED)
user_entry.place(x=670,y=270)
label_length = Label(win, text="Password Length:",font=("Times",18),bg=clr,fg=fc)
label_length.place(x=430,y=330)
entry_length = Entry(win,font=("Times",16),width=33,borderwidth=bw,relief=RAISED)
entry_length.place(x=670,y=330)
btn_generate = Button(win, text="Generate", command=generate_password,font=("Times",16),width=20)
btn_generate.place(x=740,y=450)
gen_lab=Label(win,text="Generated Password",font=("Times",18),bg=clr,fg=fc)
gen_lab.place(x=430,y=390)
label_password = Label(win)
label_password.place(x=670,y=390)
reset=Button(win,text="Reset",command=reset_btn,font=("Times",16),width=20)
reset.place(x=740,y=510)
save=Button(win,text="Save",font=("Times",16),width=20,command=saved)
save.place(x=740,y=570)
win.mainloop()