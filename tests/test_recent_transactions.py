import pytest
from src.function import recent_transactions
from datetime import datetime

def test_recent_transactions():
    executed_transactions = [
        {'id': 1, 'date': '2023-08-20T10:30:00', "state": "EXECUTED"},
        {'id': 2, 'date': '2023-08-22T15:35:00', "state": "EXECUTED"},
        {'id': 3, 'date': '2023-08-21T12:45:00', "state": "EXECUTED"},
        {'id': 4, 'date': '2023-08-18T14:50:00', "state": "EXECUTED"},
        {'id': 5, 'date': '2023-08-19T19:55:00', "state": "EXECUTED"}
    ]

    expected_result = [
        {'id': 2, 'date': '2023-08-22T15:35:00', "state": "EXECUTED"},
        {'id': 3, 'date': '2023-08-21T12:45:00', "state": "EXECUTED"},
        {'id': 1, 'date': '2023-08-20T10:30:00', "state": "EXECUTED"},
        {'id': 5, 'date': '2023-08-19T19:55:00', "state": "EXECUTED"},
        {'id': 4, 'date': '2023-08-18T14:50:00', "state": "EXECUTED"}
    ]

    assert recent_transactions(executed_transactions) == expected_result