from tkinter import *
import random
import pyperclip 

root = Tk()
root.title("Password Generator by Vijay")

bg = PhotoImage(file = "C:\\Users\\Vijay\\OneDrive\\Pictures\\cs glitch.gif")

entry = Entry(borderwidth=3, width=36)

passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    password = ""

    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
    
def e1_delete():
	e1.delete(0, END)
        
def e2_delete():
    e2.delete(0, END)

label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

label2 = Label(root, text="* Password Generator Application *", font="calibri 20 bold")
label2.pack(pady=20)

label3 = Label(root, text="Enter Password Length", font="calibri 15", width=29,height=1)
label3.pack(ipadx=40, pady=5)

e1 = Entry(root, textvariable=passlen, borderwidth=5, width=40)
e1.pack(ipadx=40, pady=5)

Button(root, text="G E N E R A T E   P A S S W O R D", command=generate, font="calibri 10 bold", width=40,height=1).pack(ipadx=40, pady=5)

e2 = Entry(root, textvariable=passstr, borderwidth=5, width=40)
e2.pack(ipadx=40, pady=5)

Button(root, text="C O P Y", command=copytoclipboard, font="calibri 10 bold", width=40,height=1).pack(ipadx=40, pady=5)

B = Button(root, text="R E S E T", command=lambda: [e1_delete(), e2_delete()], font="calibri 10 bold", width=40, height=1)
B.pack(ipadx=40, pady=5)

root.mainloop()
