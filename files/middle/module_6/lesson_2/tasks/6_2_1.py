import tkinter as tk

root = tk.Tk()
root.title("Aplikacja Tkinter")

label = tk.Label(root, text="Witaj w aplikacji!", font=("Arial", 14))
label.pack(pady=20)


def zamknij():
    root.destroy()


btn = tk.Button(root, text="Zamknij", command=zamknij)
btn.pack(pady=10)

root.mainloop()
