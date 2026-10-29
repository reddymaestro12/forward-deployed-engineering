class InsufficientBalanceError(Exception):
    pass


balance = 1000
withdrawal = 1500

if withdrawal > balance:
    raise InsufficientBalanceError("Withdrawal amount exceeds account balance")
# with try,excpet,else,finally,raise
try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

except ValueError as e:
    print("Error:", e)

else:
    print("Transaction processed successfully")

finally:
    print("Thank you for using the banking system")
