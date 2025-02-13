import glob
import os
import subprocess
import time

import pyautogui
import pygetwindow as gw

# Pełna ścieżka do Pythona (zmień na swoją wersję)
python_exe = r"C:\Users\Patryk\AppData\Local\Programs\Python\Python311\python.exe"

# Foldery
script_folder = "files/beginner"
output_folder = "screenshots"
os.makedirs(output_folder, exist_ok=True)

# Pobieranie plików .py
py_files = glob.glob(os.path.join(script_folder, "**", "code", "*.py"), recursive=True)

for py_file in py_files:
    py_file = os.path.abspath(py_file)  # Pełna ścieżka
    if not os.path.exists(py_file):
        print(f"❌ Plik nie istnieje: {py_file}")
        continue

    screenshot_path = os.path.join(output_folder, f"{os.path.basename(py_file)}.png")
    print(f"🚀 Uruchamiam: {py_file}")

    # Uruchomienie skryptu w nowym oknie CMD, które się nie zamknie od razu
    # Uruchomienie nowego okna CMD, ustawienie koloru i uruchomienie skryptu
    ps_script = r"C:\Users\Patryk\PycharmProjects\RaPSteam_docx\run_cmd_as_admin.ps1"
    subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script], shell=True)
    # Poczekaj chwilę, aż okno CMD się otworzy
    time.sleep(3)

    # Znalezienie okna CMD
    windows = [w for w in gw.getAllWindows() if "cmd" in w.title.lower()]
    if not windows:
        print("❌ Nie znaleziono okna CMD")
        continue

    cmd_window = windows[-1]  # Pierwsze znalezione okno CMD
    x, y, width, height = cmd_window.left, cmd_window.top, cmd_window.width, cmd_window.height
    print(f"🖼️ CMD: {x}, {y}, {width}, {height}")

    # Screenshot tylko okna CMD
    pyautogui.screenshot(screenshot_path, region=(x, y, width, height))
    print(f"📸 Screenshot zapisany: {screenshot_path}")

print("✅ Zakończono!")
