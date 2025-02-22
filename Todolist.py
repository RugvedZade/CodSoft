import tkinter as tk
from tkinter import messagebox
import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, start=1):
                task_list.insert(tk.END, f"{i}. {task.strip()}")

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_list.get(0, tk.END)
        for task in tasks:
            file.write(task.split(". ", 1)[1] + "\n")

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, f"{task_list.size() + 1}. {task}")
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        refresh_task_numbers()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def clear_tasks():
    task_list.delete(0, tk.END)
    save_tasks()

def mark_complete():
    try:
        selected_task_index = task_list.curselection()[0]
        task = task_list.get(selected_task_index)
        if not task.startswith("✔ "):
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, f"✔ {task}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete!")

def mark_uncomplete():
    try:
        selected_task_index = task_list.curselection()[0]
        task = task_list.get(selected_task_index)
        if task.startswith("✔ "):
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, task[2:])
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as uncomplete!")

def refresh_task_numbers():
    tasks = task_list.get(0, tk.END)
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{i}. {task.split(". ", 1)[1]}")

# Creating the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Creating UI elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

mark_complete_button = tk.Button(root, text="Mark Complete", command=mark_complete)
mark_complete_button.pack()

mark_uncomplete_button = tk.Button(root, text="Mark Uncomplete", command=mark_uncomplete)
mark_uncomplete_button.pack()

clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.pack()

task_list = tk.Listbox(root, width=50, height=15, bg="#e6e6fa")
task_list.pack(pady=10)

# Load tasks from file
load_tasks()

# Run the application
root.mainloop()