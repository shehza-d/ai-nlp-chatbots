import cv2

# Load the image
img = cv2.imread('image.jpg')

# Set the grid size and color
grid_size = 50
color = (0, 255, 0) # Green

# Draw the vertical lines
for x in range(0, img.shape[1], grid_size):
    cv2.line(img, (x, 0), (x, img.shape[0]), color, thickness=1)

# Draw the horizontal lines
for y in range(0, img.shape[0], grid_size):
    cv2.line(img, (0, y), (img.shape[1], y), color, thickness=1)

# Display the image with the grid
cv2.imshow("Grid", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
