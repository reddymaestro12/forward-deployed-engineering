def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    return a / b


print(divide(10, 0))

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    print("Valid marks entered")

except ValueError as e:
    print("Error:", e)
