import json
from exercise_2.models import Invoice, Customer, LineItems
from exercise_2.utils_types import safe_cast_to_datetime, safe_cast_to_int, safe_cast_to_float
from exercise_2.utils_validation import validate_email, validate_status, validate_is_positive
from utils import get_required_field, get_optional_field, mask_email
from typing import Any



class JsonSerializer:

    @classmethod
    def deserialize_invoice(cls, invoice_json: str, masking: bool = False) -> Invoice:
        if not invoice_json.strip():  # Check if the input is empty or just whitespace
            raise ValueError("invoice_json is empty or just whitespace")
        try:  # Try to parse the JSON string
            data = json.loads(invoice_json)
        except json.JSONDecodeError:
            raise ValueError(f"Malformed JSON: {invoice_json}")

        if not data:  # Check if the parsed JSON is an empty dictionary
            raise ValueError("invoice_json is an empty dictionary")

        customer = cls._parse_customer(
            customer_data=get_required_field(data, "customer"), masking=masking
        )
        line_items = cls._parse_line_items(
            line_items_data=get_required_field(data, "line_items")
        )

        return Invoice(
            invoice_id=get_required_field(data, "invoice_id"),
            issued_date=safe_cast_to_datetime(
                get_required_field(data, "issued_date"), "issued_date"
            ),
            due_date=safe_cast_to_datetime(
                get_required_field(data, "due_date"), "due_date"
            ),
            status=validate_status(get_required_field(data, "status")),
            customer=customer,
            line_items=line_items,
        )

    @staticmethod
    def serialize_invoice(
        invoice: Invoice,
    ) -> str: ...  # TODO: implement serialization logic

    @staticmethod
    def _parse_customer(
        customer_data: dict[str, Any], masking: bool = False
    ) -> Customer:
        customer_id = get_required_field(customer_data, "customer_id")
        name = get_optional_field(customer_data, "name")
        email = validate_email(get_required_field(customer_data, "email"))
        if masking:
            email = mask_email(email)

        return Customer(customer_id=customer_id, name=name, email=email)

    @staticmethod
    def _parse_line_items(line_items_data: dict[str, Any]) -> list[LineItems]:
        line_items = []
        for item in line_items_data:
            line_items.append(
                LineItems(
                    description=get_required_field(item, "description"),
                    quantity=validate_is_positive(
                        safe_cast_to_int(
                            get_required_field(item, "quantity"), "quantity"
                        )
                    ),
                    unit_price=safe_cast_to_float(
                        get_required_field(item, "unit_price"), "unit_price"
                    ),
                    notes=get_optional_field(item, "notes"),
                )
            )
        return line_items


# TODO: What if one field becomes Optional, or required? it seems I would need to change it in many places...
# TODO: Code-Formatter
