import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    median_blurred = cv2.medianBlur(image, 11)
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', median_blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Image/median_blurred_image.jpeg', median_blurred)