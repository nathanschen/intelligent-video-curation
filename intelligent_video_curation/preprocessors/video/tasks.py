import os
import subprocess
from typing import List

import cv2

from intelligent_video_curation.classes.config import GlobalConfig
from intelligent_video_curation.classes.video import Video
from intelligent_video_curation.helpers.files import create_temp_file


def discover_videos() -> List[str]:
    video_extensions = (".mp4", ".avi", ".mov", ".mkv")

    dir_ = GlobalConfig.input.directory
    return [os.path.join(dir_, f) for f in os.listdir(dir_) if f.endswith(video_extensions) and dir_ is not None]


def fill_audio(videos: List[Video]) -> None:
    for video in videos:
        video.audio_path = create_temp_file(".mp3")
        command = ["ffmpeg", "-i", video.path, "-vn", "-y", "-acodec", "mp3", video.audio_path]

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")  # noqa: T201


def fill_frames(videos: List[Video]) -> None:
    for video in videos:
        cap = cv2.VideoCapture(video.path)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            video.frames.append(frame)  # Append each frame as a numpy array

        cap.release()
