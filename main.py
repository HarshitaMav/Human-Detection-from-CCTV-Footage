import cv2
import threading
import os
from utils.detector import detect_people
from utils.tracker import create_tracker
from utils.counter import update_ids_and_count
import signal
import sys

# Create output directory
os.makedirs("output", exist_ok=True)

video_paths = [
    "data/video1.mp4",
    "data/video2.mp4",
    "data/video3.mp4",
    "data/video4.mp4"
]

# Global flag to stop threads
stop_flag = False

def signal_handler(sig, frame):
    global stop_flag
    print("\n[INFO] Ctrl+C detected! Gracefully stopping all threads...")
    stop_flag = True

# Attach the signal handler
signal.signal(signal.SIGINT, signal_handler)

def process_video(video_path, idx):
    global stop_flag

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERROR] Cannot open video file: {video_path}")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0.0 or fps is None:
        print(f"[WARNING] FPS not found for {video_path}, defaulting to 30")
        fps = 30.0

    out_path = f"output/out_video{idx+1}.mp4"
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    if not out.isOpened():
        print(f"[ERROR] Failed to open VideoWriter for {out_path}")
        cap.release()
        return

    tracker = create_tracker()
    active_ids = set()
    total_ids = set()

    print(f"[INFO] Processing Video {idx+1}: {video_path}")

    while cap.isOpened() and not stop_flag:
        ret, frame = cap.read()
        if not ret or frame is None:
            print(f"[INFO] Video {idx+1} ended or cannot read frame.")
            break

        detections = detect_people(frame)
        tracks = tracker.update_tracks(detections, frame=frame)
        active_ids.clear()

        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            l, t, r, b = map(int, track.to_ltrb())
            cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {track_id}", (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            active_ids.add(track_id)

        update_ids_and_count(idx, active_ids, total_ids)
        cv2.putText(frame, f"Unique Count: {len(total_ids)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        out.write(frame)
        cv2.imshow(f"Video {idx+1}", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyWindow(f"Video {idx+1}")
    print(f"[INFO] Video {idx+1} processing complete. Output saved to: {out_path}")

# Launch threads
threads = []
for i, path in enumerate(video_paths):
    thread = threading.Thread(target=process_video, args=(path, i))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

cv2.destroyAllWindows()
print("[INFO] All threads completed or interrupted. Exiting.")

