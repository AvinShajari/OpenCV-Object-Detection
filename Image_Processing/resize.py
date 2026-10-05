import cv2


image = cv2.imread("image.jpg")

if image is None:
    print("Could not load image.")
    exit()


width = 800
height = 600

resized = cv2.resize(
    image,
    (width, height)
)


cv2.imshow("Original", image)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()