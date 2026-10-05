import cv2


image = cv2.imread("image.jpg")

if image is None:
    print("Could not load image.")
    exit()


blurred = cv2.GaussianBlur(
    image,
    (7, 7),
    0
)


cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()