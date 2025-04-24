import cv2
from util import get_limits
from PIL import Image

yellow = [0, 255, 255]  # Warna kuning dalam format HSV
cap = cv2.VideoCapture(0)  # Ganti ke 1 jika kamera 0 tidak muncul

while True:
    ret, frame = cap.read()

    if not ret:
        print("Gagal membaca dari kamera.")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Temukan kontur pada mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Hanya pertimbangkan kontur yang cukup besar
        if cv2.contourArea(contour) > 1000:  # Ganti angka ini untuk menyesuaikan ukuran minimum kontur
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
