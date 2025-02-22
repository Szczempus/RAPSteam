import cv2

index = 0
available_cameras = []

while True:
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:  # Sprawdzenie, czy kamera działa
        break
    available_cameras.append(index)
    cap.release()
    index += 1

if available_cameras:
    print("Dostępne kamery:")
    for cam in available_cameras:
        print(f"- Kamera {cam}")
else:
    print("Brak dostępnych kamer")
