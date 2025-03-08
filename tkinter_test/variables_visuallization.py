import tkinter as tk
from tkinter import messagebox

def sprawdz_typ():
    wartość = entry.get()
    # Próbujemy przekonwertować na integer
    try:
        int(wartość)
        label_result.config(text="Typ: Integer", bg="lightblue")
        canvas.delete("all")
        canvas.create_rectangle(10, 10, 90, 90, fill="blue")
    except ValueError:
        # Próbujemy przekonwertować na float
        try:
            float(wartość)
            label_result.config(text="Typ: Float", bg="lightgreen")
            canvas.delete("all")
            canvas.create_oval(10, 10, 90, 90, fill="green")
        except ValueError:
            # Sprawdzamy czy to boolean
            if wartość.lower() in ['true', 'false']:
                label_result.config(text="Typ: Boolean", bg="lightyellow")
                canvas.delete("all")
                canvas.create_polygon(50, 10, 90, 90, 10, 90, fill="yellow")
            else:
                # Jeśli żadna konwersja się nie udała, to traktujemy to jako string
                label_result.config(text="Typ: String", bg="lightpink")
                canvas.delete("all")
                canvas.create_rectangle(10, 10, 90, 90, fill="pink")

root = tk.Tk()
root.title("Wizualizacja Typów Zmiennych")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=10)

btn = tk.Button(root, text="Sprawdź typ", command=sprawdz_typ, font=("Arial", 12))
btn.pack(pady=5)

label_result = tk.Label(root, text="Podaj wartość", width=20, height=2, font=("Arial", 14))
label_result.pack(pady=10)

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack(pady=10)

root.mainloop()
