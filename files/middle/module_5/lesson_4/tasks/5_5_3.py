import cv2

cap = cv2.VideoCapture(0)  # Otwórz kamerę (0 - pierwsza dostępna)
ret, frame = cap.read()  # Pobierz pojedynczą klatkę
cap.release()  # Zwolnij kamerę

if ret:
    cv2.imwrite("screenshot.png", frame)  # Zapisz obraz do pliku
    print("Screenshot zapisany jako screenshot.png")
else:
    print("Nie udało się pobrać obrazu z kamery")
