import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CheckBox Tkinter")


def pokaz_komunikat():
    if var.get():
        messagebox.showinfo("Informacja", "Regulamin zaakceptowany!")


var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Akceptuję regulamin", variable=var, command=pokaz_komunikat)
checkbox.pack(pady=10)

root.mainloop()
