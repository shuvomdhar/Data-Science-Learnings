import cv2

image = cv2.imread(r"Assignment/Task2/cover.jpeg")

# function to draw a line in the image
def line_in_image():
    if image is not None:
        height, width, connections = image.shape
        print(f"The height of the image is {height}, the width of the image is {width} and the connections of the image is {connections}\n")

        x1 = int(input("Enter the x1 coordinate of the line: "))
        y1 = int(input("Enter the y1 coordinate of the line: "))
        pt1 = (x1, y1)

        x2 = int(input("Enter the x2 coordinate of the line: "))
        y2 = int(input("Enter the y2 coordinate of the line: "))
        pt2 = (x2, y2)

        b = int(input("Enter the color(B) of BGR: "))
        g = int(input("Enter the color(G) of BGR: "))
        r = int(input("Enter the color(R) of BGR: "))
        color = (b, g, r)

        thickness = int(input("Enter the thickness of the line: "))

        line_image = cv2.line(image, pt1, pt2, color, thickness)
        show_image(line_image)
    else:
        print("Could not load image")

# function to draw a circle in the image
def circle_in_image():
    if image is not None:
        height, width, connections = image.shape
        print(f"The height of the image is {height}, the width of the image is {width} and the connections of the image is {connections}\n")

        x = int(input("Enter the x coordinate of the circle: "))
        y = int(input("Enter the y coordinate of the circle: "))
        center = (x, y)

        radius = int(input("Enter the radius of the circle: "))

        b = int(input("Enter the color(B) of BGR: "))
        g = int(input("Enter the color(G) of BGR: "))
        r = int(input("Enter the color(R) of BGR: "))
        color = (b, g, r)

        thickness = int(input("Enter the thickness of the circle(-1 / 0 / 1): "))

        circle_image = cv2.circle(image, center, radius, color, thickness)
        show_image(circle_image)
    else:
        print("Could not load image")

# function to draw a rectangle in the image
def rectangle_in_image():
    if image is not None:
        height, width, connections = image.shape
        print(f"The height of the image is {height}, the width of the image is {width} and the connections of the image is {connections}\n")

        x1 = int(input("Enter the x1 coordinate of the rectangle: "))
        y1 = int(input("Enter the y1 coordinate of the rectangle: "))
        pt1 = (x1, y1)

        x2 = int(input("Enter the x2 coordinate of the rectangle: "))
        y2 = int(input("Enter the y2 coordinate of the rectangle: "))
        pt2 = (x2, y2)

        b = int(input("Enter the color(B) of BGR: "))
        g = int(input("Enter the color(G) of BGR: "))
        r = int(input("Enter the color(R) of BGR: "))
        color = (b, g, r)

        thickness = int(input("Enter the thickness of the rectangle: "))

        rectangle_image = cv2.rectangle(image, pt1, pt2, color, thickness)
        show_image(rectangle_image)
    else:
        print("Could not load image")

# function to draw a text in the image
def text_in_image():
    if image is not None:
        height, width, connections = image.shape
        print(f"The height of the image is {height}, the width of the image is {width} and the connections of the image is {connections}\n")

        text = input("Enter the text which will appear on the image: ")

        x = int(input("Enter the x coordinate of the text: "))
        y = int(input("Enter the y coordinate of the text: "))
        origin = (x, y)

        b = int(input("Enter the color(B) of BGR: "))
        g = int(input("Enter the color(G) of BGR: "))
        r = int(input("Enter the color(R) of BGR: "))
        color = (b, g, r)

        fontscale = float(input("Enter the font scale of the text: "))

        thickness = int(input("Enter the thickness of the text: "))

        text_image = cv2.putText(image, text, origin, cv2.FONT_HERSHEY_COMPLEX, fontscale, color, thickness)
        show_image(text_image)
    else:
        print("Could not load image")

# function to save the image
def save_image(image_name):
    save_image_name = input("Enter the name of the image to save it with extension(ex: .jpeg, .png etc.): ")
    saved_image = cv2.imwrite(f"Assignment/Task2/{save_image_name}", image_name)
    if saved_image is not None:
        print("Image saved successfully")
    else:
        print("Couldn't save image")

# function to show the output image
def show_image(result_image):
    image_name = input("Enter the name of the image: ")
    cv2.imshow(f"{image_name}", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # call the save function
    user_input = input("Do you want to save it?\nType - \"y or yes\" if YES else type - \"n or no\": ")
    if user_input.lower() == "y" or "yes":
        save_image(result_image)
    else:
        pass

# main function to take user input
def main():
    print("What does you want to do?\n1. Do you want to draw a line? - \"Press 1\"\n2. Do you want to draw a circle? - \"Press 2\"\n3. Do you want to draw a rectangle? - \"Press 3\"\n4. Do you want to draw a text? - \"Press 4\"")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            line_in_image()
        case 2:
            circle_in_image()
        case 3:
            rectangle_in_image()
        case 4:
            text_in_image()
        case _:
            print("Invalid Choice\n")

# Call the main function
main()