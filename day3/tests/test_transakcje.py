# assert - asercja
# x = 5
# assert x == 5
# assert x == 50
# Traceback (most recent call last):
#   File "C:\Users\cscomarch\PycharmProjects\warsztat-23-03-2026\day3\tests\test_transakcje.py", line 4, in <module>
#     assert x == 50
#            ^^^^^^^
# AssertionError
# (.venv) PS C:\Users\cscomarch\PycharmProjects\warsztat-23-03-2026\day3\tests>

# day3/tests/test_transakcje.py:None (day3/tests/test_transakcje.py)
# day3\tests\test_transakcje.py:4: in <module>
#     assert x == 50
# E   assert 5 == 50

import transakcje as tr  # jako alias
import pytest


# pytest -v
# mapowanie transakcji
def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert tr.map_transactions(tr.transactions, "USD") == result


def test_reduce_transactions():
    assert tr.reduce_transactions([1000, 500, 700, 0]) == 2200


# test_transakcje.py::test_map_transactions_usd PASSED                                                                                                                                                                         [ 50%]
# test_transakcje.py::test_reduce_transactions PASSED

def test_filter_transactions_income():
    expected_list = [
        {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},

        {'id': 3, "type": "income", "amount": 500, "currency": "USD"},

        {'id': 5, "type": "income", "amount": 700, "currency": "USD"},

        {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]

    assert tr.filter_transactions(tr.transactions, "income") == expected_list

# test_transakcje.py::test_map_transactions_usd PASSED                                                                                                                                                                         [ 33%]
# test_transakcje.py::test_reduce_transactions PASSED                                                                                                                                                                          [ 66%]
# test_transakcje.py::test_filter_transactions_income PASSED
