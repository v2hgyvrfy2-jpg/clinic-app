from accounts import get_account

def deposit(account_id, amount):
    acc = get_account(account_id)

    acc["balance"] += amount
    acc["history"].append(f"Deposit: +{amount}")

    print(f"Deposited {amount}. Balance: {acc['balance']}")

def withdraw(account_id, amount):
    acc = get_account(account_id)

    if acc["balance"] < amount:
        print("Insufficient funds.")
        return

    acc["balance"] -= amount

    acc["history"].append(f"Withdrawal: -{amount}")

    print(f"Withdrew {amount}. Balance: {acc['balance']}")