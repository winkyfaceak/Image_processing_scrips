# Import opencv
import sys

import cv2

print("Please enter the file location of the image to convert to grayscale!")
image_location = input("The location: ")

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
in2 = int(input("1 to save, 2 for no: "))  # Convert input to integer
if in2 == 1:
    in3 = input("Please enter an image name: ")
    cv2.imwrite(in3 + '.jpg', img)  # Save as JPEG

elif in2 == 2:
    sys.exit()