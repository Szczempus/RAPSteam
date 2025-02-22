import pyautogui

# Pobranie aktualnej pozycji kursora
x, y = pyautogui.position()
print(f"Położenie kursora: X={x}, Y={y}")
