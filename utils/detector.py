from ultralytics import YOLO
import cv2
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load and fuse model only ONCE
model = YOLO('models/yolov8s.pt')
model.fuse()
model.to(device)

def detect_people(frame):
    resized_frame = cv2.resize(frame, (640, 640))
    results = model(resized_frame, verbose=False)[0]
    detections = []

    for box in results.boxes:
        cls = int(box.cls[0])
        if cls == 0:  # Only detect persons
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            detections.append(([x1, y1, x2, y2], conf, cls))

    return detections
