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


#TODO: test

def test_deserialize_transaction():
    trans_deser = JsonSerializer.deserialize_transaction(test_json)
    assert trans_deser.transaction_id == "txn_123456"
    assert trans_deser.amount == 99.99
    assert trans_deser.customer.customer_id == "cust_7890"

def test_serialize_transaction():
    trans = Transaction (
        transaction_id = "foo_id",
        amount = 123.45,
        currency = "USD",
        status = "authorized",
        customer = Customer (
            customer_id = "bar_id",
            name = "John Doe",
            email = "jd@me.com"
        )
    )
    trans_ser = JsonSerializer.serialize_transaction(trans)
    expected_serializer_trans = """{"transaction_id": "foo_id", "amount": 123.45, "currency": "USD", "status": "authorized", "customer": {"customer_id": "bar_id", "name": "John Doe", "email": "jd@me.com"}}"""
    assert trans_ser == expected_serializer_trans

def test__parse_email():
    valid = "helloWorld@gmail.com"
    invalid = "invalid@email@"


    assert JsonSerializer._parse_email(valid) == "helloWorld@gmail.com"
    assert JsonSerializer._parse_email(valid, True ) == "hel****@gmail.com"
    assert JsonSerializer._parse_email(invalid) == None


