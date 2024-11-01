from intelligent_video_curation.classes.config import GlobalConfig
from intelligent_video_curation.helpers.files import create_output_json, load_yaml


def setup(config: str) -> None:
    dict_ = load_yaml(config_path=config)
    GlobalConfig.initialize_from_dict(dict_)
    create_output_json()
