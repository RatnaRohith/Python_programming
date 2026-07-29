# Program to swap two numbers without using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
