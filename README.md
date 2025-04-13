# 👁️‍🗨️ Human Tracking & Counting from CCTV Videos (Multi-Camera)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Tracking-green?logo=github)
![DeepSORT](https://img.shields.io/badge/DeepSORT-MultiObjectTracking-orange)
![License](https://img.shields.io/github/license/HarshitaMav/Human-Detection-from-CCTV-Footage)
![Stars](https://img.shields.io/github/stars/HarshitaMav/Human-Detection-from-CCTV-Footage?style=social)

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
```
---

## ⚙️ How It Works

- **Detection**: `detector.py` uses YOLOv8 to detect people.  
- **Tracking**: `tracker.py` integrates DeepSORT to assign IDs.  
- **Counting**: `counter.py` keeps track of total unique people detected.  
- **Multi-threading**: `main.py` launches one thread per video file to parallelize processing.

---

## 📦 Dependencies

Install the required packages with:

```bash
pip install -r requirements.txt
```
Or install them individually:
```
pip install ultralytics opencv-python deep-sort-realtime torch
```
---

## 🛠️ Run the Project
Place your input videos inside the data/ folder and run:

```bash
python main.py
```
- Press **Ctrl+C** anytime to gracefully stop the processing.
- Processed videos will be saved in the output/ folder.

---

## 📌 Notes
- All video outputs are stored in the `output/` directory.
- Incomplete videos or forcefully terminated processing may corrupt `.mp4` files.
- Ensure input videos are readable and not locked by another process.
- Use `yolov8s.pt` or upgrade to larger models (e.g., `yolov8m.pt`) for better accuracy if GPU resources allow.

---

## ✨ Example Output
Each video feed shows:
- Bounding boxes on each detected person
- Real-time assigned ID
- Unique person count at the top left
- 
## 📸 Example Output
### 🎯 Person Detection + ID Assignment + Unique Person Count Display:
!(screenshots/Screenshot 2025-04-13 174626.png)
!(screenshots/Screenshot 2025-04-13 174851.png)

---

## 🤝 Contributions
Feel free to fork, enhance, or contribute! PRs and issues welcome.
