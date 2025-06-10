from numbers import Number
from typing import Any


def get_required_field(data: Any, field: str,) -> Any:
    value = data.get(field)
    if value is None or value == "":
        raise ValueError(f"{field} is required but missing")
    return value

# TODO: return default value
def get_optional_field(data: Any, field: str,) -> Any:
    value = data.get(field)
    if value is None or value == "":
        return None
    return value

def mask_email(email: str) -> str:
    main , domain = email.split("@", maxsplit= 1)
    if len(main) > 3:
        new_main = main[0:3] + "****"
    else:
        new_main = "****"
    return new_main + "@" + domain