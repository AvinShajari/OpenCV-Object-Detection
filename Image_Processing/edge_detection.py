import cv2


image = cv2.imread("image.jpg")

if image is None:
    print("Could not load image.")
    exit()


gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)


edges = cv2.Canny(
    gray,
    100,
    200
)


cv2.imshow("Original", image)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()