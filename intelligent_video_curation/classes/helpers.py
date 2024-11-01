from typing import Any, Dict

import dacite


def dict_to_class(*, data: Dict, class_: Any) -> Any:
    return dacite.from_dict(data_class=class_, data=data)
