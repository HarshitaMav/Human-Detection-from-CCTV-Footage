# 👁️‍🗨️ Human Tracking & Counting from CCTV Videos (Multi-Camera)

🧠 Track and count **unique humans** in **multiple simultaneous CCTV feeds** using **YOLOv8** for detection and **DeepSORT** for tracking. This system efficiently identifies individuals even across different camera angles, minimizing duplicates and false counts.

---

## 🔍 Features

✅ Multi-camera video processing (4 simultaneous feeds)  
✅ Human-only detection using YOLOv8  
✅ Accurate tracking with DeepSORT  
✅ Real-time count of unique individuals  
✅ Resilient to occlusion and background noise  
✅ Graceful interruption (Ctrl+C safe)  
✅ Outputs saved with bounding boxes and IDs in the folder `/output/`

---

## 🧠 Tech Stack

| Component   | Tool               |
|-------------|--------------------|
| Object Detection | [YOLOv8](https://github.com/ultralytics/ultralytics) - `yolov8s.pt` |
| Object Tracking  | DeepSORT (`ByteTrack`-style tracking via Norfair/BoT-SORT logic) |
| Programming Language | Python |
| Visualization | OpenCV |
| Parallelism | Threading |

---

## 📁 Project Structure

```plaintext
├── main.py                # Main execution script (multi-threaded)
├── models/
│   └── yolov8s.pt         # YOLOv8 weights
├── data/
│   ├── video1.mp4
│   ├── video2.mp4
│   ├── video3.mp4
│   └── video4.mp4
├── output/                # Processed output videos
├── utils/
│   ├── detector.py        # YOLO detection logic
│   ├── tracker.py         # DeepSORT tracker initialization
│   └── counter.py         # ID tracking and counting logic
└── README.md

## ⚙️ How It Works

- **Detection**: `detector.py` uses YOLOv8 to detect people.  
- **Tracking**: `tracker.py` integrates DeepSORT to assign IDs.  
- **Counting**: `counter.py` keeps track of total unique people detected.  
- **Multi-threading**: `main.py` launches one thread per video file to parallelize processing.
