import glob
import os
import time

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

# Pełna ścieżka do Pythona (zmień na swoją wersję)
python_exe = r"C:\Users\Patryk\AppData\Local\Programs\Python\Python311\python.exe"

# Folder główny
script_folder = "files/beginner/module_1"

# Pobieranie plików .py w podfolderach "code"
single = "1_7_5"
# single = None

py_files = glob.glob(os.path.join(script_folder, "**", "code", "*.py"), recursive=True)
py_files += glob.glob(os.path.join(script_folder, "**", "tasks", "*.py"), recursive=True)

if single:
    py_files = glob.glob(os.path.join(script_folder, "**", "code", f"{single}.py"), recursive=True)
    py_files += glob.glob(os.path.join(script_folder, "**", "tasks", f"{single}.py"), recursive=True)
    print(py_files)


def crop_me(screenshot_path):
    # Wczytaj obraz
    image = cv2.imread(screenshot_path)

    # Jeśli obraz nie został załadowany poprawnie, przerwij
    if image is None:
        print("❌ Nie można załadować obrazu.")
        return

    # Wymiary oryginalnego obrazu
    h, w, _ = image.shape

    # **1. Usuń dolny margines 40px**
    image = image[:h - 40, :]

    # **2. Tworzenie maski dla tekstu (ciemne piksele na tle F2F2F2)**
    lower_text = np.array([0, 0, 0], dtype=np.uint8)  # Czarne odcienie
    upper_text = np.array([60, 60, 60], dtype=np.uint8)  # Jasne czarne (lekko szare)
    mask_text = cv2.inRange(image, lower_text, upper_text)  # Maskujemy tylko tekst

    # **3. Przetwarzanie od dołu, aby znaleźć pierwszą linię z ≥ 45px tekstu**
    cut_y = None
    last_removed_lines = []  # Przechowuje usunięte linie

    for y in range(image.shape[0] - 1, -1, -1):  # Iterujemy od dołu do góry
        row_text = mask_text[y, :]  # Pobieramy linię w masce

        # print(f"Rząd {y}: {np.count_nonzero(row_text)}")  # Liczba pikseli tekstu w wierszu

        if np.count_nonzero(row_text) >= 50:  # Jeśli wiersz ma ≥ 45 pikseli tekstu
            cut_y = y
            break  # Znaleziono linię z treścią → przestajemy usuwać
        else:
            last_removed_lines.append(y)  # Dodajemy usunięte linie do listy

    # **4. Jeśli znaleziono linię, przycinamy i dodajemy elementy**
    if cut_y is not None:
        cropped_image = image[:cut_y + 1, :]  # Zachowujemy tylko istotne linie

        # **5. Pobranie 3. linii od ostatniej usuniętej**
        if len(last_removed_lines) >= 3:
            line_to_repeat = last_removed_lines[2]  # 3. od końca usunięta linia
        else:
            line_to_repeat = last_removed_lines[
                -1] if last_removed_lines else cut_y  # Jeśli brak, użyj ostatniej dostępnej

        repeated_row = image[line_to_repeat:line_to_repeat + 1, :]  # Pobranie danej linii
        repeated_last_row = np.vstack([repeated_row] * 20)  # Powielenie jej 20 razy

        # **6. Dodanie 35 pikseli koloru #C0C0C0**
        gray_bar = np.full((15, w, 3), (12, 12, 12), dtype=np.uint8)  # Tworzymy jednolity pasek

        # **7. Łączenie: obraz + powielona linia + szary pasek**
        final_image = np.vstack((cropped_image, repeated_last_row, gray_bar))

        # **8. Zapisujemy obraz**
        output_path = screenshot_path.replace(".py.png", ".png")
        cv2.imwrite(output_path, final_image)
        print(f"✅ Obraz zapisany: {output_path}")
    else:
        print("❌ Nie znaleziono tekstu, obraz nie został przycięty.")

    # Usunięcie oryginalnego pliku po zapisaniu nowego
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
        print(f"🗑️ Oryginalny plik usunięty: {screenshot_path}")
    else:
        print(f"⚠️ Plik nie istnieje: {screenshot_path}")


import re
import subprocess


def extract_arguments_from_file(file_path):
    """Pobiera argumenty z komentarza # Argumenty: "1" "2" "3"."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = re.search(r'#\s*Argumenty:\s*(.*)', line)
                if match:
                    return match.group(1).strip().split(',')  # Zwracamy listę argumentów
    except Exception as e:
        print(f"❌ Błąd podczas odczytu pliku: {file_path} - {e}")
    return []  # Brak argumentów


def extract_inputs_from_file(file_path):
    """Pobiera inputy z komentarza # Input: "1" "2" "3"."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = re.search(r'#\s*Input:\s*(.*)', line)
                if match:
                    return match.group(1).strip().split(',')  # Zwracamy listę wartości inputów
    except Exception as e:
        print(f"❌ Błąd podczas odczytu pliku: {file_path} - {e}")
    return []  # Brak inputów


# Input: 1 2 3


for py_file in py_files:
    time.sleep(2)
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
    time.sleep(3)

    if inputs:
        print(f"🔧 Wprowadzam inputy: {inputs}")

        # Wysyłamy inputy do otwartego okna CMD
        for value in inputs:
            time.sleep(.1)
            pyautogui.write(value)  # Wpisuje tekst
            pyautogui.press("enter")  # Naciska Enter

    # Znalezienie okna CMD
    windows = [w for w in gw.getAllWindows() if "cmd" in w.title.lower() or "command prompt" in w.title.lower()]

    if not windows:
        print("❌ Nie znaleziono okna CMD")
        continue

    cmd_window = windows[0]  # Ostatnio otwarte okno CMD

    # x, y, width, height = cmd_window.left, cmd_window.top, cmd_window.width, cmd_window.height
    time.sleep(1)  # Dajemy czas na aktywację
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
