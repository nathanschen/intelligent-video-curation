import json
from dataclasses import asdict

from intelligent_video_curation.classes.config import GlobalConfig
from intelligent_video_curation.classes.video import Video


def output(videos: list[Video]) -> None:
    total = []
    for video in videos:
        dict_ = asdict(video)  # handy little thing. this recurses.
        for exclude in ["audio_path", "frames", "metadata"]:
            dict_.pop(exclude, None)
        total.append(dict_)
    if GlobalConfig.internal.output_json_path is not None:
        with open(GlobalConfig.internal.output_json_path, "w", encoding="utf-8") as json_file:
            json.dump(total, json_file, indent=4)
