# Dictionary to track IDs for each video
video_id_sets = {}

def update_ids_and_count(video_index, current_ids, total_ids):
    if video_index not in video_id_sets:
        video_id_sets[video_index] = set()

    video_set = video_id_sets[video_index]

    # Add new IDs
    for track_id in current_ids:
        if track_id not in video_set:
            video_set.add(track_id)
            total_ids.add(track_id)

    # Remove IDs that disappeared
    removed = video_set - current_ids
    video_set -= removed
    total_ids -= removed
