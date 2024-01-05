# Import the banking module
import banking_module

# Initialize account balance
initial_balance = 1000

# Check the account balance
balance_result = banking_module.check_balance(initial_balance)
print(balance_result)

# Make a withdrawal
withdrawal_result = banking_module.withdraw(initial_balance, 200)
print(withdrawal_result)

# Attempt a withdrawal with insufficient funds
insufficient_result = banking_module.withdraw(initial_balance, 1200)
print(insufficient_result)

