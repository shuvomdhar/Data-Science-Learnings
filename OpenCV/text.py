import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    print("Image loaded successfully")

    h, w, c = image.shape
    print(f"Height: {h}\nWidth: {w}\nChannels: {c}\n")

    put_text = cv2.putText(image, "Hello Python Programmers", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)

    cv2.imshow("Text in the Image", put_text)
    cv2.imwrite("Image/text_in_image.jpeg", put_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
