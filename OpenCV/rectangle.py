import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    print("Image loaded successfully")

    h, w, c = image.shape
    print(f"Height: {h}\nWidth: {w}\nChannels: {c}\n")

    pt1 = (50, 50)
    pt2 = (250, 200)
    color = (0, 255, 0)
    thickness = 3

    rectangle_image = cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Rectangle Image", rectangle_image)
    cv2.imwrite("Image/rectangle_image.jpeg", rectangle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
