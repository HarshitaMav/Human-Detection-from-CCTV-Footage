# 👁️‍🗨️ Human Tracking & Counting from CCTV Videos (Multi-Camera)

Track and count **unique humans** in **multiple simultaneous CCTV feeds** using **YOLOv8** for detection and **DeepSORT** for tracking. This system efficiently identifies individuals even across different camera angles, minimizing duplicates and false counts.

---

## 🔍 Features

✅ Multi-camera video processing (4 simultaneous feeds)  
✅ Human-only detection using YOLOv8  
✅ Accurate tracking with DeepSORT  
✅ Real-time count of unique individuals  
✅ Resilient to occlusion and background noise  
✅ Graceful interruption (Ctrl+C safe)  
✅ Outputs saved with bounding boxes and IDs

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

