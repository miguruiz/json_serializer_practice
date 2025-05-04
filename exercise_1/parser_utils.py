from dataclasses import dataclass
from enum import Enum

class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    MEX = "MEX"



class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class Transaction:
    def __init__(self,transaction_id,  amount, currency, status, customer):
        self.transaction_id = transaction_id
        self.amount = amount
        self.currency = currency
        self.status = status
        self.customer = customer

