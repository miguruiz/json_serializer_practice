from numbers import Number
from typing import Any, Callable

from exercise_2.models import Status


def validate_email(email: str) -> str:
    if email.count("@") > 1: # TODO: use regex
        return None
    else:
        return email

def validate_is_non_negative(number: Number, field_name: str) -> bool:
    validate_number(number, lambda x: x >= 0, f"{field_name} must be greater or equal than 0")

def validate_is_positive(number: Number, field_name: str) -> bool:
    validate_number(number, lambda x: x > 0, f"{field_name} must be greater than 0")

def validate_number(num: Number, predicate: Callable[[Number], bool], error_message: str) -> Number:
    if not predicate(num):
        raise ValueError(error_message) # TODO: parse message error with field_name
    return num

def validate_status(value: str) -> Status:
    try:
        return Status(value)
    except ValueError:
        raise ValueError(f"Invalid status: {value}. Must be one of {[s.value for s in Status]}")

