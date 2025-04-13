from deep_sort_realtime.deepsort_tracker import DeepSort

def create_tracker():
    tracker = DeepSort(
        max_age=15,
        n_init=2,
        nn_budget=70,
        max_iou_distance=0.7,
        embedder="mobilenet",  # or torchreid or clip_RN50
        half=True,
        bgr=True
    )
    return tracker

