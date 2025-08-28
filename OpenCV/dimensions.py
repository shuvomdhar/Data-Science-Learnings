import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    height, width, channels = image.shape
    print(f"Height of the image is {height},\nwidth of the image is {width} and \nthe number of channels of the image is {channels}")
