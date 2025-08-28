import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), dtype="uint8")
img2 = np.zeros((250, 500, 3), dtype="uint8")

cv2.rectangle(img1, (50, 50), (200, 200), (255, 255, 255), -1)
cv2.circle(img2, (300, 125), 75, (255, 255, 255), -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)
bitwise_not1 = cv2.bitwise_not(img1)
bitwise_not2 = cv2.bitwise_not(img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise XOR', bitwise_xor)
cv2.imshow('Bitwise NOT 1', bitwise_not1)
cv2.imshow('Bitwise NOT 2', bitwise_not2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Image/bitwise_and.jpeg', bitwise_and)
cv2.imwrite('Image/bitwise_or.jpeg', bitwise_or)
cv2.imwrite('Image/bitwise_xor.jpeg', bitwise_xor)
cv2.imwrite('Image/bitwise_not1.jpeg', bitwise_not1)
cv2.imwrite('Image/bitwise_not2.jpeg', bitwise_not2)