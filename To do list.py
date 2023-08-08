import tkinter as tk
from tkinter import messagebox
import tkinter

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","please enter the task")
def delete_task():
    try:
        index=task_list.curselection()
        task_list.delete(index)
    except:
        messagebox.showwarning("warning","please select the tasks to delete")        
    
def clear_task():
    task_list.delete(0,tk.END)
 
# created the main window    
window=tk.Tk()
window.title("To-Do list")   

task_list=tk.Listbox(window)
task_list.pack(pady=5)

# create a task entry
task_entry=tk.Entry(window,font=("lucida",12))
task_entry.pack(pady=5)

# create buttons
add_button=tk.Button(window,text="Add task",command=add_task)
add_button.pack(pady=5,fill=tk.X)

delete_button=tk.Button(window,text="Delete task",command=delete_task)
delete_button.pack(pady=5,fill=tk.X)

clear_task=tk.Button(window,text="Clear task",command=clear_task)
clear_task.pack(pady=5,fill=tk.X)


window.geometry("400x350")

# start the mainloop
window.mainloop()
    