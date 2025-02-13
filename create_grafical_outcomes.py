import glob
import os
import re
import subprocess
import time

import pyautogui
import pygetwindow as gw

# Pełna ścieżka do Pythona (zmień na swoją wersję)
python_exe = r"C:\Users\Patryk\AppData\Local\Programs\Python\Python311\python.exe"

# Folder główny
script_folder = "files/beginner"

# Pobieranie plików .py w podfolderach "code"
py_files = glob.glob(os.path.join(script_folder, "**", "code", "*.py"), recursive=True)


def extract_arguments_from_file(file_path):
    """Pobiera argumenty z komentarza # Argumenty: "1" "2" "3"."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                match = re.search(r'#\s*Argumenty:\s*"(.+?)"', line)
                if match:
                    return match.group(1)  # Zwracamy argumenty w postaci stringa
    except Exception as e:
        print(f"❌ Błąd podczas odczytu pliku: {file_path} - {e}")
    return ""  # Brak argumentów


for py_file in py_files:
    time.sleep(3)
    py_file = os.path.abspath(py_file)  # Pełna ścieżka
    if not os.path.exists(py_file) or "__init__" in py_file:
        print(f"❌ Pominięto: {py_file}")
        continue

    # Ścieżka do folderu "screenshots" w tej samej lekcji co plik
    lesson_folder = os.path.dirname(os.path.dirname(py_file))  # Folder lekcji
    screenshot_folder = os.path.join(lesson_folder, "screenshots")
    os.makedirs(screenshot_folder, exist_ok=True)  # Tworzymy folder, jeśli nie istnieje

    screenshot_path = os.path.join(screenshot_folder, f"{os.path.basename(py_file)}.png")
    print(f"🚀 Uruchamiam: {py_file}")

    # Pobieramy argumenty z pliku
    arguments = extract_arguments_from_file(py_file)

    # Tworzymy polecenie CMD do uruchomienia skryptu w nowym oknie
    cmd_command = f'start cmd /k "color F0 && {python_exe} {py_file} {arguments}"'

    # Uruchamiamy CMD z białym tłem
    process = subprocess.Popen(cmd_command, shell=True, text=True)

    # Czekamy chwilę, aby CMD się otworzyło i było widoczne
    time.sleep(2)

    # Znalezienie okna CMD
    windows = [w for w in gw.getAllWindows() if "cmd" in w.title.lower() or "command prompt" in w.title.lower()]

    if not windows:
        print("❌ Nie znaleziono okna CMD")
        continue

    cmd_window = windows[0]  # Ostatnio otwarte okno CMD

    # x, y, width, height = cmd_window.left, cmd_window.top, cmd_window.width, cmd_window.height
    time.sleep(2)  # Dajemy czas na aktywację
    # Nowe wymiary okna CMD w pikselach
    width = 1000
    height = 600
    x = 200
    y = 100

    print(f"🖼️ CMD: {x}, {y}, {width}, {height}")

    # Ustawienie pozycji i rozmiaru okna CMD
    cmd_window.moveTo(x, y)  # Przesunięcie okna
    cmd_window.resizeTo(width, height)  # Zmiana rozmiaru
    time.sleep(1)
    # **Aktywujemy okno CMD przed zrobieniem screenshota**
    cmd_window.activate()
    time.sleep(2)  # Dajemy czas na aktywację

    # **Klikamy w środek okna CMD, aby upewnić się, że jest aktywne**
    pyautogui.click(x + width // 2, y + height // 2)

    # Screenshot tylko okna CMD
    crop_margin = 10  # Liczba pikseli do ucięcia z boków i dołu

    # Zmieniamy region, aby usunąć ramkę, NIE ruszamy góry ekranu
    pyautogui.screenshot(
        screenshot_path,
        region=(x + crop_margin, y, width - (2 * crop_margin), height - crop_margin)
    )

    print(f"📸 Screenshot zapisany: {screenshot_path}")

    # Zamknięcie okna CMD
    subprocess.Popen("taskkill /F /IM cmd.exe", shell=True)

print("✅ Zakończono!")
