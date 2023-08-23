import pytest
from src.function import transaction_output

def test_transaction_output_empty_list():
    assert transaction_output([]) == ""

def test_transaction_output_single_transaction():
    single_transaction = [
        {
            "date": "2021-11-01",
            "description": "Перевод",
            "operationAmount": {"amount": 500, "currency": {"name": "руб"}},
            "to": "1234567812345678",
            "from": "2345678923456789",
        }
    ]
    expected_output = "01.11.2021 Перевод\n2345 67** **** 6789 -> Счет **5678\n500 руб\n\n"
    assert transaction_output(single_transaction) == expected_output

def test_transaction_output_multiple_transactions():
    transactions = [
        {
            "date": "2021-11-01",
            "description": "Покупка",
            "operationAmount": {"amount": 300, "currency": {"name": "руб"}},
            "to": "1234567812345678",
            "from": "2345678923456789",
        },
        {
            "date": "2021-11-02",
            "description": "Оплата",
            "operationAmount": {"amount": 1500, "currency": {"name": "руб"}},
            "to": "3456789034567890",
            "from": "Счет 456789012345",
        },
    ]
    expected_output = (
        "01.11.2021 Покупка\n2345 67** **** 6789 -> Счет **5678\n300 руб\n\n"
        "02.11.2021 Оплата\nСчет **2345 -> Счет **7890\n1500 руб\n\n"
    )
    assert transaction_output(transactions) == expected_output