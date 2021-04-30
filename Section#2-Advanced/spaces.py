import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('Weirdo', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_RGB2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)
