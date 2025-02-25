# -*- coding: utf-8 -*-
"""Pseudocode(Group 7).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1my_7yWETBS1VmfDlsJ9FQSLiKVbgZ30k
"""

import cv2
import matplotlib.pyplot as plt

#Load a grayscale image
image = cv2.imread('grayscale 2.jpeg', cv2.IMREAD_GRAYSCALE)

#Apply the pseudocolor using OpenCV
colored_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)

#Display the grayscale and pseudocolor images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(colored_image)
plt.title('Pseudocolor Image(JET)')
plt.axis('off')

plt.show()

import cv2
import matplotlib.pyplot as plt

#Load a grayscale image
image = cv2.imread('grayscale 2.jpeg', cv2.IMREAD_GRAYSCALE)

#Apply the pseudocolor using OpenCV
colored_image = cv2.applyColorMap(image, cv2.COLORMAP_VIRIDIS)

#Display the grayscale and pseudocolor images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(colored_image)
plt.title('Pseudocolor Image(VIRIDIS)')
plt.axis('off')

plt.show()

import cv2
import matplotlib.pyplot as plt

#Load a grayscale image
image = cv2.imread('grayscale 2.jpeg', cv2.IMREAD_GRAYSCALE)

#Apply the pseudocolor using OpenCV
colored_image = cv2.applyColorMap(image, cv2.COLORMAP_PLASMA)

#Display the grayscale and pseudocolor images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(colored_image)
plt.title('Pseudocolor Image(PLASMA)')
plt.axis('off')

plt.show()

import cv2
import matplotlib.pyplot as plt

#Load a grayscale image
image = cv2.imread('grayscale 2.jpeg', cv2.IMREAD_GRAYSCALE)

#Apply the pseudocolor using OpenCV
colored_image = cv2.applyColorMap(image, cv2.COLORMAP_HOT)

#Display the grayscale and pseudocolor images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(colored_image)
plt.title('Pseudocolor Image(HOT)')
plt.axis('off')

plt.show()

import cv2
import matplotlib.pyplot as plt

#Load a grayscale image
image = cv2.imread('grayscale 2.jpeg', cv2.IMREAD_GRAYSCALE)

#Apply the pseudocolor using OpenCV
colored_image = cv2.applyColorMap(image, cv2.COLORMAP_COOL)

#Display the grayscale and pseudocolor images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(colored_image)
plt.title('Pseudocolor Image(COOL)')
plt.axis('off')

plt.show()