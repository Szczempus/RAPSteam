import tkinter as tk


def mnoz():
    wynik.set(int(entry.get()) * 2)


root = tk.Tk()
root.title("Mnożenie")

entry = tk.Entry(root)
entry.pack()
wynik = tk.StringVar()
button = tk.Button(root, text="Pomnóż przez 2", command=mnoz)
button.pack()
label = tk.Label(root, textvariable=wynik)
label.pack()

root.mainloop()
