import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.drawContours(image, [cnt], 0, (0, 255, 0), 2)
    cv2.imshow('Original Image', image)
    cv2.imshow('Thresholded Image', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Image/contours_image.jpeg', image)