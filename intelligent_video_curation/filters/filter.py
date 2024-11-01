from typing import List

from intelligent_video_curation.classes.video import Video
from intelligent_video_curation.filters.dummy.dummy_filter import dummy_filter

filters = [dummy_filter]


def run(videos: List[Video]) -> List[Video]:
    for f in filters:
        for video in videos:
            f(video)

    return videos
