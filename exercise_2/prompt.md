📝 **Prompt**

Implement a serializer/deserializer for a class `Invoice` that includes:

> "invoice_id": string,  
> "issued_date": string (ISO format),  
> "due_date": string (ISO format),  
> "status": enum (values: `UNPAID`, `PAID`, `CANCELLED`),  
> "customer": object with:
> > "customer_id": string,  
> > "name": string,  
> > "email": string,
>
> "line_items": a list of items, each with:
> > "description": string,  
> > "quantity": int,  
> > "unit_price": float,  
> > "notes": optional string (can be `None`)

### Requirements:

1. Implement serialization/deserialization logic without external libraries like `pydantic`.
2. Properly handle enums, lists, and optional fields.
3. Validate that during deserialization:
    - `quantity` must be greater than 0.
    - `unit_price` must be greater than or equal to 0.
    - `status` must be a valid enum value.

### Expected Behavior:

- When serializing an `Invoice` object, it should return a well-structured JSON string.
- When deserializing a JSON string, it should create a valid `Invoice` object and handle errors if the data is invalid (
  e.g., invalid status, negative quantity, or unit price).

```
{
  "invoice_id": "inv_001",
  "issued_date": "2025-05-04T10:00:00Z",
  "due_date": "2025-05-14T23:59:59Z",
  "status": "UNPAID",
  "customer": {
    "customer_id": "cust_123",
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com"
  },
  "line_items": [
    {
      "description": "Website development",
      "quantity": 1,
      "unit_price": 1500.0,
      "notes": "Initial payment"
    },
    {
      "description": "Monthly maintenance",
      "quantity": 3,
      "unit_price": 200.0,
      "notes": null
    }
  ]
}

```