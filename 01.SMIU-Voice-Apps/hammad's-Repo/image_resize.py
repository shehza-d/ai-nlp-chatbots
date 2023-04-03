import cv2

# Load the image
img = cv2.imread('image.jpg')

# Set the new dimensions
width = 500
height = 300
dim = (width, height)

# Resize the image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# Display the original and resized images
cv2.imshow("Original", img)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
