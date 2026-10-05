
from ultralytics import YOLO
import cv2
import time
import os


# =========================
# Load YOLOv8 model
# =========================

model = YOLO("yolov8s.pt")


# =========================
# Detection function
# =========================

def detect_frame(frame):
    results = model.predict(
        source=frame,
        imgsz=640,
        conf=0.25,
        iou=0.45,
        max_det=100,
        verbose=False
    )

    output = results[0].plot()

    return output


# =========================
# Webcam
# =========================

def webcam_detection():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open webcam.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    previous_time = time.time()

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Could not read webcam frame.")
            break

        output = detect_frame(frame)

        current_time = time.time()

        fps = 1 / max(
            current_time - previous_time,
            0.001
        )

        previous_time = current_time

        cv2.putText(
            output,
            f"FPS: {fps:.1f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "YOLOv8 Webcam Detection",
            output
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# =========================
# Image
# =========================

def image_detection():

    image_path = "Object_Detection/images/image.jpg"

    if not os.path.exists(image_path):
        print("Image not found:")
        print(image_path)
        return

    image = cv2.imread(image_path)

    if image is None:
        print("Could not load image.")
        return

    output = detect_frame(image)

    cv2.imshow(
        "YOLOv8 Image Detection",
        output
    )

    print("Press Q or any key to close.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# =========================
# Video
# =========================

def video_detection():

    video_path = "Object_Detection/videos/video.mp4"

    if not os.path.exists(video_path):
        print("Video not found:")
        print(video_path)
        return

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Could not open video.")
        return

    previous_time = time.time()

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        output = detect_frame(frame)

        current_time = time.time()

        fps = 1 / max(
            current_time - previous_time,
            0.001
        )

        previous_time = current_time

        cv2.putText(
            output,
            f"FPS: {fps:.1f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "YOLOv8 Video Detection",
            output
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# =========================
# Main Menu
# =========================

print()
print("==============================")
print("     YOLOv8 Object Detection")
print("==============================")
print()
print("1 - Webcam")
print("2 - Image")
print("3 - Video")
print("0 - Exit")
print()

choice = input("Select input: ")


if choice == "1":

    webcam_detection()

elif choice == "2":

    image_detection()

elif choice == "3":

    video_detection()

elif choice == "0":

    print("Program closed.")

else:

    print("Invalid choice.")
