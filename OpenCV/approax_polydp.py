import cv2

image = cv2.imread('Image/random.jpeg')

if image is None:
    print("Error: Image does not load")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

        corners = len(approx)
        if corners == 3:
            shape = "Triangle"
        elif corners == 4:
            shape = "Quadrilateral"
        elif corners == 5:
            shape = "Pentagon"
        elif corners == 6:
            shape = "Hexagon"
        else:
            shape = "Circle"

        cv2.putText(image, shape, (cv2.boundingRect(approx)[0], cv2.boundingRect(approx)[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

    cv2.imshow('Shape Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Image/approximated_shapes.jpeg', image)