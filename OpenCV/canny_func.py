import cv2

image = cv2.imread('Image/random.jpeg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image does not load")
else:
    edges = cv2.Canny(image, 100, 200)
    cv2.imshow('Original Image', image)
    cv2.imshow('Canny Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Image/canny_edges.jpeg', edges)