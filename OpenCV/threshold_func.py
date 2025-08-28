import cv2

image = cv2.imread('Image/random.jpeg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image does not load")
else:
    ret, thresh_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Original Image', image)
    cv2.imshow('Thresholded Image', thresh_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Image/thresholded_image.jpeg', thresh_img)