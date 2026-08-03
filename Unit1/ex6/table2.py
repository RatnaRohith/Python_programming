# Program to Print Multiplication Table using while loop

num = int(input("Enter a number: "))
i = 1

print("\nMultiplication Table of", num)

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1