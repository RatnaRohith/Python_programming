def calculate_bill(amount, tax=5):
    total = amount + (amount * tax / 100)
    return total


print("Bill:", calculate_bill(1000))
print("Bill:", calculate_bill(1000, 10))