from dataclasses import dataclass
from typing import Optional


@dataclass
class Labels:
    dummy: Optional[str] = None

    verdict: bool = True
