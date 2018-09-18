import numpy as np
import cv2

a = cv2.imread("a.jpg", cv2.IMREAD_UNCHANGED)
b = cv2.imread("b.jpg", cv2.IMREAD_UNCHANGED)

a = a.astype(float)
b = b.astype(float)


ab = a
for i in range(len(ab)):
  ab[i] = a[i] + b[i]

cv2.imwrite('Out.png', ab)
