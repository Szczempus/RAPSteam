import tkinter as tk


def odwroc_tekst():
    wynik.set(entry.get()[::-1])


root = tk.Tk()
root.title("Odwracanie tekstu")

entry = tk.Entry(root)
entry.pack()
wynik = tk.StringVar()
button = tk.Button(root, text="Odwróć", command=odwroc_tekst)
button.pack()
label = tk.Label(root, textvariable=wynik)
label.pack()

root.mainloop()
