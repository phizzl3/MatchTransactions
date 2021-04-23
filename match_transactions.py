import itertools


def get_total():
    return input("What is the total amount?: ")


def get_transactions():
    print("Enter each transaction amount and press enter."
          "\nEnter when done.")
    t = []
    while True:
        ea = input("Transaction: ").strip("$ ")
        if ea:
            t.append(float(ea.replace(',', '')))
        else:
            return t


def get_combo_number():
    return input("How many transactions should give you this total?: ")


def find_matches(tt, cn, ts):
    combos = itertools.combinations(ts, int(cn))
    match = False
    for combo in combos:
        if sum(combo) == float(tt):
            print(f"Match Found: {combo} = {tt}")
            match = True
    if not match:
        print("No matches found.")


def main():
    total = get_total()
    combo_num = get_combo_number()
    transactions = get_transactions()
    find_matches(total, combo_num, transactions)


if __name__ == '__main__':
    main()
