def deduct_wallet(balance, amount):
    if balance >= amount:
        return balance - amount
    return None