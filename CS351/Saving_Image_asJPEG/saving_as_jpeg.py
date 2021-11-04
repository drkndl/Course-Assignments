import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

# Read the image
img = cv.imread('aircraft.png')
print(img.shape)
plt.imshow(img)
plt.show()


# Show the image using matplotlib
cv.imshow('original', img)


# Cropping an image [y, x]
cropped_image = img[210:310, 150:300]


# Display cropped image
cv.imshow('cropped', cropped_image)
cv.waitKey(15000)
cv.destroyAllWindows()

# SAVING THE IMAGE AS A JPEG FILE
cv.imwrite('cropped.jpeg', cropped_image)