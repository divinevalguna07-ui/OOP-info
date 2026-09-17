import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Student Management System")
root.geometry("700x500")
root.configure(bg="#F2D9B3")

BG_COLOR = "#F2D9B3"
TITLE_COLOR = "#EC790E"
LABEL_COLOR = "#0E4950"
ENTRY_BG = "#B6F2D1"
ADD_COLOR = "#146D78"
UPDATE_COLOR = "#CF6D9C"
DELETE_COLOR = "#D57E67"
CLEAR_COLOR = "#357544"

BUTTON_TEXT = "white"

#Title
title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 18,"bold"),
    bg=BG_COLOR,
    fg=TITLE_COLOR
)

title_label.pack(pady=10)

#Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

#Name
tk.Label(
    input_frame,
    text="Name:",
    font=("Arial", 11, "bold"),
    bg="white",
    fg=LABEL_COLOR
).grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

#Age
tk.Label(
    input_frame,
    text="Age:",
    font=("Arial", 11, "bold"),
    bg="white",
    fg=LABEL_COLOR
).grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=1, column=1, padx=5, pady=5)

#Course
tk.Label(
    input_frame,
    text="Course:",
    font=("Arial", 11, "bold"),
    bg="white",
    fg=LABEL_COLOR
).grid(row=2, column=0, padx=5, pady=5)
course_entry = tk.Entry(input_frame, width=30)
course_entry.grid(row=2, column=1, padx=5, pady=5)

#Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add",
    width=10,
    font=("Arial", 11, "bold"),
    bg=ADD_COLOR,
    fg=BUTTON_TEXT,
    command="add_student"
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update",
    width=10,
    font=("Arial", 11, "bold"),
    bg=UPDATE_COLOR,
    fg=BUTTON_TEXT,
    command="update_student"
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    width=10,
    font=("Arial", 11, "bold"),
    bg=DELETE_COLOR,
    fg=BUTTON_TEXT,
    command="delete_student"
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=10,
    font=("Arial", 11, "bold"),
    bg=CLEAR_COLOR,
    fg=BUTTON_TEXT,
    command="clear_student"
).grid(row=0, column=3, padx=5)

#Table
tree=ttk.Treeview(
    root,
    columns=("ID", "Name", "Age", "Course",),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Course", text="Course")

tree.column("ID", width=50)
tree.column("Name", width=200)
tree.column("Age", width=80)
tree.column("Course", width=200)

tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

























