# Define a function to check the account balance
def check_balance(account_balance):
    return f"Your account balance is ${account_balance}."

# Define a function to make a withdrawal
def withdraw(account_balance, amount):
    if amount <= account_balance:
        new_balance = account_balance - amount
        return f"Withdrawal successful! Your new balance is ${new_balance}."
    else:
        return "Insufficient funds. Withdrawal failed."
