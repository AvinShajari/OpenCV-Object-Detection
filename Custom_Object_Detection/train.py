from ultralytics import YOLO


# Load pretrained YOLOv8 model
model = YOLO("yolov8s.pt")


# Train custom model
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    workers=4
)


print("Training completed.")