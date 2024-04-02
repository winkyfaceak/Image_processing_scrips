import sys
import os
import cv2

print("Please enter the file location of the image to convert to grayscale!")
while True:
    image_location = input("The location: ")
    if os.path.isfile(image_location):
        break
    else:
        print("Invalid file location. Please try again.")

# Load the input image
img = cv2.imread(image_location)

# Obtain the dimensions of the image array using the shape method
(row, col) = img.shape[0:2]

# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        img[i, j] = sum(img[i, j]) * 0.33

print("Do you wish to save the image?")
while True:
    try:
        in1 = int(input("1 to save, 2 for no: "))  # Convert input to integer
        if in1 == 1 or in1 == 2:
            break
        else:
            print("Invalid input. Please enter either 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if in1 == 1:
    default_path = os.path.expanduser("~/Pictures/Grayscale")
    os.makedirs(default_path, exist_ok=True)  # Create the directory if it doesn't exist
    in3 = input("Please enter an image name: ")
    cv2.imwrite(os.path.join(default_path, in3 + '.jpg'), img)
    print("Saved in default path: " + default_path)
elif in1 == 2:
    sys.exit()