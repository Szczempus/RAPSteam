import tkinter as tk

root = tk.Tk()
root.title("Kopiowanie tekstu")


def kopiuj_tekst():
    pole2.delete(0, tk.END)
    pole2.insert(0, pole1.get())


pole1 = tk.Entry(root, width=30)
pole1.pack(pady=5)

pole2 = tk.Entry(root, width=30)
pole2.pack(pady=5)

btn = tk.Button(root, text="Kopiuj", command=kopiuj_tekst)
btn.pack(pady=10)

root.mainloop()
