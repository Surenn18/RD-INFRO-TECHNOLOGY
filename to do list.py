import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# Add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        task_entry.delete(0, tk.END)
        refresh_tasks()
        save_tasks()

# Delete selected task
def delete_task():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        refresh_tasks()
        save_tasks()

# Mark task as done
def mark_done():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        refresh_tasks()
        save_tasks()

# Refresh the displayed list
def refresh_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["done"] else "❌"
        task_list.insert(tk.END, f"{status} {task['task']}")

# GUI Setup
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")

tasks = load_tasks()

task_entry = tk.Entry(app, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

tk.Button(app, text="Add Task", command=add_task).pack(pady=5)

task_list = tk.Listbox(app, width=45, height=10, font=("Arial", 12))
task_list.pack(pady=10)

tk.Button(app, text="Mark as Done", command=mark_done).pack(pady=5)
tk.Button(app, text="Delete Task", command=delete_task).pack(pady=5)

refresh_tasks()

app.mainloop()
