import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Employee Management System")
window.geometry("750x700")
window.configure(bg="#EAF4FB")

employees = []
selected_employee = None

# COLORS

BG_COLOR = "#C8DFDB"
TITLE_COLOR = "#6A1B9A"
LABEL_COLOR = "#1976D2"
ENTRY_BG = "#FFFFFF"

BUTTON_BLUE = "#1976D2"
BUTTON_GREEN = "#2E7D32"
BUTTON_RED = "#D32F2F"
BUTTON_ORANGE = "#EF6C00"
BUTTON_GRAY = "#546E7A"

CARD_COLOR = "#FFFFFF"
SELECTED_COLOR = "#BBDEFB"
BORDER_COLOR = "#90CAF9"

# ADD EMPLOYEE
def add_employee():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    course = course_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    city = city_entry.get().strip()

    if not name or not age or not course or not email or not phone or not city:
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    employees.append({
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "phone": phone,
        "city": city
    })

    display_employees()
    clear_fields()

# DISPLAY EMPLOYEES
def display_employees():
    global selected_employee

    for widget in result_frame.winfo_children():
        widget.destroy()

    selected_employee = None

    for index, employee in enumerate(employees):

        employee_frame = tk.Frame(
            result_frame,
            bd=2,
            relief="solid",
            padx=10,
            pady=8,
            bg=CARD_COLOR,
            highlightbackground=BORDER_COLOR,
            highlightcolor=BORDER_COLOR,
            highlightthickness=1
        )

        employee_frame.pack(
            pady=5,
            padx=20,
            fill="x"
        )

        employee_name_label = tk.Label(
            employee_frame,
            text=f"Name: {employee['name']}",
            font=("Arial", 10, "bold"),
            bg=CARD_COLOR,
            fg="#0D47A1",
            anchor="w"
        )
        employee_name_label.pack(anchor="w")

        employee_age_label = tk.Label(
            employee_frame,
            text=f"Age: {employee['age']}",
            font=("Arial", 10),
            bg=CARD_COLOR,
            fg=LABEL_COLOR,
            anchor="w"
        )
        employee_age_label.pack(anchor="w")

        employee_course_label = tk.Label(
            employee_frame,
            text=f"Course: {employee['course']}",
            font=("Arial", 10),
            bg=CARD_COLOR,
            fg=LABEL_COLOR,
            anchor="w"
        )
        employee_course_label.pack(anchor="w")

        employee_email_label = tk.Label(
            employee_frame,
            text=f"Email: {employee['email']}",
            font=("Arial", 10),
            bg=CARD_COLOR,
            fg=LABEL_COLOR,
            anchor="w"
        )
        employee_email_label.pack(anchor="w")

        employee_phone_label = tk.Label(
            employee_frame,
            text=f"Phone: {employee['phone']}",
            font=("Arial", 10),
            bg=CARD_COLOR,
            fg=LABEL_COLOR,
            anchor="w"
        )
        employee_phone_label.pack(anchor="w")

        employee_city_label = tk.Label(
            employee_frame,
            text=f"City: {employee['city']}",
            font=("Arial", 10),
            bg=CARD_COLOR,
            fg=LABEL_COLOR,
            anchor="w"
        )
        employee_city_label.pack(anchor="w")

        # Allow clicking employee box or labels
        employee_frame.bind(
            "<Button-1>",
            lambda event, i=index: select_employee(i)
        )

        employee_name_label.bind(
            "<Button-1>",
            lambda event, i=index: select_employee(i)
        )

        employee_age_label.bind(
            "<Button-1>",
            lambda event, i=index: select_employee(i)
        )

        employee_course_label.bind(
            "<Button-1>",
            lambda event, i=index: select_employee(i)
        )

        employee_email_label.bind(
            "<Button-1>",
            lambda event, i=index: select_employee(i)
        )

        employee_phone_label.bind(
            "<Button-1>",
            lambda event, i=index: select_employee(i)
        )

        employee_city_label.bind(
            "<Button-1>",
            lambda event, i=index: select_employee(i)
        )

