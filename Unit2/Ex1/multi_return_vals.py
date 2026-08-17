def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication


# Function call
sum_result, difference, product = calculate(10, 5)

print("Addition:", sum_result)
print("Subtraction:", difference)
print("Multiplication:", product)