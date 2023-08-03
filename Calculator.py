import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math

window = tk.Tk()
window.title('Calculator by Vijay')

frame = tk.Frame(master=window, padx=10, bg='black')
frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=36)
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=15)

def myclick(number):
	entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")
		
def undo():
    entire_string = entry.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear()
        entry.insert(0,new_string)
    else:
        clear()
        entry.insert(0,"Error")

def squared():
        entry.result = False
        entry.current = math.sqrt(float(entry.get()))
        entry.display(entry.current)

def clear():
	entry.delete(0, tk.END)
	
button_1 = tk.Button(master=frame, text="C",fg='white', bg='red', padx=15, pady=5, height=2, width=1, command=clear, font='bold')
button_1.grid(row=1, column=0, pady=2)

button_2 = tk.Button(master=frame, text='%',bg='black', fg='white', padx=15, pady=5, height=2, width=1, command=lambda: myclick('%'), font='bold')
button_2.grid(row=1, column=1, pady=2)

button_3 = tk.Button(master=frame, text='<−',fg='white',bg='black', padx=15, pady=5, height=2, width=1, command=undo, font='bold')
button_3.grid(row=1, column=2, pady=2)

button_4 = tk.Button(master=frame, text="/",fg='orange',bg='black', padx=15, pady=5, height=2, width=1, command=lambda: myclick('/'), font='bold')
button_4.grid(row=1, column=3, pady=2)

button_5 = tk.Button(master=frame, text='7', bg='black', fg='white', padx=15, pady=5, height=2, width=1, command=lambda: myclick('7'), font='bold')
button_5.grid(row=2, column=0, pady=2)

button_6 = tk.Button(master=frame, text='8', bg='black', fg='white', padx=15, pady=5, height=2, width=1, command=lambda: myclick('8'), font='bold')
button_6.grid(row=2, column=1, pady=2)

button_7 = tk.Button(master=frame, text='9', bg='black', fg='white', padx=15, pady=5, height=2, width=1, command=lambda: myclick('9'), font='bold')
button_7.grid(row=2, column=2, pady=2)

button_8 = tk.Button(master=frame, text='x',fg='orange',bg='black', padx=15, pady=5, height=2, width=1, command=lambda: myclick('*'), font='bold')
button_8.grid(row=2, column=3, pady=2)

button_9 = tk.Button(master=frame, text='4', bg='black', fg='white' , padx=15, pady=5, height=2, width=1, command=lambda: myclick('4'), font='bold')
button_9.grid(row=3, column=0, pady=2)

button_10 = tk.Button(master=frame, text='5', bg='black', fg='white' , padx=15, pady=5, height=2, width=1, command=lambda: myclick('5'), font='bold')
button_10.grid(row=3, column=1, pady=2)

button_11 = tk.Button(master=frame, text="6", bg='black', fg='white' , padx=15, pady=5, height=2, width=1, command=lambda: myclick('6'), font='bold')
button_11.grid(row=3, column=2, pady=2)

button_12 = tk.Button(master=frame, text="−",fg='orange',bg='black', padx=15, pady=5, height=2, width=1, command=lambda: myclick('-'), font='bold')
button_12.grid(row=3, column=3, pady=2)

button_13 = tk.Button(master=frame, text="1", bg='black', fg='white' , padx=15, pady=5, height=2, width=1, command=lambda: myclick('1'), font='bold')
button_13.grid(row=4, column=0, pady=2)

button_14 = tk.Button(master=frame, text="2", bg='black', fg='white' , padx=15, pady=5, height=2, width=1, command=lambda: myclick('2'), font='bold')
button_14.grid(row=4, column=1, pady=2)

button_15 = tk.Button(master=frame, text="3", bg='black', fg='white' , padx=15, pady=5, height=2, width=1, command=lambda: myclick('3'), font='bold')
button_15.grid(row=4, column=2, pady=2)

button_16 = tk.Button(master=frame, text="+",fg='orange',bg='black', padx=15, pady=5, height=2, width=1, command=lambda: myclick('+'), font='bold')
button_16.grid(row= 4, column=3, pady=2)

button_17 = tk.Button(master=frame, text="00", bg='black', fg='white', padx=15, pady=5, height=2, width=1, command=lambda: myclick('00'), font='bold')
button_17.grid(row=5, column=0, pady=2)

button_18 = tk.Button(master=frame, text="0", bg='black', fg='white', padx=15, pady=5, height=2, width=1, command=lambda: myclick('0'), font='bold')
button_18.grid(row=5, column=1, pady=2)

button_19 = tk.Button(master=frame, text="•", bg='black', fg='white' , padx=15, pady=5, height=2, width=1, command=lambda: myclick('.'), font='bold')
button_19.grid(row=5, column=2, pady=2)

button_20 = tk.Button(master=frame, text="=",fg='white', bg='orange', padx=15, pady=5, height=2, width=1, command=equal, font='bold')
button_20.grid(row=5, column=3, pady=2)

window.mainloop()
