import cv2

image = cv2.imread("Image/random.jpeg")

if image is not None:
    cropped = image[100:200, 50:150]
    if cropped is not None:
        cv2.imshow("Original Image", image)
        cv2.imshow("Cropped Image", cropped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("cropped_image.jpeg", cropped)
    else:
        print("Image cropping operation failed")
else:
    print("Image could not be found")