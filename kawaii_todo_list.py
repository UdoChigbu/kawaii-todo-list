import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

FILENAME = "tasks.txt"

tasks = []

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                text, checked = line.strip().rsplit("||", 1)
                add_task_ui(text, bool(int(checked)))

def save_tasks():
    with open(FILENAME, "w") as f:
        for task_text, var in tasks:
            f.write(f"{task_text}||{int(var.get())}\n")

def add_task():
    task = task_entry.get().strip()
    if task:
        add_task_ui(f"🌸 {task}")
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Oops!", "Please enter a task, cutie! 💕")

def add_task_ui(task_text, checked=False):
    var = tk.IntVar(value=1 if checked else 0)
    checkbox = tk.Checkbutton(task_frame, text=task_text, variable=var, font=font_main, bg="#fff9fb", anchor="w")
    checkbox.pack(fill="x", pady=2, padx=10)
    tasks.append((task_text, var))

def delete_checked_tasks():
    global tasks
    new_tasks = []
    for widget, (text, var) in zip(task_frame.winfo_children(), tasks):
        if var.get():
            widget.destroy()
        else:
            new_tasks.append((text, var))
    tasks = new_tasks
    save_tasks()

# Main window
root = tk.Tk()
root.title("🌈 Kawaii To-Do List 💖")
root.geometry("430x500")
root.resizable(False, False)

# Background
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((430, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Fonts and colors
font_main = ("Comic Sans MS", 12)
button_font = ("Comic Sans MS", 11)
entry_bg = "#fff0f5"
button_color = "#ffd6ec"
listbox_bg = "#fff9fb"

# Entry
task_entry = tk.Entry(root, font=font_main, width=25, bg=entry_bg, bd=2, relief="groove")
task_entry.place(x=80, y=40)

# Buttons
add_button = tk.Button(root, text="✨ Add Task", font=button_font, bg=button_color, fg="#555",
                       relief="ridge", bd=3, command=add_task)
add_button.place(x=150, y=80)

delete_button = tk.Button(root, text="🧹 Delete Checked", font=button_font, bg=button_color, fg="#555",
                          relief="ridge", bd=3, command=delete_checked_tasks)
delete_button.place(x=140, y=120)

# Task container
task_frame = tk.Frame(root, bg=listbox_bg, bd=2, relief="sunken")
task_frame.place(x=30, y=160, width=370, height=270)

# Footer
footer = tk.Label(root, text="💫 Stay organized, sweetie! 💫", font=("Comic Sans MS", 10), bg="#fff0f0", fg="#a66aa1")
footer.place(x=110, y=455)

# Load saved tasks
load_tasks()

root.mainloop()
