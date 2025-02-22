import cv2

cap = cv2.VideoCapture(0)  # Otwórz kamerę

while True:
    ret, frame = cap.read()  # Pobierz klatkę obrazu
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Konwersja do skali szarości
    cv2.imshow("Podgląd - Obraz czarno-biały", gray_frame)  # Wyświetlenie obrazu

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wyjście po naciśnięciu 'q'
        break

cap.release()  # Zwolnij kamerę
cv2.destroyAllWindows()  # Zamknij okno
