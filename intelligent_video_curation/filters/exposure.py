from intelligent_video_curation.classes.config import GlobalConfig
from intelligent_video_curation.classes.video import Video
import numpy as np
import cv2 as cv


def exposure(video: Video) -> None:
    # Step 0: identify the parameters & valid filtering values you'd like to support, such as
    # emotion: happy, sad
    # pose: extreme, frontal
    # Then add a field in Parameters class in config.py, and config.yaml.
    # user input in config.yaml will populate the corresponding parameter in Parameters(),
    # which you can then access as GlobalConfig.curation_parameters._____
    # also add any relevant label fields in Labels class in labels.py

    # Step 1: access & check out the video
    video.audio_path  # do whatever analysis... # noqa: B018
    video.frames  # do whatever analysis... # noqa: B018
    video.path  # do whatever analysis... # noqa: B018

    # Step 2: Apply any labels
    video.labels.dummy = "very"

    # Step 3: determine the verdict for inclusion
    # access the parameter that you added to config.py as follows...
    # this will be populated by the yaml file input.
    GlobalConfig.curation_parameters.dummy  # noqa: B018

    # Step 4: Apply the verdict
    # if the analysis indicates the video should be excluded, set verdict to false
    video.labels.verdict = False

    """
    Determines if an image is overexposed based on pixel intensity.

    Parameters:
    - image: np.array, input image
    - threshold: int, intensity threshold to consider pixels as bright (default 20 away from 0 or 255).
    - overexposure_ratio: float, % of pixels above threshold.
    - underexposure_ratio: float, % of pixels below threshold.

    Returns:
    - o: if the image is overexposed.
    - u: if the image is underexposed.
    - c: if the image is exposed correctly.
    """

    threshold=20
    overexposure_ratio=0.3
    underexposure_ratio=0.3


    video_exposures = np.empty(len(video.frames), dtype = str)
    for frame, i in video.frames, range(len(video.frames)):
        output = ""
        gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        total_pixels = gray_image.size

        overexposed_pixels = np.sum(gray_image >= 255-threshold)
        underexposed_pixels = np.sum(gray_image <= threshold)

        over_image_ratio = overexposed_pixels / total_pixels
        under_image_ratio = underexposed_pixels / total_pixels

        if over_image_ratio > overexposure_ratio:
            output = 'o'
        elif under_image_ratio > underexposure_ratio:
            output = 'u'
        else:
            output = 'c'
        
        video_exposures[i] = output

    values, counts = np.unique(video_exposures, return_counts=True)
    
    if counts[1] > counts[0]:
        video.labels.exposure = "over"
    if counts[2] > counts[0]:
        video.labels.exposure = "under"

    if video.labels.exposure == GlobalConfig.curation_parameters.exposure:
        video.labels.verdict = True

    

    
