# ATM Transaction History

transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Calculate current balance
balance = sum(transactions)

# Create separate lists
deposits = [t for t in transactions if t > 0]
withdrawals = [t for t in transactions if t < 0]

# Count deposits and withdrawals
deposit_count = len(deposits)
withdrawal_count = len(withdrawals)

# Find largest deposit and withdrawal
largest_deposit = max(deposits)
largest_withdrawal = min(withdrawals)

# Display results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal) 