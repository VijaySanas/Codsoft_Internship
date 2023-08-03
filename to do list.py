import tkinter
import tkinter.messagebox
from tkinter import font

root = tkinter.Tk()
root.title("To Do List by Vijay")
root.configure(bg='#00FFFF')

label_font = font.Font(size=24,slant="italic")

label = tkinter.Label(root, text="--- TO DO LIST ---",bg='#00FFFF', font=label_font)
label.pack()

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
    
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=7, width=30, font=2)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, borderwidth=10, width=30, font=2)
entry_task.pack(ipady=2)

button_add_task = tkinter.Button(root, text="Add Items", width=32, command=add_task, font="bold 15")
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete Item", width=32, command=delete_task, font="bold 15")
button_delete_task.pack()

root.mainloop()