# SELECT EMPLOYEE
def select_employee(index):
    global selected_employee

    selected_employee = index
    employee = employees[index]

    clear_entries_only()

    name_entry.insert(0, employee["name"])
    age_entry.insert(0, employee["age"])
    course_entry.insert(0, employee["course"])
    email_entry.insert(0, employee["email"])
    phone_entry.insert(0, employee["phone"])
    city_entry.insert(0, employee["city"])

    highlight_selected_employee()

# HIGHLIGHT SELECTED EMPLOYEE
def highlight_selected_employee():

    for widget in result_frame.winfo_children():

        widget.config(
            bg=CARD_COLOR,
            bd=2
        )

        for child in widget.winfo_children():
            child.config(bg=CARD_COLOR)

    if selected_employee is not None:

        employee_boxes = result_frame.winfo_children()

        if selected_employee < len(employee_boxes):

            selected_box = employee_boxes[selected_employee]

            selected_box.config(
                bg=SELECTED_COLOR,
                bd=3
            )

            for child in selected_box.winfo_children():
                child.config(bg=SELECTED_COLOR)

# UPDATE EMPLOYEE
def update_employee():
    global selected_employee

    if selected_employee is None:
        messagebox.showwarning(
            "Warning",
            "Please select an employee to update."
        )
        return

    name = name_entry.get().strip()
    age = age_entry.get().strip()
    course = course_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    city = city_entry.get().strip()

    if not name or not age or not course or not email or not phone or not city:
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    employees[selected_employee]["name"] = name
    employees[selected_employee]["age"] = age
    employees[selected_employee]["course"] = course
    employees[selected_employee]["email"] = email
    employees[selected_employee]["phone"] = phone
    employees[selected_employee]["city"] = city

    updated_index = selected_employee

    display_employees()

    selected_employee = updated_index

    clear_entries_only()

    name_entry.insert(0, employees[updated_index]["name"])
    age_entry.insert(0, employees[updated_index]["age"])
    course_entry.insert(0, employees[updated_index]["course"])
    email_entry.insert(0, employees[updated_index]["email"])
    phone_entry.insert(0, employees[updated_index]["phone"])
    city_entry.insert(0, employees[updated_index]["city"])

    highlight_selected_employee()

    messagebox.showinfo(
        "Success",
        "Employee information updated successfully."
    )

# DELETE EMPLOYEE
def delete_employee():
    global selected_employee

    if selected_employee is None:
        messagebox.showwarning(
            "Warning",
            "Please select an employee to delete."
        )
        return

    result = messagebox.askyesno(
        "Delete Employee",
        "Are you sure you want to delete this employee?"
    )

    if not result:
        return

    employees.pop(selected_employee)

    selected_employee = None

    display_employees()
    clear_fields()


# CLEAR ENTRIES
def clear_entries_only():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)

# CLEAR ALL
def clear_fields():
    global selected_employee

    clear_entries_only()

    selected_employee = None

    for widget in result_frame.winfo_children():

        widget.config(
            bg=CARD_COLOR,
            bd=2
        )

        for child in widget.winfo_children():
            child.config(bg=CARD_COLOR)


# EXIT
def exit_program():
    window.destroy()

# TITLE
title_label = tk.Label(
    window,
    text="EMPLOYEE MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg=TITLE_COLOR
)
title_label.pack(pady=(15, 10))

# FORM FRAME

form_frame = tk.Frame(
    window,
    bg=BG_COLOR
)

form_frame.pack()

# NAME
name_label = tk.Label(
    form_frame,
    text="Name:",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=LABEL_COLOR
)
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(
    form_frame,
    width=40,
    font=("Arial", 10),
    bg=ENTRY_BG,
    fg="#212121",
    relief="solid",
    bd=1
)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# AGE
age_label = tk.Label(
    form_frame,
    text="Age:",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=LABEL_COLOR
)
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

