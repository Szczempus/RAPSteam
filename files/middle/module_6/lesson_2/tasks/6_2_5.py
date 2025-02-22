import tkinter as tk

root = tk.Tk()
root.title("Licznik kliknięć")

licznik = 0


def zwieksz_licznik():
    global licznik
    licznik += 1
    label.config(text=f"Kliknięcia: {licznik}")


label = tk.Label(root, text="Kliknięcia: 0", font=("Arial", 14))
label.pack(pady=10)

btn = tk.Button(root, text="Kliknij mnie", command=zwieksz_licznik)
btn.pack(pady=10)

root.mainloop()
