from dataclasses import dataclass, field
from typing import Dict, Optional

from intelligent_video_curation.classes.helpers import dict_to_class


@dataclass
class Parameters:
    dummy: Optional[str] = None
    model: Optional[str] = None
    min_face_size: Optional[int] = None

    emotion: Optional[str] = None


# Please add any new parameters here. These will be populated from config.yaml.
# follow the format shown.


@dataclass
class Input:
    directory: Optional[str] = None


@dataclass
class Output:
    directory: Optional[str] = None


@dataclass
class Internal:
    output_json_path: Optional[str] = None


@dataclass
class Config:
    input: Input = field(default_factory=Input)
    curation_parameters: Parameters = field(default_factory=Parameters)
    output: Output = field(default_factory=Output)

    internal: Internal = field(default_factory=Internal)

    def initialize_from_dict(self, data: Dict) -> None:
        updated_instance = dict_to_class(data=data, class_=Config)
        self.__dict__.update(updated_instance.__dict__)


GlobalConfig: Config = Config()
