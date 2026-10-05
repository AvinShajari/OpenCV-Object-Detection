import cv2


image = cv2.imread("image.jpg")

if image is None:
    print("Could not load image.")
    exit()


gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)


_, threshold = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)


contours, hierarchy = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)


output = image.copy()


cv2.drawContours(
    output,
    contours,
    -1,
    (0, 255, 0),
    2
)


print("Number of contours:", len(contours))


cv2.imshow(
    "Contours",
    output
)

cv2.waitKey(0)
cv2.destroyAllWindows()