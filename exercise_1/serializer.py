import json

from exercise_1.models_dataclass import Transaction, Customer

class JsonSerializer:

    @staticmethod
    def deserialize_transaction(transaction_json: str) -> Transaction:

        parsed_json = json.loads(transaction_json)


        # customer = Customer(**parsed_json["customer"])
        customer = Customer (
          customer_id  = parsed_json["customer"]["customer_id"], #TODO: Check if required.
          name = parsed_json["customer"]["name"],
          email = JsonSerializer._parse_email(parsed_json["customer"]["email"], True) #TODO: Check email regex
        )

        transaction = Transaction(
            transaction_id=parsed_json["transaction_id"],
            amount=float(parsed_json["amount"]), #TODO: check casting, and if its within some limits?
            currency=parsed_json["currency"], #TODO: create enum, and check the currency is listed.
            status=parsed_json["status"], #TODO:
            customer=customer)
        return transaction

    @staticmethod
    def serialize_transaction(transaction: Transaction) -> str:
        # If I can serialize the JSON as-is (using asdict)... Add a comment that Schema is controlled at @dataclasslevel
        # json.dumps(asdict(transaction))

        # Otherwise:
        data = {
            "transaction_id": transaction.transaction_id,
            "amount": transaction.amount,
            "currency": transaction.currency,
            "status": transaction.status,
            "customer": {
                "customer_id": transaction.customer.customer_id,
                "name": transaction.customer.name,
                "email": transaction.customer.email,
            }
        }

        return json.dumps(data)

    @staticmethod
    def _parse_email(email: str, mask_email = False) -> str: # Lets assume for masking, we ***

        if email.count("@") > 1: # TODO: validate regex
            return None

        if mask_email:
            main , domain = email.split("@", maxsplit= 1)
            if len(main) > 3:
                new_main = main[0:3] + "****"
            else:
                new_main = "****"
            return new_main + "@" + domain
        else:
            return email