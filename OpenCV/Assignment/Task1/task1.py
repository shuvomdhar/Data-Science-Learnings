import cv2

image = cv2.imread(r"Assignment/Task1/cover.jpeg")

if image is not None:
    print("Image found")
    cv2.imshow("Assignment 1 Input Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    bgrToGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    output = cv2.imwrite(r"Assignment/Task1/output.jpeg", bgrToGray)
    cv2.imshow("Assignment 1 Output Image", bgrToGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if output is not None:
        print("Image is saved successfully")
        height, width, channels = image.shape
        print(f"Height of the image is {height},\nwidth of the image is {width} and \nthe number of channels of the image is {channels}")
    else:
        print("Image could not be saved")
else:
    print("Image is not found")
