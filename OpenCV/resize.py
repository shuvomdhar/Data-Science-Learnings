import cv2

image = cv2.imread("Image/random.jpeg")

if image is not None:
    resized = cv2.resize(image, (300, 300))
    if resized is not None:
        cv2.imshow("Original Image", image)
        cv2.imshow("Resized Image", resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("Image/resized_image.jpeg", resized)
    else:
        print("Image resize failed")
else:
    print("Image could not be found")