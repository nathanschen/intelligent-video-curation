import atexit
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import yaml

from intelligent_video_curation.classes.config import GlobalConfig


def load_yaml(config_path: str) -> Dict[Any, Any]:
    path = Path(config_path)
    with path.open("r") as file:
        return yaml.safe_load(file)


def create_output_json() -> None:
    GlobalConfig.internal.output_json_path = f"{GlobalConfig.output.directory}/curation_results_{datetime.now().strftime('%Y-%m-%d-%H-%S')}.json"


def create_temp_file(suffix: str = "") -> str:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)  # noqa: SIM115
    temp_file_path = temp_file.name
    temp_file.close()
    atexit.register(lambda: os.remove(temp_file_path) if os.path.exists(temp_file_path) else None)
    return temp_file_path
