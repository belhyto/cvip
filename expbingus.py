import cv2

# Load the image
img = cv2.imread("flower.png")
if img is None:
    print("Error: Failed to load the image.")
    exit()

# Resize the image
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

# Rotate the image
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize the grayscale image
resized_gray_img = cv2.resize(gray_img, (512, 512))

# Rotate the resized grayscale image
rotated_gray_img = cv2.rotate(resized_gray_img, cv2.ROTATE_90_CLOCKWISE)

# Display the original image
cv2.imshow("Original Image", img)

# Display the rotated grayscale image
cv2.imshow("Rotated Grayscale Image", rotated_gray_img)

# Wait until any key is pressed and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
