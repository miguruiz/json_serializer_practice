from enum import Enum
from datetime import datetime
from typing import Optional


class Status(Enum):
    UNPAID = "UNPAID"
    PAID = "PAID"
    CANCELLED = "CANCELLED"


class Customer:
    def __init__(self, customer_id, name: Optional[str], email: Optional[str]):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class LineItems:
    def __init__(self, description: str, quantity: int, unit_price: float, notes: str=None):
        if not isinstance(quantity, int):
            raise TypeError(f"quantity must be an int")
        if not isinstance(unit_price, (float, int)):  # allow ints, auto-convert
            raise TypeError(f"unit_price must be a float")

        self.description = description
        self.quantity = quantity # Int
        self.unit_price = unit_price # float
        self.notes = notes # Optional

class Invoice:
    def __init__(self,invoice_id: str , issued_date: datetime, due_date :datetime, status: Status, customer: Customer, line_items: list[LineItems]):
        if not isinstance(issued_date, datetime):
            raise TypeError(f"issued_date must be an datetime")
        if not isinstance(due_date, datetime):  # allow ints, auto-convert
            raise TypeError(f"unit_price must be a datetime")
        if not isinstance(status, Status):
            raise TypeError(f"status must be a valid Status")

        self.invoice_id = invoice_id
        self.issued_date = issued_date
        self.due_date = due_date
        self.status = status
        self.customer = customer
        self.line_items = line_items


