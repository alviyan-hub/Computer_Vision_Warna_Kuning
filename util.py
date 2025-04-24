import numpy as np
import cv2

def get_limits(color):
    # Mengubah warna dari BGR ke HSV
    c = np.uint8([[color]])  # Membuat array 2D dengan satu pixel untuk warna yang diberikan
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # Konversi ke HSV

    # Menentukan batas bawah dan atas berdasarkan nilai Hue
    
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255  # Sesuaikan saturasi dan value

    # Mengubah menjadi array tipe uint8
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

