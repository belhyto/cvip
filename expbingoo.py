import cv2
import matplotlib.pyplot as plt

# Assuming the image 'grains.jpg' is in the same directory as this script
image_path = 'grains.jpg'

# Read the image
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print("Error: Cannot find the image")
else:
    # Display the image using Matplotlib
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Turn off axis labels
    plt.show()
