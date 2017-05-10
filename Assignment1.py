from Tkinter import *
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

def original():
    cv2.imshow("Image", original_image)

def gray():
    cv2.imshow("Image", gray_image)

def histogram():
    plt.clf()
    plt.hist(gray_image.ravel(), 256, [0, 256])
    plt.show()

def adjust_gamma(image):
    gamma = 2.2
    invGamma = 1.0 / gamma
    gamma_table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, gamma_table)

def histogram_gamma():
    plt.clf()
    plt.hist(gray_gamma_image.ravel(), 256, [0, 256])
    plt.show()

def adjust_solarization(image):
    const_solarization = 2 * np.pi / 255
    solarization_table = np.array([np.abs(np.sin(i * const_solarization)) * 100 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, solarization_table)

def solarized():
    cv2.imshow("Image", solarized_image)
    plt.clf()
    plt.hist(solarized_image.ravel(), 256, [0, 256])
    plt.show()

def adjust_posterization1(image):
    posterization1_table = np.array([0 for i in np.arange(0, 256)]).astype("uint8")
    for i in np.arange(0, 256):
        if i < 64:
            posterization1_table[i] = 0
        elif i < 128:
            posterization1_table[i] = 100
        elif i < 192:
            posterization1_table[i] = 200
        else:
            posterization1_table[i] = 300
    return cv2.LUT(image, posterization1_table)

def posterized1():
    cv2.imshow("Image", posterized1_image)
    plt.clf()
    plt.hist(posterized1_image.ravel(), 256, [0, 256])
    plt.show()

def adjust_posterization2(image):
    posterization2_table = np.array([0 for i in np.arange(0, 256)]).astype("uint8")
    for i in np.arange(0, 256):
        if i < 32:
            posterization2_table[i] = 0
        elif i < 64:
            posterization2_table[i] = 100
        elif i < 96:
            posterization2_table[i] = 200
        elif i < 128:
            posterization2_table[i] = 300
        elif i < 160:
            posterization2_table[i] = 400
        elif i < 192:
            posterization2_table[i] = 500
        elif i < 224:
            posterization2_table[i] = 600
        else:
            posterization2_table[i] = 700
    return cv2.LUT(image, posterization2_table)

def posterized2():
    cv2.imshow("Image", posterized2_image)
    plt.clf()
    plt.hist(posterized2_image.ravel(), 256, [0, 256])
    plt.show()

def adjust_dithering1(image):
    a = np.matrix(image)
    b = np.matrix('0 2; 3 1')
    for x in range(0, 665): # columns
        for y in range(0, 1000): # rows
            a[x,y] = int(a[x,y]/52)
            i = x % 2
            j = y % 2
            if a[x,y] > b[i,j]:
                a[x,y] = 255
            else:
                a[x,y] = 0
    return a

def dithered1():
    cv2.imshow("Image", dithered1_image)
    plt.clf()
    plt.hist(dithered1_image.ravel(), 256, [0, 256])
    plt.show()

def adjust_dithering2(image):
    a = np.matrix(image)
    b = np.matrix('0 7 3; 6 5 2; 4 1 8')
    for x in range(0, 665): # columns
        for y in range(0, 1000): # rows
            a[x,y] = int(a[x,y]/52)
            i = x % 3
            j = y % 3
            if a[x,y] > b[i,j]:
                a[x,y] = 255
            else:
                a[x,y] = 0
    return a

def dithered2():
    cv2.imshow("Image", dithered2_image)
    plt.clf()
    plt.hist(dithered2_image.ravel(), 256, [0, 256])
    plt.show()

def adjust_dithering3(image):
    a = np.matrix(image)
    b = np.matrix('0 8 2 10; 12 4 14 6; 3 11 1 9; 15 7 13 5')
    for x in range(0, 665): # columns
        for y in range(0, 1000): # rows
            a[x,y] = int(a[x,y]/52)
            i = x % 4
            j = y % 4
            if a[x,y] > b[i,j]:
                a[x,y] = 255
            else:
                a[x,y] = 0
    return a

def dithered3():
    cv2.imshow("Image", dithered3_image)
    plt.clf()
    plt.hist(dithered3_image.ravel(), 256, [0, 256])
    plt.show()

app = Tk()
app.title("Window")

image_name = "Fox.jpg"
original_image = cv2.imread(image_name)

gray_image = cv2.imread(image_name, 0)

gamma_adjusted = adjust_gamma(gray_image)
cv2.imwrite("gamma.jpg", gamma_adjusted)
gray_gamma_image = cv2.imread("gamma.jpg")

solarization_adjusted = adjust_solarization(gray_image)
cv2.imwrite("solarized.jpg", solarization_adjusted)
solarized_image = cv2.imread("solarized.jpg")

posterization1_adjusted = adjust_posterization1(gray_image)
cv2.imwrite("posterized1.jpg", posterization1_adjusted)
posterized1_image = cv2.imread("posterized1.jpg")

posterization2_adjusted = adjust_posterization2(gray_image)
cv2.imwrite("posterized2.jpg", posterization2_adjusted)
posterized2_image = cv2.imread("posterized2.jpg")

dithering1_adjusted = adjust_dithering1(gray_image)
cv2.imwrite("dithered1.jpg", dithering1_adjusted)
dithered1_image = cv2.imread("dithered1.jpg")

dithering2_adjusted = adjust_dithering2(gray_image)
cv2.imwrite("dithered2.jpg", dithering2_adjusted)
dithered2_image = cv2.imread("dithered2.jpg")

dithering3_adjusted = adjust_dithering3(gray_image)
cv2.imwrite("dithered3.jpg", dithering3_adjusted)
dithered3_image = cv2.imread("dithered3.jpg")

original_button = Button(app, text="Display Original Image", command=original)
gray_button = Button(app, text="Display Grayscale Image", command=gray)
histogram_button = Button(app, text="Display Histogram For Grayscale Image", command=histogram)
histogram_gamma_button = Button(app, text="Display Histogram For Grayscale Image After Gamma Correction", command=histogram_gamma)
solarization_button = Button(app, text="Display Histogram For Grayscale Image After Solarization And The Solarized Image", command=solarized)
posterization1_button = Button(app, text="Display Histogram For Grayscale Image After Posterization1 And The Posterized Image", command=posterized1)
posterization2_button = Button(app, text="Display Histogram For Grayscale Image After Posterization2 And The Posterized Image", command=posterized2)
dithering1_button = Button(app, text="Display Histogram For Grayscale Image After 2 x 2 Dithering And The Dithered Image", command=dithered1)
dithering2_button = Button(app, text="Display Histogram For Grayscale Image After 3 x 3 Dithering And The Dithered Image", command=dithered2)
dithering3_button = Button(app, text="Display Histogram For Grayscale Image After 4 x 4 Dithering And The Dithered Image", command=dithered3)

original_button.pack()
gray_button.pack()
histogram_button.pack()
histogram_gamma_button.pack()
solarization_button.pack()
posterization1_button.pack()
posterization2_button.pack()
dithering1_button.pack()
dithering2_button.pack()
dithering3_button.pack()

app.mainloop()
