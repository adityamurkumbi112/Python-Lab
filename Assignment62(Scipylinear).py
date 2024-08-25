import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image from a URL (alternatively, you can load from a local file)
url = r'C:\Users\Aditya\Downloads\DANLC-master\DANLC-master\dog.jpg'
original_image = cv2.imread(url, cv2.IMREAD_COLOR)

# If reading from local file, use:
# original_image = cv2.imread('path_to_your_image.jpg')

# Check if the image was loaded
if original_image is None:
    print("Error: Could not load image")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filter
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)  # Sobel filter in x direction
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)  # Sobel filter in y direction
    sobel_combined = cv2.magnitude(sobelx, sobely)  # Magnitude of the gradient

    # Display the images
    plt.figure(figsize=(12, 6))
    
    # Display the original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Display the Sobel filtered image
    plt.subplot(1, 2, 2)
    plt.imshow(sobel_combined, cmap='viridis')
    plt.title('Filtered Image (Sobel Filter)')
    plt.axis('off')

    plt.show()
