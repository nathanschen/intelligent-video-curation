from typing import List

from intelligent_video_curation.classes.video import Video
from intelligent_video_curation.preprocessors.video.tasks import discover_videos, fill_audio, fill_frames


def run() -> List[Video]:
    raw_video_paths = discover_videos()
    videos: List[Video] = [Video(path=path) for path in raw_video_paths]
    fill_audio(videos)
    fill_frames(videos)

    return videos
