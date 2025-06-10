from datetime import datetime
from typing import Any, Type


def safe_cast_to_int(
    field: str, field_name: str, fail_mode: str = "fail", default_value: int = 0
) -> int:
    return safe_cast(field, int, field_name, fail_mode, default_value)


def safe_cast_to_float(
    field: str, field_name: str, fail_mode: str = "fail", default_value: float = 0.0
) -> float:
    return safe_cast(field, float, field_name, fail_mode, default_value)


def safe_cast_to_datetime(
    field: str, field_name: str, fail_mode: str = "fail", default_value: datetime = None
) -> datetime:
    return safe_cast(field, datetime, field_name, fail_mode, default_value)


def safe_cast(
    field: str,
    cast_type: Type,
    field_name: str,
    fail_mode: str = "fail",
    default_value: Any = None,
) -> Any:
    supported_types = {int, float, datetime}
    if cast_type not in supported_types:
        raise TypeError(f"Unsupported cast_type: {cast_type.__name__}")

    try:
        if cast_type == datetime:
            return datetime.fromisoformat(field)
        else:
            return cast_type(field)
    except (ValueError, TypeError):
        if fail_mode == "fail":
            raise ValueError(
                f"Cannot cast field '{field_name}' with value '{field}' to {cast_type.__name__}"
            )
        elif fail_mode == "default_if_failed":
            return default_value
        else:
            raise ValueError(f"Unknown fail mode: {fail_mode}")
