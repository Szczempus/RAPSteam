import cv2

cap = cv2.VideoCapture(0)  # Inicjalizacja kamery

while True:
    ret, frame = cap.read()  # Odczyt klatki obrazu
    if not ret:
        break

    cv2.imshow("Podgląd kamery", frame)  # Wyświetlanie obrazu

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wyjście po naciśnięciu 'q'
        break

cap.release()
cv2.destroyAllWindows()
