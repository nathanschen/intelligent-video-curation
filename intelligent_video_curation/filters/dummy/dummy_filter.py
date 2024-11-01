from intelligent_video_curation.classes.config import GlobalConfig
from intelligent_video_curation.classes.video import Video


def dummy_filter(video: Video) -> None:
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
