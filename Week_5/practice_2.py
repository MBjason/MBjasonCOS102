import tkinter as tk
from tkinter import messagebox
from PIL import Image

def welcomeMessage(username):
    window = tk.Toplevel(root)
    window.title("Admin Box")
    wimdow.geometry("500X200")
    
    
    label_1 = tk.label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text= "This is Python GUI with Tkinter")
    label_2.pack()
    
    root.mainloop()
    
def submit():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == " Mary" and password == "cos102":
        welcomeMessage(username)
        
    else:
        messagebox.showerror("Login", "Invalid username or password")    
    
    

    
        