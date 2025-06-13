import tkinter as tk
from tkinter import messagebox

employes = {
     "IT": ["Alice Johnson", "Bob Smith", "Charlie King"],
    "HR": ["Diana Prince", "Eve Adams"],
    "Logistics": ["Frank Joe", "George Maxwell"],
    "Finance": ["Hannah Gray", "Ike Turner"]
}
def verification():
    name = name_entry.get()
    department = dept_var.get()
    
    if not name or department == "Select":
        messagebox.showinfo("Iput error, Please Enter valid input.")
        return
    
    if name in employes and department in employes[department]:
        messagebox.showinfo("Welcome !!!")
    else:
        messagebox.showinfo("Commot!!")
    
root = tk.TK()
root.title("GIG Employee Verification")
root.geometry(300*300)


tk.label(root, "Enter your full name").pack()
name_entry = tk.entry(root,width=30)
name_entry.pack()

tk.Label(root, text="Select Department:").pack()
dept_var = tk.StringVar(value="Select")
dept_menu = tk.OptionMenu(root, dept_var, *employees.keys())
dept_menu.pack

verify_button = tk.Button(root, text="Verify", command=verify_employee)
verify_button.pack(pady=15)

root.mainloop()
