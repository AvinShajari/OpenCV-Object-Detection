import cv2


image = cv2.imread("image.jpg")

if image is None:
    print("Could not load image.")
    exit()

cv2.imshow("Original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()