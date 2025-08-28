import cv2

image = cv2.imread("Image/random.jpeg")

if image is None:
    print("Could not load image")
else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imwrite("Image/flipped_horizontal.jpeg", flipped_horizontal)
    cv2.imwrite("Image/flipped_vertical.jpeg", flipped_vertical)
    cv2.imwrite("Image/flipped_both.jpeg", flipped_both)

    cv2.imshow("Original image", image)
    cv2.imshow("Horizontally flipped image", flipped_horizontal)
    cv2.imshow("Vertically flipped image", flipped_vertical)
    cv2.imshow("Horizontally and Vertically flipped image", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    