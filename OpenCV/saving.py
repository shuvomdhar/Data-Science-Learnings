import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    print("Image loaded successfully")
    cv2.imshow("Image showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    output = cv2.imwrite("Image/output.jpeg", image)
    if output:
        print("Image saved successfully")
    else:
        print("Image did not save successfully")
