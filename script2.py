import subprocess
import time

# Ścieżka do pliku z kodem, który chcesz wyświetlić
file_to_display = "/home/files/zadanie_2.py"

# Uruchom terminal xterm, aby wyświetlić listing kodu
result_file = "/home/outcome/result.txt"
with open(result_file, "w") as result:
    subprocess.run(["python3", file_to_display], stdout=result, stderr=subprocess.STDOUT)

# Wyświetl wynik w terminalu graficznym
subprocess.Popen([
    "xfce4-terminal", "--geometry=136x40", "--hold", "-e", f"cat {result_file}"
])

time.sleep(3)

# Ścieżki do plików
xwd_path = "/home/outcome/screenshot.xwd"
png_path = "/home/outcome/screenshot.png"

# Wykonaj zrzut ekranu za pomocą xwd
subprocess.run(["xwd", "-root", "-display", ":99", "-out", xwd_path], check=True)

# Konwertuj .xwd na .png za pomocą ImageMagick
subprocess.run(["convert", xwd_path, png_path], check=True)

print(f"Screenshot saved to {png_path}")
