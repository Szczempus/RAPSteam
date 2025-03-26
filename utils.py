import glob
import os
import time

import re
import subprocess
import time
import psutil
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw


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


def is_cmd_running():
    """Sprawdza, czy jakiś proces cmd.exe jest aktywny."""
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and 'cmd.exe' in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False