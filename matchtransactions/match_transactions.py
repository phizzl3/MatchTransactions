"""Searches every combination of the group of transactions to try to find
    a set that adds up to the given total.
"""

import itertools


def get_total() -> str:
    """Gets the total amount to try to calculate a match for."""
    return input("\nWhat is the total amount?: ")


def get_transactions() -> list:
    """Gets each transaction to combine to look for a matching combo."""
    print("Enter each transaction amount and press enter."
          "\nEnter when done.")
    transactions = []
    while True:
        each = input("Transaction: ").strip("$ ")
        if each:
            transactions.append(float(each.replace(',', '')))
        else:
            return transactions


def find_matches(total: float, transactions: list) -> None:
    """Searches every combination of the group of transactions to try to find
    a set that adds up to the given total.

    Args:
        total (float): The total amount to try to calculate a match for.
        transactions (list): All of the transactions (float) to combine to 
        look for a matching combo.
    """
    match = False
    for i in range(1, len(transactions)+1):
        combos = itertools.combinations(transactions, i)
        for combo in combos:
            if sum(combo) == total:
                print(f"\nMatch Found: sum{combo} = {total}\n")
                match = True
    if not match:
        print("\nNo matches found.")


def main():
    total = get_total()
    transactions = get_transactions()
    find_matches(float(total), transactions)
    input("ENTER to close.")


if __name__ == '__main__':
    main()
