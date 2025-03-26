import glob
import os
import time

import re
import subprocess

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

from utils import extract_arguments_from_file, extract_inputs_from_file, crop_me, is_cmd_running

# Pełna ścieżka do Pythona (zmień na swoją wersję)
python_exe = r"C:\Python311\python.exe"


# Pobieranie plików .py w podfolderach "code"
single = "5_4_5"
# single = None

modules = [1,2,3,4,5,6]

for module in modules:

    # Folder główny
    script_folder = f"files/middle/module_{module}"
    print("script_folder",script_folder)

    py_files = glob.glob(os.path.join(script_folder, "**", "code", "*.py"), recursive=True)
    py_files += glob.glob(os.path.join(script_folder, "**", "tasks", "*.py"), recursive=True)

    if single:
        py_files = glob.glob(os.path.join(script_folder, "**", "code", f"{single}.py"), recursive=True)
        py_files += glob.glob(os.path.join(script_folder, "**", "tasks", f"{single}.py"), recursive=True)
        print(py_files)


    for py_file in py_files:
        time.sleep(2)
        # while is_cmd_running():
        #     print("... wating ... ")
        #     try:
        #         subprocess.Popen("taskkill /F /IM cmd.exe", shell=True)
        #         process.terminate()  # Próba zakończenia procesu
        #         time.sleep(.5)  # Dajemy czas na zamknięcie
        #         process.kill()  # Wymuszone zamknięcie, jeśli nie zakończyło się poprawnie
        #     except Exception as e:
        #         pass
        #     time.sleep(1)


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
        inputs = extract_inputs_from_file(py_file)

        print(f"🔧 Argumenty: {arguments}")
        print(f"🔧 Inputy: {inputs}")

        # Tworzymy ciąg argumentów do przekazania w CMD
        arguments_str = " ".join(arguments)  # np. "1 2 3"

        # Tworzymy ciąg `echo` do przekazania wartości do input()
        input_str = " && ".join([f"echo {val}" for val in inputs]) if inputs else ""

        # Tworzymy polecenie CMD do uruchomienia skryptu
        cmd_command = f'start cmd /k "color F0 && {python_exe} {py_file} {arguments}"'

        process = subprocess.Popen(cmd_command, shell=True, stdin=subprocess.PIPE, text=True)
        time.sleep(1)

        if inputs:
            print(f"🔧 Wprowadzam inputy: {inputs}")

            # Wysyłamy inputy do otwartego okna CMD
            for value in inputs:
                time.sleep(.2)
                pyautogui.write(value)  # Wpisuje tekst
                pyautogui.press("enter")  # Naciska Enter

        # Znalezienie okna CMD
        windows = [w for w in gw.getAllWindows() if "cmd" in w.title.lower() or "command prompt" in w.title.lower()]

        if not windows:
            print("❌ Nie znaleziono okna CMD")
            continue

        cmd_window = windows[0]  # Ostatnio otwarte okno CMD

        # x, y, width, height = cmd_window.left, cmd_window.top, cmd_window.width, cmd_window.height
        time.sleep(.5)  # Dajemy czas na aktywację
        # Nowe wymiary okna CMD w pikselach
        width = 1001
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
        time.sleep(1)  # Dajemy czas na aktywację

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
        try:
            subprocess.Popen("taskkill /F /IM cmd.exe", shell=True)
            process.terminate()  # Próba zakończenia procesu
            time.sleep(1)  # Dajemy czas na zamknięcie
            process.kill()  # Wymuszone zamknięcie, jeśli nie zakończyło się poprawnie
        except Exception as e:
            pass

        crop_me(screenshot_path)
        print("🔥" * 20)

print("✅ Zakończono!")
