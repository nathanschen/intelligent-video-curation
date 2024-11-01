from dataclasses import dataclass, field
from typing import Any, Dict, List

import numpy as np

from intelligent_video_curation.classes.labels import Labels


@dataclass
class Video:
    # these fields are filled-in during preprocessing

    path: str = field(default_factory=str)
    audio_path: str = field(default_factory=str)
    frames: List[np.ndarray] = field(default_factory=list, repr=False)
    # handy little thing. repr=false prevents this from being included in a dictionary-ifying operation
    # note, if you are gonna have a default factory to operate on it immediately
    # don't also have Optional or else mypy screams at you because it thinks it can be field | None

    metadata: Dict[Any, Any] = field(default_factory=dict)  # field function lets you define things like default values, factories, etc.

    # these fields are filled-in during filtering
    labels: Labels = field(default_factory=Labels)
