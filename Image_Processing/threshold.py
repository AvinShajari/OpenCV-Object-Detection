import cv2


image = cv2.imread("image.jpg")

if image is None:
    print("Could not load image.")
    exit()


gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)


_, thresholded = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)


cv2.imshow("Grayscale", gray)
cv2.imshow("Threshold", thresholded)

cv2.waitKey(0)
cv2.destroyAllWindows()