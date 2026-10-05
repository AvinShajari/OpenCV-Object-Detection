# OpenCV & YOLOv8 Computer Vision

A practical Computer Vision project built with Python, OpenCV, and YOLOv8.

This project contains examples of image processing, real-time object detection, object tracking, and custom YOLOv8 model training.

## Features

* Image reading and visualization
* Image resizing
* Grayscale conversion
* Gaussian blur
* Thresholding
* Edge detection with Canny
* Contour detection
* Real-time object detection with YOLOv8
* Real-time object tracking with ByteTrack
* Custom object detection training

## Technologies

* Python
* OpenCV
* YOLOv8
* Ultralytics
* ByteTrack

## Installation

Clone the repository:

```bash
git clone https://github.com/AvinShajari/OpenCV.git
cd OpenCV
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Object Detection

Run YOLOv8 object detection:

```bash
python Object_Detection/yolov8_detection.py
```

The program uses the webcam and detects objects in real time.

Press `Q` to exit.

## Object Tracking

Run YOLOv8 object tracking with ByteTrack:

```bash
python Object_Tracking/yolov8_tracking.py
```

The program detects and tracks objects in real time and assigns tracking IDs to detected objects.

Press `Q` to exit.

## Image Processing

The `Image_Processing` directory contains basic OpenCV examples:

* `read_image.py`
* `resize.py`
* `grayscale.py`
* `blur.py`
* `threshold.py`
* `edge_detection.py`
* `contours.py`

## Custom Object Detection

The `Custom_Object_Detection` directory contains the files required for training a custom YOLOv8 model.

```text
Custom_Object_Detection/
├── train.py
└── data.yaml
```

The custom dataset can contain classes such as:

* Phone
* Laptop
* Bottle

## Project Structure

```text
OpenCV/
│
├── Custom_Object_Detection/
│   ├── train.py
│   └── data.yaml
│
├── Image_Processing/
│   ├── read_image.py
│   ├── resize.py
│   ├── grayscale.py
│   ├── blur.py
│   ├── threshold.py
│   ├── edge_detection.py
│   └── contours.py
│
├── Object_Detection/
│   └── yolov8_detection.py
│
├── Object_Tracking/
│   └── yolov8_tracking.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Future Improvements

* Custom YOLOv8 datasets
* Improved object detection accuracy
* More advanced object tracking
* Image and video input support
* GPU acceleration
* Additional Computer Vision algorithms

## Author

**Avin Shajari**

GitHub: https://github.com/AvinShajari
