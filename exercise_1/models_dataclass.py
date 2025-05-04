from dataclasses import dataclass, field
from typing import Optional, List

from enum import Enum

class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    MEX = "MEX"


@dataclass
class Customer:
    customer_id: str
    name: str
    email: Optional[str] = field(default=None)


@dataclass
class Transaction:
    transaction_id: str
    amount: float
    currency: str
    status: str
    customer: Customer