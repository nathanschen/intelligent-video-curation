from dataclasses import dataclass


@dataclass
class Labels:
    exposure: str = "correct"
    dummy: str = ""
    verdict: bool = True


# please add any relevant labels to your filters here. labels may not always be the same as
# curation parameters. follow the format examples.
