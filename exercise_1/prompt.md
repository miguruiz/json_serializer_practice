📝 Prompt
You are given a class structure to represent a Payment Transaction. Each transaction has:
> - transaction_id: string
> - amount: float
> - currency: string
> - status: string (e.g., "authorized", "settled", "refunded")
> - customer: an object with:
> - customer_id: string
> - name: string
> - email: string

Implement custom serialization and deserialization logic to convert a Transaction object (including nested Customer) to
a JSON string and back.

## QUESTIONS

[//]: # (- How to best handle defaults, required & optional in the @dataclass?)

- How to best handle the strictness of the validations? Fail on the first, try all and collect errors? Have an object
  that represents the Validations, with the validation elvel?
- How to put in the code the validations? functions? have a class?
- Can @dataclasses have default values?.. Maybe check the logging mode, and depending, log all exceptions, or simple
- How to declare Optionals in @dataclasses
  fail with the first one.
- How to handle Enums or checks against referential data (checking all Currencies)? .. is it good practice in a
  json-deserializer, where are the limits to check?
- What does `pydantic`, `dataclass`, or `marshmallow` do?
- What would be the best way to mask a field (eg. a card, or an email). What is the typical regulation? What are the
  alterantives? (encrypt, hash, mask)
- How to test private methods?
- Is it ok to return None in _parse_email when invalid email?
- In asserts, what is the difference between == and ===?

## TODO FOR THE ASSIGNMENT

*OPTION: FULL*
SERIALIZER_RAW_JSON -> RAW_DESER_JSON (Raw_class)
-----> PARSED_CLASSES --> SER_PARSED_JSON
SERIALIZER_RAW_JSON -> RAW_DESER_JSON (Raw_class)

*OPTION: DIRECT (Avoid representation of raw_classes)*
SERIALIZER_RAW_JSON
-----> PARSED_CLASSES --> SER_PARSED_JSON
SERIALIZER_RAW_JSON

- When parsing the JSON:
    - Check for empty Json
    - Check for mal-formed Json
    - How to handle:
        - empty Json
        - mal-formed JSON
        - Missing required fields
        - Validations: enums, cast types, regex( email, phone-number, card_number).
    - Masking functions
- Logging
- Tests
- Docstrings
- Add a comment in the main for Parse configuration/Args if needed with things like: FailMode [FailFast, etc], Masking[]

## TODO...

- Practice timestamp
- Practice inline If-else
- Practice for comprenhension
- Remove the @dataclass