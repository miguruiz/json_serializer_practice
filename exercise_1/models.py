from typing import Optional, List
from enum import Enum

class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    MEX = "MEX"


class Customer:
    def __init__(self, customer_id: int, name: str, email: Optional[str] = None) -> None:
        if not customer_id or not name:
            raise ValueError("customer_id and name are required")

        self.customer_id: int = customer_id
        self.name: str = name
        self.email: Optional[str] = email

class Transaction:
    def __init__(self, transaction_id: int, amount: float, currency: Currency, status: str, customer: Customer, notes: Optional[List[str]] = None) -> None:
        self.transaction_id: int = transaction_id
        self.amount: float = amount
        self.currency: Currency = currency
        self.status: str = status
        self.customer: Customer = customer
        self.notes: Optional[List[str]] = notes if notes is not None else []

