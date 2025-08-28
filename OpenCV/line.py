import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    print("Image loaded successfully")

    h, w, c = image.shape
    print(f"Height: {h}\nWidth: {w}\nChannels: {c}\n")

    pt1 = (50, 100)
    pt2 = (300, 100)
    color = (255, 0, 0)
    thickness = 4

    lined_image = cv2.line(image, pt1, pt2, color, thickness)

    cv2.imshow("Lined Image", lined_image)
    cv2.imwrite("Image/lined_image.jpeg", lined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