age_entry = tk.Entry(
    form_frame,
    width=40,
    font=("Arial", 10),
    bg=ENTRY_BG,
    fg="#212121",
    relief="solid",
    bd=1
)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# COURSE
course_label = tk.Label(
    form_frame,
    text="Course:",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=LABEL_COLOR
)
course_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

course_entry = tk.Entry(
    form_frame,
    width=40,
    font=("Arial", 10),
    bg=ENTRY_BG,
    fg="#212121",
    relief="solid",
    bd=1
)
course_entry.grid(row=2, column=1, padx=10, pady=5)

# EMAIL
email_label = tk.Label(
    form_frame,
    text="Email:",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=LABEL_COLOR
)
email_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

email_entry = tk.Entry(
    form_frame,
    width=40,
    font=("Arial", 10),
    bg=ENTRY_BG,
    fg="#212121",
    relief="solid",
    bd=1
)
email_entry.grid(row=3, column=1, padx=10, pady=5)

# PHONE
phone_label = tk.Label(
    form_frame,
    text="Phone:",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=LABEL_COLOR
)
phone_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

phone_entry = tk.Entry(
    form_frame,
    width=40,
    font=("Arial", 10),
    bg=ENTRY_BG,
    fg="#212121",
    relief="solid",
    bd=1
)
phone_entry.grid(row=4, column=1, padx=10, pady=5)

# CITY
city_label = tk.Label(
    form_frame,
    text="City:",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=LABEL_COLOR
)
city_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

city_entry = tk.Entry(
    form_frame,
    width=40,
    font=("Arial", 10),
    bg=ENTRY_BG,
    fg="#212121",
    relief="solid",
    bd=1
)
city_entry.grid(row=5, column=1, padx=10, pady=5)

# BUTTON FRAME
button_frame = tk.Frame(
    window,
    bg=BG_COLOR
)

button_frame.pack(pady=15)

# BUTTONS
add_button = tk.Button(
    button_frame,
    text="Add",
    width=10,
    bg=BUTTON_GREEN,
    fg="white",
    activebackground="#1B5E20",
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    command=add_employee
)
add_button.grid(row=0, column=0, padx=5)


update_button = tk.Button(
    button_frame,
    text="Update",
    width=10,
    bg=BUTTON_BLUE,
    fg="white",
    activebackground="#0D47A1",
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    command=update_employee
)
update_button.grid(row=0, column=1, padx=5)


delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=10,
    bg=BUTTON_RED,
    fg="white",
    activebackground="#B71C1C",
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    command=delete_employee
)
delete_button.grid(row=0, column=2, padx=5)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=10,
    bg=BUTTON_ORANGE,
    fg="white",
    activebackground="#E65100",
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    command=clear_fields
)
clear_button.grid(row=0, column=3, padx=5)


exit_button = tk.Button(
    button_frame,
    text="Exit",
    width=10,
    bg=BUTTON_GRAY,
    fg="white",
    activebackground="#37474F",
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    command=exit_program
)
exit_button.grid(row=0, column=4, padx=5)

# EMPLOYEE INFORMATION

output_label = tk.Label(
    window,
    text="Employee Information",
    font=("Arial", 13, "bold"),
    bg=BG_COLOR,
    fg=TITLE_COLOR
)
output_label.pack(pady=(5, 3))


result_label = tk.Label(
    window,
    text="Click an employee to select and edit",
    font=("Arial", 10, "bold"),
    bg=BG_COLOR,
    fg="#546E7A"
)
result_label.pack(pady=(3, 5))

# RESULT FRAME
result_frame = tk.Frame(
    window,
    bg=BG_COLOR
)

result_frame.pack(
    pady=5,
    padx=10,
    fill="both",
    expand=True
)

# START PROGRAM

window.mainloop()
