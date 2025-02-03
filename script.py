import os
import subprocess
import time

# Ścieżka do pliku z kodem, który chcesz wyświetlić
file_to_display = "/home/files/zadanie_2.py"

# Lista terminali do przetestowania
terminals = [
    ("xfce4-terminal", ["xfce4-terminal", "--geometry=136x40", "--hold", "-e", "cat"]),
    ("kitty", ["kitty", "--hold", "--override", "background=white", "--override", "foreground=black", "cat"]),
    ("urxvt", ["urxvt", "-bg", "white", "-fg", "black", "-hold", "-geometry", "136x40", "-e", "cat"]),
    ("xterm", ["xterm", "-bg", "white", "-fg", "black", "-hold", "-geometry", "136x40", "-e", "cat"])
]

# Ścieżka katalogu do wyników
output_dir = "/home/outcome/"
os.makedirs(output_dir, exist_ok=True)

# Uruchomienie testów dla każdego terminala
for terminal_name, terminal_command in terminals:
    try:
        print(f"Testing terminal: {terminal_name}")

        # Plik wynikowy
        result_file = os.path.join(output_dir, f"{terminal_name}_result.txt")

        # Uruchomienie skryptu Python i zapisanie wyniku do pliku
        with open(result_file, "w") as result:
            subprocess.run(["python3", file_to_display], stdout=result, stderr=subprocess.STDOUT)

        # Wyświetlenie wyniku w terminalu
        terminal_process = subprocess.Popen(terminal_command + [result_file])

        # Czekaj na wyrenderowanie
        time.sleep(3)

        # Wykonaj zrzut ekranu
        xwd_path = os.path.join(output_dir, f"{terminal_name}_screenshot.xwd")
        png_path = os.path.join(output_dir, f"{terminal_name}_screenshot.png")
        subprocess.run(["xwd", "-root", "-display", ":99", "-out", xwd_path], check=True)

        # Konwertuj .xwd na .png za pomocą ImageMagick
        subprocess.run(["convert", xwd_path, png_path], check=True)

        print(f"Screenshot for {terminal_name} saved to {png_path}")

        # Zamknij terminal
        terminal_process.terminate()
        time.sleep(1)

    except Exception as e:
        print(f"Error testing terminal {terminal_name}: {e}")

print("All terminal tests completed.")
