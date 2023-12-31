import cv2
import numpy as np
from pyzbar.pyzbar import decode

lst = ['Akshit Madan', 'Mira Singh', 'Aditya Dev', 'Sameer Bhat']

img = cv2.imread('assets/4.png')
img = cv2.resize(img, (512,512))
for qrcode in decode(img):
    codeData = qrcode.data.decode('utf-8')
    print(codeData)
    # print(qrcode)
    points = (np.array([qrcode.polygon], np.int32))
    # print(points)
    points = (points.reshape((-1, 1, 2)))
    points2 = qrcode.rect
    if codeData in lst:
        cv2.polylines(img, [points], True, (0,255,0), 5)
        cv2.putText(img, codeData, (points2[0], points2[1]-10), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (0,255,0), 2)
    else:
        cv2.polylines(img, [points], True, (0,0,255), 5)
        cv2.putText(img, 'UnAuthorized', (points2[0], points2[1]-10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,0,255), 2)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
