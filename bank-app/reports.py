from accounts import registry

def account_summary(account_id):
    acc = registry[account_id]

    print("\n--- Account Summary ---")
    print(f"Owner: {acc['owner']}")
    print(f"Balance: {acc['balance']}")
    print(f"History: {acc['history']}")

def snapshot(account_id):
    acc = registry[account_id]

    snap = acc
    return snap