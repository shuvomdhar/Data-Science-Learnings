import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    print("Image loaded successfully")

    h, w, c = image.shape
    print(f"Height: {h}\nWidth: {w}\nChannels: {c}\n")

    center = (150, 150)
    radius = 50
    color = (255, 0, 0)
    thickness = -1

    circle_image = cv2.circle(image, center, radius, color, thickness)

    cv2.imshow("Circle Image", circle_image)
    cv2.imwrite("Image/circle_image.jpeg", circle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
