import pytest
from exercise_1.models_dataclass import Transaction, Customer
from exercise_1.serializer import JsonSerializer

test_json = """{
  "transaction_id": "txn_123456",
  "amount": 99.99,
  "currency": "USD",
  "status": "authorized",
  "customer": {
    "customer_id": "cust_7890",
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
}"""

expected_serialized_trans = """{"transaction_id": "foo_id", "amount": 123.45, "currency": "USD", "status": "authorized", "customer": {"customer_id": "bar_id", "name": "John Doe", "email": "jd@me.com"}}"""


#TODO: test edge cases: empty, malformed, etc

@pytest.fixture
def transaction():
    # Fixture to create a sample Transaction object
    return Transaction(
        transaction_id="foo_id",
        amount=123.45,
        currency="USD",
        status="authorized",
        customer=Customer(
            customer_id="bar_id",
            name="John Doe",
            email="jd@me.com"
        )
    )

def test_deserialize_transaction():
    trans_deser = JsonSerializer.deserialize_transaction(test_json)
    assert trans_deser.transaction_id == "txn_123456"
    assert trans_deser.amount == 99.99
    assert trans_deser.customer.customer_id == "cust_7890"
    assert trans_deser.customer.email == "joh****@example.com"

def test_serialize_transaction(transaction):
    # Test serialization of a Transaction object
    trans_ser = JsonSerializer.serialize_transaction(transaction)
    assert trans_ser == expected_serialized_trans


