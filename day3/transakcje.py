from functools import reduce

transactions = [
    {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},
    {'id': 2, "type": "expense", "amount": 200, "currency": "USD"},
    {'id': 3, "type": "income", "amount": 500, "currency": "USD"},
    {'id': 4, "type": "expense", "amount": 300, "currency": "USD"},
    {'id': 5, "type": "income", "amount": 700, "currency": "USD"},
    {'id': 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def filter_transactions(transactions, transaction_type):
    """
    filtruje transakcje po typie transakcji expense, income
    :param transactions:
    :param transaction_type:
    :return:
    """
    return list(filter(lambda x: x['type'] == transaction_type, transactions))


def map_transactions(transactions, currency):
    """
    Mapuje transakcje spełniające warunek waluty na kwote w nowej liście
    :param transactions:
    :param currency:
    :return: lista transakcji
    """
    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


def reduce_transactions(mapped):
    """
    Zsumuje kwoty transakcji
    :param mapped:
    :return: wartości zsumowanych transakcji, int, float
    """
    return reduce(lambda x, y: x + y, mapped, 0)


def process_transactions(transactions, transaction_type, currency):
    pass
