import glob
import os
import re
import subprocess
import time

import pyautogui

# Pełna ścieżka do Pythona (zmień na swoją wersję)
python_exe = r"C:\Users\Patryk\AppData\Local\Programs\Python\Python311\python.exe"

# Foldery
script_folder = "files/beginner"
output_folder = "screenshots"
os.makedirs(output_folder, exist_ok=True)

# Pobieranie plików .py
py_files = glob.glob(os.path.join(script_folder, "**", "code", "*.py"), recursive=True)


def extract_input_from_file(file_path):
    """Pobiera wartości input() z drugiej linijki pliku .py"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) > 1:
                match = re.search(r'Inputs:\s*"(.+?)"', lines[1])
                if match:
                    return match.group(1).replace('"', '').replace(' ', '\n')  # Zamienia spacje na nowe linie
    except Exception as e:
        print(f"❌ Błąd podczas odczytu pliku: {file_path} - {e}")
    return None  # Brak inputów


for py_file in py_files:
    py_file = os.path.abspath(py_file)  # Pełna ścieżka
    if not os.path.exists(py_file):
        print(f"❌ Plik nie istnieje: {py_file}")
        continue
    # if __init__.py
    if "__init__" in py_file:
        continue

    time.sleep(5)
    screenshot_path = os.path.join(output_folder, f"{os.path.basename(py_file)}.png")
    print(f"🚀 Uruchamiam: {py_file}")

    # Pobieramy inputy z pliku
    input_data = extract_input_from_file(py_file)

    # Tworzymy polecenie CMD do uruchomienia skryptu w nowym oknie
    cmd_command = f'start cmd /k "color F0 && {python_exe} {py_file}"'

    # Uruchamiamy CMD z białym tłem
    process = subprocess.Popen(cmd_command, stdin=subprocess.PIPE, shell=True, text=True)
    time.sleep(5)  # Poczekaj chwilę, aż okno się otworzy
    # Jeśli skrypt wymaga inputów, przekazujemy je do stdin
    if input_data:
        process.communicate(input_data + "\n")  # Dodajemy ENTER na końcu

    import pygetwindow as gw

    windows = [w for w in gw.getAllWindows() if "cmd" in w.title.lower() or "command prompt" in w.title.lower()]

    if not windows:
        print("❌ Nie znaleziono okna CMD")
        continue

    cmd_window = windows[-1]  # Ostatnio otwarte okno CMD
    x, y, width, height = cmd_window.left, cmd_window.top, cmd_window.width, cmd_window.height
    print(f"🖼️ CMD: {x}, {y}, {width}, {height}")

    time.sleep(5)  # Dajemy czas na aktywację
    # **Aktywujemy okno CMD przed zrobieniem screenshota**
    # **Aktywujemy okno CMD przed zrobieniem screenshota**
    cmd_window.activate()
    time.sleep(5)  # Dajemy czas na aktywację

    # **Klikamy w środek okna CMD, aby upewnić się, że jest aktywne**
    pyautogui.click(x + width // 2, y + height // 2)

    # Screenshot tylko okna CMD
    pyautogui.screenshot(screenshot_path, region=(x, y, width, height))
    print(f"📸 Screenshot zapisany: {screenshot_path}")

    subprocess.Popen("taskkill /F /IM cmd.exe", shell=True)  # Zamknięcie okna CMD
