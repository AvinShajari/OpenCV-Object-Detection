from ultralytics import YOLO
import cv2
import time


# Load YOLOv8 model
model = YOLO("yolov8s.pt")


# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


previous_time = 0


while True:

    ret, frame = cap.read()

    if not ret:
        break


    # YOLO tracking
    results = model.track(
        source=frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.35,
        iou=0.5,
        imgsz=640,
        verbose=False
    )


    # Draw tracking results
    output = results[0].plot()


    # Calculate FPS
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
        "YOLOv8 Object Tracking",
        output
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()