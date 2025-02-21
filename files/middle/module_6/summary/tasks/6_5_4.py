import tkinter as tk
from tkinter import messagebox


def sprawdz():
    if var.get():
        messagebox.showinfo("Regulamin", "Regulamin zaakceptowany!")


root = tk.Tk()
root.title("CheckBox")

var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Akceptuję regulamin", variable=var, command=sprawdz)
checkbox.pack()

root.mainloop()
